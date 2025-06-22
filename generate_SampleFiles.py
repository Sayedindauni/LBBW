import pandas as pd
import os

# Create sample_data directory
os.makedirs('sample_data', exist_ok=True)

# Generate sample data
# 80 perfect matches
matches = pd.DataFrame({
    'ISIN': [f'ISIN{1000+i}' for i in range(80)],
    'Ticker': [f'TICK{i}' for i in range(80)],
    'Name': [f'Company_{i}' for i in range(80)],
    'Currency': ['EUR']*80
})

# 10 mismatched rows: same ISIN but fields differ
mismatches_A = pd.DataFrame({
    'ISIN': [f'ISIN{2000+i}' for i in range(10)],
    'Ticker': [f'TICKA{i}' for i in range(10)],
    'Name': [f'CompA_{i}' for i in range(10)],
    'Currency': ['USD']*10
})
mismatches_B = pd.DataFrame({
    'ISIN': mismatches_A['ISIN'],
    'Ticker': [f'TICKB{i}' for i in range(10)],
    'Name': [f'CompB_{i}' for i in range(10)],
    'Currency': ['USD']*10
})

# 10 unique to A
unique_A = pd.DataFrame({
    'ISIN': [f'ISIN{3000+i}' for i in range(10)],
    'Ticker': [f'TICKUA{i}' for i in range(10)],
    'Name': [f'CompUA_{i}' for i in range(10)],
    'Currency': ['GBP']*10
})

# 10 unique to B
unique_B = pd.DataFrame({
    'ISIN': [f'ISIN{4000+i}' for i in range(10)],
    'Ticker': [f'TICKUB{i}' for i in range(10)],
    'Name': [f'CompUB_{i}' for i in range(10)],
    'Currency': ['JPY']*10
})

# Assemble source A and B
source_A = pd.concat([matches, mismatches_A, unique_A], ignore_index=True)
source_B = pd.concat([matches, mismatches_B, unique_B], ignore_index=True)

# Write to Excel
source_A.to_excel('sample_data/source_A.xlsx', sheet_name='MasterData', index=False)
source_B.to_excel('sample_data/source_B.xlsx', sheet_name='MasterData', index=False)

# Notify user
print("Generated 'sample_data/source_A.xlsx' and 'sample_data/source_B.xlsx' with sample MasterData sheets.")
