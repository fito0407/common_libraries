import pandas as pd
from datasets import Dataset, DatasetDict
import os
import fitos.module_data as fm

folder_path = 'docs'
original_dataset1 = Dataset.from_pandas(pd.read_csv(os.path.join(folder_path, 'correlation_df.csv')))
original_dataset2 = Dataset.from_pandas(pd.read_csv(os.path.join(folder_path, 'correlation_df_short.csv')))
new_dataset1 = fm.reduce_dataset(original_dataset1,10)

print("datasets")
print(type(original_dataset1))
print(len(original_dataset1))
print(type(new_dataset1))
print(len(new_dataset1))


original_dataset_dict= DatasetDict()
original_dataset_dict["A1"]=original_dataset1
original_dataset_dict["A2"]=original_dataset2
dataset_dict= fm.reduce_datasetdictionary(original_dataset_dict,10)

print("dataset dictionaries")
print(type(original_dataset_dict))
print(len(original_dataset_dict["A1"]))
print(len(original_dataset_dict["A2"]))
print(type(dataset_dict))
print(len(dataset_dict["A1"]))
print(len(dataset_dict["A2"]))