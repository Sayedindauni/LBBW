import pandas as pd

# 1. Load sheets
A = pd.read_excel('sample_data/source_A.xlsx', sheet_name='MasterData')
B = pd.read_excel('sample_data/source_B.xlsx', sheet_name='MasterData')

# 2. Merge with indicator
merged = A.merge(B, on='ISIN', how='outer', suffixes=('_A','_B'), indicator=True)

# 3. Identify mismatches
#   - Rows not present in both (“left_only” or “right_only”)
#   - Or present in both but any field differs
def row_diff(row):
    if row['_merge'] != 'both':
        return True
    for col in ['Ticker','Name','Currency']:
        if row[f'{col}_A'] != row[f'{col}_B']:
            return True
    return False

diffs = merged[merged.apply(row_diff, axis=1)]

# 4. Write output
with pd.ExcelWriter('mismatches.xlsx') as writer:
    diffs.to_excel(writer, sheet_name='Mismatches', index=False)
    # summary
    summary = pd.DataFrame({
        'Matched': [len(merged) - len(diffs)],
        'Mismatched': [len(diffs)]
    })
    summary.to_excel(writer, sheet_name='Summary', index=False)



