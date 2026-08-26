from pathlib import Path
import pyarrow as pa 
import pyarrow.parquet as pq
from src.transformation.netflix_parser import parser_netflix_dataset

RAW_FILE = Path("data/raw/combined_data_1.txt")
PROCESSED_DIR = Path("data/processed")

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def ingest(file_path): 
    output_path = PROCESSED_DIR / f"{file_path.stem}.parquet"
    writer = None 

    try: 
        for df in parser_netflix_dataset(file_path): 
            table = pa.Table.from_pandas(df, preserve_index = False)

            if writer is None: 
                writer = pq.ParquetWriter(
                    output_path,
                    table.schema
                )
            writer.write_table(table)

            print(f"Processed {len(df)} records")

    finally: 
        if writer is not None: 
            writer.close() 

    print(f"Created: {output_path}")

if __name__ == "__main__": 
    # ingest(RAW_FILE)
    pass
    
