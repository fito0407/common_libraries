import random
from datasets import DatasetDict
from pyarrow import dictionary


def reduce_dataset(dataset_original, percentage_target):
    """
        It reduces a dataset to certain percentage

        Args:
            dataset_original: The dataset.

            percentage_target: New ds = p% of old ds.

        Returns:
            dict: The reduced dataset.
    """
    answer= dataset_original
    if (percentage_target>=0) & (percentage_target<100):
      subset_size = max(1, int(percentage_target/100 * len(dataset_original)))
      indices_to_keep = random.sample(range(len(dataset_original)), subset_size)
      answer = dataset_original.select(indices_to_keep)
    return answer

def reduce_datasetdictionary(datasetdictionary_original, percentage_target):
    """
            It reduces each dataset of a dataset dictionary to certain percentage

            Args:
                dataset_original: The dataset.

                percentage_target: New ds = p% of old ds.

            Returns:
                dict: The reduced dataset dictionary.
    """
    answer= DatasetDict()
    for key in datasetdictionary_original:
        dataset_original= datasetdictionary_original[key]
        dataset_reduced= reduce_dataset(dataset_original, percentage_target)
        answer[key] = dataset_reduced
    return answer

def get_maxlenght_datasetdictionary(datasetdictionary):
    answer = {}
    for key_superior, dataset in datasetdictionary.items():
        answer[key_superior] = {}

        columns_dict = {col: dataset[col] for col in dataset.column_names}
        for column_name, values in columns_dict.items():
            answer[key_superior][column_name] = max_list_elements(values)
    return answer

def max_list_elements(list_items):
    answer=0
    if list_items is not None:
        if any(isinstance(item, list) for item in list_items):
            buffer=[]
            for item in list_items:
                buffer.append(max_list_elements(item))
            answer = max(buffer)
        else:
            answer=len(list_items)

    return answer

def get_minlenght_datasetdictionary(datasetdictionary):
    answer = {}
    for key_superior, dataset in datasetdictionary.items():
        answer[key_superior] = {}

        columns_dict = {col: dataset[col] for col in dataset.column_names}
        for column_name, values in columns_dict.items():
            answer[key_superior][column_name] = min_list_elements(values)
    return answer

def min_list_elements(list_items):
    answer=0
    if list_items is not None:
        if any(isinstance(item, list) for item in list_items):
            buffer=[]
            for item in list_items:
                buffer.append(min_list_elements(item))
            answer = min(buffer)
        else:
            answer=len(list_items)

    return answer