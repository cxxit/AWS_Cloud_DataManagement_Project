import pandas as pd 

file_path = "data/raw/combined_data_1.txt"
chunk_size = 10000

# with open(file_path, "r") as file: 
#     for _ in range(10):
#         print(file.readline().strip())
def parser_netflix_dataset(file_path = file_path, chunk_size = chunk_size):
    records = [] 
    current_movie_id = None 

    with open(file_path, "r") as file: 
        for line in file: 
            line = line.strip() 

            if line.endswith(":"): 
                current_movie_id = int(line[:-1])
            else: 
                customer_id, rating, date = line.split(",")

                records.append({
                    "movie_id": current_movie_id,
                    "customer_id": customer_id,
                    "rating": int(rating),
                    "date": date
                })

            if len(records) >= chunk_size: 
                df = pd.DataFrame(records)
                yield pd.DataFrame(records)

                print(df.head())
                print(f"Processed {len(df)} records")

                records.clear()
                
        # Process remaining records
        if records:
            df = pd.DataFrame(records)
            yield pd.DataFrame(records)
            print(f"Processed {len(df)} records")


