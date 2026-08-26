import pandas as pd 

df = pd.read_parquet("data/processed/combined_data_1.parquet")

print("Parquet rows:", len(df))
count = 0
with open("data/raw/combined_data_1.txt", "r") as file: 
    for line in file: 
        line = line.strip() 
        if line.endswith(":"): 
            continue 
        else: 
            count+=1


print(count)

# if count == len(df) then all records in txt file has been correctly transformed and trasnferred into the parquet file



    



