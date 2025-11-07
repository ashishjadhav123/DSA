import pandas as pd

def read_large_excel(file_name, sheet_name=0, chunk_size=5000):
    """Generator to read Excel file in chunks."""
    excel_iter = pd.read_excel(file_name, sheet_name=sheet_name, chunksize=chunk_size)
    for chunk in excel_iter:
        yield chunk

# Write chunks to CSV with header only for the first chunk
first_chunk = True

for chunk in read_large_excel("large_data.xlsx", chunk_size=5000):
    # Example data cleaning
    chunk['Age'] = chunk['Age'].fillna(chunk['Age'].mean())

    # Write to CSV
    chunk.to_csv(
        "processed_data.csv",
        mode='a',                 # append mode
        index=False,
        header=first_chunk        # only write header for the first chunk
    )

    first_chunk = False           # After first write, no more headers
