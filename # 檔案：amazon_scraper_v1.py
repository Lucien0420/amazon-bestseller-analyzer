# 檔案：amazon_scraper_v1.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_page_content(url, headers):
    """
    [買菜函式]
    負責發送網路請求並獲取頁面 HTML 內容。
    """
    print(f"正在抓取頁面：{url}")
    try:
        response = requests.get(url, headers=headers, timeout=10) # 加上 timeout 避免無限等待
        response.raise_for_status() # 檢查 HTTP 狀態碼是否為 200
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"抓取頁面時發生錯誤：{e}")
        return None

def parse_product_data(html_content):
    """
    [洗菜函式]
    負責解析 HTML，從中提取所有商品資訊。
    """
    if html_content is None:
        return []

    soup = BeautifulSoup(html_content, "lxml")
    products_data = []
    
    # 根據 Lucien 你的偵查報告，我們的主要目標是 id='gridItemRoot' 的區塊
    product_blocks = soup.find_all('div', id='gridItemRoot')
    
    print(f"分析中... 總共找到 {len(product_blocks)} 件商品。")

    for block in product_blocks:
        try:
            # --- 開始從 block (大箱子) 中尋找具體資訊 ---

            # 1. 排名 (Rank)
            rank_tag = block.find('span', class_='zg-bdg-text')
            rank = rank_tag.text.strip() if rank_tag else "N/A"

            # 2. 標題 (Title) & 連結 (Link)
            # 我們先找到包含連結和標題的 <a> 標籤
            link_tag = block.find('a', class_='a-link-normal aok-block')
            title = block.find('div', class_='_cDEzb_p13n-sc-css-line-clamp-3_g3dy1')
            if link_tag:
                title = title.text.strip()
                # 記得拼接 base_url
                link = "https://www.amazon.com" + link_tag['href']
            else:
                title = "N/A"
                link = "N/A"

            # 3. 價格 (Price)
            price_tag = block.find('span', class_='p13n-sc-price') or block.find('span', class_='_cDEzb_p13n-sc-price_3mJ9Z')
            price = price_tag.text.strip() if price_tag else "N/A"

            # 4. 評分 (Rating)
            rating_tag = block.find('span', class_='a-icon-alt')
            rating = rating_tag.text.strip() if rating_tag else "N/A"

            # 5. 評論數 (Review Count)
            review_tag = block.find('span', class_='a-size-small')
            review_count = review_tag.text.strip() if review_tag else "N/A"

            # --- 將所有資訊組合成一個字典 ---
            product = {
                "Rank": rank,
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Review Count": review_count,
                "URL": link
            }
            products_data.append(product)

        except Exception as e:
            print(f"解析某個商品區塊時發生錯誤：{e}")
            continue # 即使某個區塊出錯，也跳過，繼續處理下一個

    return products_data

def save_to_csv(data, filename="amazon_bestsellers2.csv"):
    """
    [上菜函式]
    負責將資料儲存成 CSV。
    """
    if not data:
        print("沒有資料可以儲存。")
        return

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf_8_sig')
    print(f"資料已成功儲存至 {filename}")

def main():
    """
    [總指揮函式]
    負責調度以上所有函式，完成整個專案流程。
    """
    target_url = "https://www.amazon.com/Best-Sellers-Computers-Accessories/zgbs/pc/"
    my_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9' # Pro Tip: 加上語言偏好，讓 Amazon 回傳英文頁面
    }
    
    html = get_page_content(target_url, my_headers)
    
    if html:
        product_list = parse_product_data(html)
        save_to_csv(product_list)

# --- 程式執行的入口 ---
# 這是一個 Python 的慣例寫法，確保只有當這個檔案被「直接執行」時，
# main() 函式才會被呼叫。如果是被其他檔案 import，則不會自動執行。
if __name__ == "__main__":
    main()