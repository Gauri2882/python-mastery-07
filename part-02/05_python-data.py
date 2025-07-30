""" Project: Data Cleaner """

import pandas as pd

def load_data(file_path):
    """Load data from CSV file"""
    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully!")
        return df
    except Exception as e:
        print("❌ Error loading data:", e)
        return None

def clean_data(df):
    """Clean the data"""
    print("\n---- Cleaning Data ----")
    print("Initial Shape:", df.shape)

    # Handle missing values
    print("\n🔧 Handling missing values...")
    df = df.dropna()
    print("After dropping missing values:", df.shape)

    # Remove duplicates
    print("\n🧹 Removing duplicates...")
    df = df.drop_duplicates()
    print("After removing duplicates:", df.shape)

    return df

def save_data(df, output_path):
    """Save the cleaned data to a new CSV file"""
    try:
        df.to_csv(output_path, index=False)
        print(f"✅ Cleaned data saved to: {output_path}")
    except Exception as e:
        print("❌ Error saving data:", e)

def main():
    print("🧼 Welcome to the Data Cleaner Tool!")

    # Input file
    input_file = input("📥 Enter the full path to your CSV file: ").strip()
    df = load_data(input_file)
    if df is None:
        return

    # Show initial data
    print("\n---- Initial Data Preview ----")
    print(df.head())

    # Clean the data
    df = clean_data(df)

    # Save cleaned data
    output_file = input("\n📤 Enter the path to save the cleaned CSV file: ").strip()
    save_data(df, output_file)

if __name__ == "__main__":
    main()
