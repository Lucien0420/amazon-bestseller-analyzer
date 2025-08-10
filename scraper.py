# File: scraper.py
# Responsibility: Scrapes product data from the Amazon Best Sellers page 
#                 and saves it as raw_bestsellers.csv.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_page_content(url, headers):
    """Sends an HTTP GET request to fetch the HTML content of a specified URL.

    Args:
        url (str): The URL of the target webpage.
        headers (dict): The HTTP headers to use for the request, used to simulate a browser.

    Returns:
        str | None: The HTML text content of the page if the request is successful 
                    (HTTP status 200), otherwise None.
    """
    print(f"Fetching page: {url}")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raises an exception if the status code is not 200
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def parse_product_data(html_content):
    """Parses the HTML of an Amazon Best Sellers page to extract structured information for all products.

    Args:
        html_content (str): The complete HTML content string containing the product list.

    Returns:
        list[dict]: A list of product dictionaries. Each dictionary represents one product 
                    and contains its rank, title, price, etc. Returns an empty list if 
                    there is no content or parsing fails.
    """
    if html_content is None:
        return []

    soup = BeautifulSoup(html_content, "lxml")
    products_data = []
    
    product_blocks = soup.find_all('div', id='gridItemRoot')
    print(f"Parsing... Found {len(product_blocks)} products in total.")

    for block in product_blocks:
        try:
            rank_tag = block.find('span', class_='zg-bdg-text')
            title_block = block.find('div', class_='_cDEzb_p13n-sc-css-line-clamp-3_g3dy1')
            link_tag = block.find('a', class_='a-link-normal')
            price_tag = block.find('span', class_='_cDEzb_p13n-sc-price_3mJ9Z') or block.find('span', class_='p13n-sc-price')
            rating_tag = block.find('span', class_='a-icon-alt')
            review_tag = block.find('span', class_='a-size-small')

            product = {
                "Rank": rank_tag.text.strip() if rank_tag else "N/A",
                "Title": title_block.text.strip() if title_block else "N/A",
                "Price": price_tag.text.strip() if price_tag else "N/A",
                "Rating": rating_tag.text.strip() if rating_tag else "N/A",
                "Review Count": review_tag.text.strip() if review_tag else "N/A",
                "URL": "https://www.amazon.com" + link_tag['href'] if link_tag else "N/A"
            }
            products_data.append(product)

        except Exception as e:
            print(f"Error parsing a product block, skipping: {e}")
            continue

    return products_data

def save_to_csv(data, filename):
    """Saves the extracted list of data to a CSV file.

    Args:
        data (list[dict]): The list of product dictionaries to save.
        filename (str): The path and name of the output CSV file.

    Returns:
        None: This function does not return any value.
    """
    if not data:
        print("Warning: No data available to save.")
        return

    df = pd.DataFrame(data)
    # Use utf_8_sig encoding to ensure proper display in Excel for non-ASCII characters.
    df.to_csv(filename, index=False, encoding='utf_8_sig')
    print(f"Data successfully saved to {filename}")

def main():
    """The main function and entry point for the script's execution.
    
    Orchestrates the entire workflow of fetching, parsing, and saving the data.
    """
    target_url = "https://www.amazon.com/Best-Sellers-Computers-Accessories/zgbs/pc/"
    my_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    
    html = get_page_content(target_url, my_headers)
    
    if html:
        product_list = parse_product_data(html)
        # As per standardization requirements, specify the output filename as raw_bestsellers.csv
        save_to_csv(product_list, filename="raw_bestsellers.csv")

if __name__ == "__main__":
    main()