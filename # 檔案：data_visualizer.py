# 檔案：data_visualizer.py (最終版)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def visualize_top_reviews(df, output_folder="plots"):
    # ... (此函式不變) ...
    print("--- 開始分析：評論數最多的前 10 項商品 ---")
    if not os.path.exists(output_folder): os.makedirs(output_folder)
    top_10_reviews = df.sort_values(by="Review Count", ascending=False).head(10)
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 8))
    sns.barplot(x="Review Count", y="Title", data=top_10_reviews, palette="viridis")
    plt.title("Top 10 Most Reviewed Products on Amazon Bestsellers", fontsize=16)
    plt.xlabel("Number of Reviews", fontsize=12)
    plt.ylabel("Product Title", fontsize=12)
    plt.tight_layout()
    output_path = os.path.join(output_folder, "top_10_most_reviewed.png")
    plt.savefig(output_path)
    print(f"圖表已成功儲存至：{output_path}")

def visualize_price_distribution(df, output_folder="plots"):
    # ... (此函式不變) ...
    print("--- 開始分析：商品價格分佈情況 (直方圖) ---")
    if not os.path.exists(output_folder): os.makedirs(output_folder)
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 7))
    sns.histplot(data=df, x="Price", bins=20, kde=True)
    plt.title("Distribution of All Product Prices (including outliers)", fontsize=16)
    plt.xlabel("Price (USD)", fontsize=12)
    plt.ylabel("Number of Products (Frequency)", fontsize=12)
    plt.tight_layout()
    output_path = os.path.join(output_folder, "price_distribution.png")
    plt.savefig(output_path)
    print(f"圖表已成功儲存至：{output_path}")

def visualize_filtered_price_distribution(df, output_folder="plots"):
    # ... (此函式不變) ...
    print("--- 開始分析：過濾後的商品價格分佈 (放大鏡模式) ---")
    if not os.path.exists(output_folder): os.makedirs(output_folder)
    df_filtered = df[df['Price'] < 200].copy()
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 7))
    sns.histplot(data=df_filtered, x="Price", bins=20, kde=True)
    plt.title("Distribution of Product Prices (Under $200)", fontsize=16)
    plt.xlabel("Price (USD)", fontsize=12)
    plt.ylabel("Number of Products (Frequency)", fontsize=12)
    plt.tight_layout()
    output_path = os.path.join(output_folder, "price_distribution_filtered.png")
    plt.savefig(output_path)
    print(f"圖表已成功儲存至：{output_path}")

def visualize_price_vs_rating(df, output_folder="plots"):
    # ... (此函式不變) ...
    print("--- 開始分析：價格 vs 評分 (散佈圖) ---")
    if not os.path.exists(output_folder): os.makedirs(output_folder)
    df_filtered = df[df['Price'] < 200].copy()
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=df_filtered, x="Price", y="Rating", alpha=0.6, s=100)
    plt.title("Price vs. Rating (for products under $200)", fontsize=16)
    plt.xlabel("Price (USD)", fontsize=12)
    plt.ylabel("Rating (out of 5 stars)", fontsize=12)
    plt.tight_layout()
    output_path = os.path.join(output_folder, "price_vs_rating.png")
    plt.savefig(output_path)
    print(f"圖表已成功儲存至：{output_path}")

# ==================================================================
# ▼▼▼▼▼▼▼▼▼▼ 我們新增的最後一個函式 ▼▼▼▼▼▼▼▼▼▼
# ==================================================================
def visualize_price_vs_review_count(df, output_folder="plots"):
    """
    分析並視覺化「價格」與「評論數」之間的關係。
    """
    print("--- 開始分析：價格 vs 評論數 (散佈圖) ---")
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df_filtered = df[df['Price'] < 200].copy()

    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 8))

    # 使用 sns.scatterplot
    # 這次我們加入 hue 參數，讓點的大小根據「評分」變化，增加圖表維度
    sns.scatterplot(data=df_filtered, x="Price", y="Review Count", 
                    size="Rating", hue="Rating", sizes=(20, 200), alpha=0.7, palette="viridis")

    plt.title("Price vs. Review Count (for products under $200)", fontsize=16)
    plt.xlabel("Price (USD)", fontsize=12)
    plt.ylabel("Number of Reviews", fontsize=12)
    
    plt.tight_layout()

    output_path = os.path.join(output_folder, "price_vs_review_count.png")
    plt.savefig(output_path)
    
    print(f"圖表已成功儲存至：{output_path}")

# ============================================
#         主程式執行區 (最終版)
# ============================================
if __name__ == "__main__":
    cleaned_data_filename = "amazon_bestsellers2_cleaned.csv"
    
    try:
        df_cleaned = pd.read_csv(cleaned_data_filename)
        
        # 依序呼叫所有繪圖函式
        visualize_top_reviews(df_cleaned)
        visualize_price_distribution(df_cleaned)
        visualize_filtered_price_distribution(df_cleaned)
        visualize_price_vs_rating(df_cleaned)
        visualize_price_vs_review_count(df_cleaned) # <--- 新增最後的呼叫
        
        print("\n[--- 視覺化模組執行完畢 ---]")
        
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 '{cleaned_data_filename}'。")