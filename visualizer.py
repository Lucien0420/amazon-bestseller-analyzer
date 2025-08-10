# File: visualizer.py
# Responsibility: Reads the cleaned data (cleaned_bestsellers.csv), generates
#                 multiple analytical plots, and saves them to the 'plots' directory.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def visualize_top_reviews(df, output_folder):
    """Sorts products by review count and generates a horizontal bar chart for the top 10.

    Args:
        df (pd.DataFrame): The cleaned product data DataFrame.
        output_folder (str): The folder path to save the generated plot.
    """
    print("--- Generating chart: Top 10 Most Reviewed Products ---")
    top_10 = df.sort_values(by="Review Count", ascending=False).head(10)
    
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 8))
    sns.barplot(x="Review Count", y="Title", data=top_10, palette="viridis")
    plt.title("Top 10 Most Reviewed Products", fontsize=16)
    plt.xlabel("Number of Reviews", fontsize=12)
    plt.ylabel("Product Title", fontsize=12)
    plt.tight_layout()
    
    output_path = os.path.join(output_folder, "top_10_most_reviewed.png")
    plt.savefig(output_path)
    plt.close() # Close the plot to free up memory
    print(f"Chart saved to: {output_path}")

def visualize_price_distribution(df, output_folder):
    """Generates a histogram of the overall product price distribution (including outliers).

    Args:
        df (pd.DataFrame): The cleaned product data DataFrame.
        output_folder (str): The folder path to save the generated plot.
    """
    print("--- Generating chart: Product Price Distribution ---")
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 7))
    sns.histplot(data=df, x="Price", bins=30, kde=True)
    plt.title("Distribution of Product Prices (Full Range)", fontsize=16)
    plt.xlabel("Price (USD)", fontsize=12)
    plt.ylabel("Number of Products", fontsize=12)
    plt.tight_layout()
    
    output_path = os.path.join(output_folder, "price_distribution_full.png")
    plt.savefig(output_path)
    plt.close()
    print(f"Chart saved to: {output_path}")

def visualize_filtered_price_distribution(df, output_folder):
    """Generates a histogram for filtered product prices (under $200).

    Args:
        df (pd.DataFrame): The cleaned product data DataFrame.
        output_folder (str): The folder path to save the generated plot.
    """
    print("--- Generating chart: Filtered Product Price Distribution (< $200) ---")
    df_filtered = df[df['Price'] < 200].copy()
    
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 7))
    sns.histplot(data=df_filtered, x="Price", bins=20, kde=True)
    plt.title("Distribution of Product Prices (Under $200)", fontsize=16)
    plt.xlabel("Price (USD)", fontsize=12)
    plt.ylabel("Number of Products", fontsize=12)
    plt.tight_layout()
    
    output_path = os.path.join(output_folder, "price_distribution_filtered.png")
    plt.savefig(output_path)
    plt.close()
    print(f"Chart saved to: {output_path}")

def visualize_price_vs_rating(df, output_folder):
    """Generates a scatter plot of Price vs. Rating for products under $200.

    Args:
        df (pd.DataFrame): The cleaned product data DataFrame.
        output_folder (str): The folder path to save the generated plot.
    """
    print("--- Generating chart: Price vs. Rating ---")
    df_filtered = df[(df['Price'] < 200) & (df['Rating'].notna())].copy()

    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=df_filtered, x="Price", y="Rating", alpha=0.6, s=80)
    plt.title("Price vs. Rating (for products under $200)", fontsize=16)
    plt.xlabel("Price (USD)", fontsize=12)
    plt.ylabel("Rating (out of 5)", fontsize=12)
    plt.tight_layout()
    
    output_path = os.path.join(output_folder, "price_vs_rating.png")
    plt.savefig(output_path)
    plt.close()
    print(f"Chart saved to: {output_path}")

def visualize_price_vs_review_count(df, output_folder):
    """Generates a scatter plot of Price vs. Review Count, with point size based on Rating.

    Args:
        df (pd.DataFrame): The cleaned product data DataFrame.
        output_folder (str): The folder path to save the generated plot.
    """
    print("--- Generating chart: Price vs. Review Count ---")
    df_filtered = df[(df['Price'] < 200) & (df['Rating'].notna())].copy()

    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=df_filtered, x="Price", y="Review Count", 
                    size="Rating", hue="Rating", sizes=(20, 200), alpha=0.7, palette="viridis")
    plt.title("Price vs. Review Count (Bubble size by Rating)", fontsize=16)
    plt.xlabel("Price (USD)", fontsize=12)
    plt.ylabel("Number of Reviews", fontsize=12)
    plt.tight_layout()

    output_path = os.path.join(output_folder, "price_vs_review_count.png")
    plt.savefig(output_path)
    plt.close()
    print(f"Chart saved to: {output_path}")

def main():
    """The main execution function for the script.
    
    Handles reading the cleaned data, creating the output directory, 
    and calling all visualization functions sequentially.
    """
    input_filepath = os.path.join("output", "data", "cleaned_bestsellers.csv")
    output_dir = os.path.join("output", "plots")

    try:
        print(f"Reading cleaned file: {input_filepath}")
        df_cleaned = pd.read_csv(input_filepath) 
        
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created output directory: {output_dir}")

        # Call all visualization functions
        visualize_top_reviews(df_cleaned, output_dir)
        visualize_price_distribution(df_cleaned, output_dir)
        visualize_filtered_price_distribution(df_cleaned, output_dir)
        visualize_price_vs_rating(df_cleaned, output_dir)
        visualize_price_vs_review_count(df_cleaned, output_dir)
        
        print("\n[--- Visualization module execution complete ---]")
        
    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_filepath}'. Please run cleaner.py first to generate it.")
    except Exception as e:
        print(f"An unexpected error occurred during processing: {e}")

if __name__ == "__main__":
    main()