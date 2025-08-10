# 檔案：data_cleaner_v3.py (我們的最終版本)

import pandas as pd

def clean_amazon_data(df):
    """
    [核心清洗函式]
    接收一個從 amazon_scraper_v1.py 產出的原始 DataFrame，
    進行完整的數據清洗與型態轉換，並回傳一個乾淨的 DataFrame。
    """
    # 建立一個副本，避免修改到原始傳入的 DataFrame，這是 pandas 的良好實踐
    cleaned_df = df.copy()

    # --- 清洗排名 (Rank) ---
    if 'Rank' in cleaned_df.columns:
        cleaned_df['Rank'] = cleaned_df['Rank'].astype(str).str.replace('#', '', regex=False)
        cleaned_df['Rank'] = pd.to_numeric(cleaned_df['Rank'], errors='coerce').fillna(0).astype(int)

    # --- 清洗價格 (Price) ---
    if 'Price' in cleaned_df.columns:
        # 你的 .str.extract() 方法非常完美
        cleaned_df['Price'] = pd.to_numeric(cleaned_df['Price'].str.extract(r'(\d+\.?\d*)')[0], errors='coerce')

    # --- 清洗評論數 (Review Count) ---
    if 'Review Count' in cleaned_df.columns:
        # 鏈式寫法：將多個操作串在一起，更簡潔
        cleaned_df['Review Count'] = pd.to_numeric(
            cleaned_df['Review Count'].astype(str).str.replace(',', '', regex=False),
            errors='coerce'
        ).fillna(0).astype(int)

    # --- 清洗評分 (Rating) ---
    if 'Rating' in cleaned_df.columns:
        # 鏈式寫法
        cleaned_df['Rating'] = pd.to_numeric(
            cleaned_df['Rating'].astype(str).str.split(' ').str[0],
            errors='coerce'
        )
    
    # 回傳清洗乾淨的 DataFrame
    return cleaned_df

# ============================================
#         主程式執行區 (Main Execution Block)
# ============================================
if __name__ == "__main__":
    # 1. 讀取原始資料
    input_filename = "amazon_bestsellers2.csv"
    output_filename = "amazon_bestsellers2_cleaned_new.csv"
    
    print(f"正在讀取原始檔案：{input_filename}")
    raw_df = pd.read_csv(input_filename)
    
    print("\n--- 清洗前的資料型態 ---")
    raw_df.info()

    # 2. 呼叫函式進行清洗
    print("\n--- 開始執行數據清洗 ---")
    cleaned_df = clean_amazon_data(raw_df)
    print("--- 數據清洗完成 ---")

    # 3. 預覽並儲存結果
    print("\n--- 清洗後的資料型態 ---")
    cleaned_df.info()
    
    print("\n--- 清洗後的資料預覽 ---")
    print(cleaned_df.head())

    cleaned_df.to_csv(output_filename, index=False, encoding="utf_8_sig")
    print(f"\n任務完成！已將清洗後的資料儲存為 {output_filename}")