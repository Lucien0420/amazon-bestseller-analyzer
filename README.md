# Project: Amazon Eye (V1.1)

An end-to-end data pipeline project that scrapes, cleans, and visualizes best-selling products from Amazon to uncover market insights. This project demonstrates proficiency in web scraping, data manipulation, and data visualization using Python.

## Features

* **Web Scraping:** Scrapes product information from Amazon's Best-Sellers page, including rank, title, price, rating, and review count, using `requests` and `BeautifulSoup`.
* **Data Cleaning:** Processes the raw scraped data into a structured and clean format using `pandas`, handling missing values and converting data types for analysis.
* **Data Visualization:** Generates multiple insightful charts with `matplotlib` and `seaborn` to reveal trends in pricing, product popularity, and customer ratings.

## Tech Stack

* Python 3
* Requests
* BeautifulSoup4
* Pandas
* Matplotlib
* Seaborn

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Lucien0420/Project-Amazon-Eye.git](https://github.com/Lucien0420/Project-Amazon-Eye.git)
    cd Project-Amazon-Eye
    ```
2.  **Install dependencies:**
    ```bash
    pip install requests beautifulsoup4 pandas matplotlib seaborn
    ```
3.  **Execute the pipeline:**
    The scripts are designed to be run in sequence.
    ```bash
    # Step 1: Scrape raw data and save to raw_data.csv
    python amazon_scraper_v1.py
    
    # Step 2: Clean the raw data and save to cleaned_data.csv
    python data_cleaner_v3.py
    
    # Step 3: Generate visualization plots from cleaned data
    python data_visualizer.py
    ```
    After execution, all generated charts will be saved in the `plots/` directory.

## Analysis Results Preview

#### 1. Price Distribution (All Products)
![Price Distribution](plots/price_distribution.png)
* **Insight:** Most products are concentrated in the lower price range, with a few high-priced outliers that could skew analysis.

#### 2. Price Distribution (Filtered, Under $200)
![Filtered Price Distribution](plots/price_distribution_filtered.png)
* **Insight:** After filtering, it's clear that the majority of best-sellers are priced under $50.

#### 3. Top 10 Most Reviewed Products
![Top 10 Most Reviewed Products](plots/top_10_most_reviewed.png)
* **Insight:** Provides a clear view of the most popular items, which can inform market selection strategies.

#### 4. Price vs. Rating Scatter Plot
![Price vs. Rating](plots/price_vs_rating.png)
* **Insight:** For products under $200, there is no strong correlation suggesting that higher price equals higher rating, indicating the prevalence of high value-for-money products.

#### 5. Price vs. Review Count (with Rating dimension)
![Price vs. Review Count](plots/price_vs_review_count.png)
* **Insight:** This multi-dimensional plot reveals that many "blockbuster" products with extremely high review counts are very affordably priced (under $50) and generally have high ratings (indicated by the greener, larger dots), highlighting the core consumer market segment.

---

# 專案：亞馬遜之眼 (Project: Amazon Eye) V1.1

這是一個端到端的數據管道專案，旨在從亞馬遜網站上抓取「電腦與配件」類別的暢銷商品資訊，並對其進行清洗、分析與可視化，以挖掘潛在的市場趨勢。

## 核心功能

* **數據抓取 (Scraping):** 使用 `requests` 與 `Beautiful Soup` 抓取亞馬遜暢銷榜單頁面的商品資訊，包括排名、標題、價格、評分與評論數。
* **數據清洗 (Cleaning):** 使用 `pandas` 對抓取到的原始數據進行格式化處理，將價格、評分等欄位轉換為可用於分析的數字格式。
* **數據可視化 (Visualization):** 使用 `matplotlib` 與 `seaborn` 生成多維度的分析圖表，提供商業洞見。

## 技術棧 (Tech Stack)

* Python 3
* Requests
* BeautifulSoup 4
* Pandas
* Matplotlib
* Seaborn

## 安裝與執行

1.  **複製專案庫**
    ```bash
    git clone [https://github.com/Lucien0420/Project-Amazon-Eye.git](https://github.com/Lucien0420/Project-Amazon-Eye.git)
    cd Project-Amazon-Eye
    ```
2.  **安裝依賴套件**
    ```bash
    pip install requests beautifulsoup4 pandas matplotlib seaborn
    ```
3.  **執行數據管道**
    腳本被設計為依序執行。
    ```bash
    # 步驟一：抓取原始數據並存檔
    python amazon_scraper_v1.py
    
    # 步驟二：清洗數據並存檔
    python data_cleaner_v3.py
    
    # 步驟三：由清洗後的數據生成可視化圖表
    python data_visualizer.py
    ```
    執行完畢後，所有圖表將會自動儲存在 `plots/` 資料夾下。

## 分析成果預覽

#### 1. 商品價格分佈 (含離群值)
![商品價格分佈](plots/price_distribution.png)
* **洞見:** 大部分商品集中在低價區間，但存在少數高價商品，可能是分析時的干擾項。

#### 2. 商品價格分佈 (過濾後, < $200)
![過濾後的商品價格分佈](plots/price_distribution_filtered.png)
* **洞見:** 去除高價商品後，可以更清晰地看到暢銷商品主要集中在 $0 - $50 美元區間。

#### 3. 評論數 Top 10 商品
![評論數 Top 10 商品](plots/top_10_most_reviewed.png)
* **洞見:** 市場熱度最高的商品類型可以一目了然，為選品提供參考。

#### 4. 價格 vs. 評分 (散佈圖)
![價格 vs. 評分](plots/price_vs_rating.png)
* **洞見:** 在 $200 美元以下，似乎沒有「越貴評分越高」的絕對趨勢，高性價比商品普遍存在。

#### 5. 價格 vs. 評論數 (含評分維度)
![價格 vs. 評論數](plots/price_vs_review_count.png)
* **洞見:** 這張圖揭示了更複雜的關係。許多評論數極高的「爆款」商品，價格都非常親民（低於 $50），且評分普遍不低（綠色點代表高分），這可能是市場的主力消費區間。