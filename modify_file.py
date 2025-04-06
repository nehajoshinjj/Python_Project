import pandas as pd
import os

def process_quantum_file(file_path):
    # Step 1: Read the file
    df = pd.read_csv(file_path)

    # Step 2: Replace headers
    header_map = {
        'CCY': 'UsRate',
        'USD_RATE': 'UsRate',
        'AUD_RATE': 'AudRate'
    }
    df.rename(columns=lambda x: header_map.get(x.strip().replace(" ", ""), x), inplace=True)

    # Step 3: Remove '-' from filename
    dir_name, original_file = os.path.split(file_path)
    new_file_name = original_file.replace("-", "")
    new_file_path = os.path.join(dir_name, new_file_name)

    # Save the modified file
    df.to_csv(new_file_path, index=False)
    print(f"Processed file saved as: {new_file_path}")

# Example usage:
process_quantum_file('Source-Data.csv')
