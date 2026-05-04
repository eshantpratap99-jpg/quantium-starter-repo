import pandas as pd
import glob

# 1. Collect all three CSV files from the data folder
files = glob.glob("data/*.csv")

# 2. Read and combine them into one single table
df_list = [pd.read_csv(f) for f in files]
df = pd.concat(df_list, ignore_index=True)

# 3. Filter for "Pink Morsel" only
df = df[df['product'].str.lower() == 'pink morsel'].copy()

# 4. Create "sales" column (Price * Quantity)
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
df['sales'] = df['price'] * df['quantity']

# 5. Keep only the three fields: sales, date, region
df = df[['sales', 'date', 'region']]

# 6. Save the final result
df.to_csv("formatted_data.csv", index=False)

print("Formatted data file created successfully!")