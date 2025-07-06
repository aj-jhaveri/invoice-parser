import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def write_to_csv(data, output_path):
    """Writes a list of dictionaries to a CSV file."""
    if not data:
        logging.warning("No data to write to CSV.")
        return

    df = pd.DataFrame(data)
    try:
        df.to_csv(output_path, index=False)
        logging.info(f"Data successfully written to {output_path}")
    except Exception as e:
        logging.error(f"Error writing to CSV: {e}")
