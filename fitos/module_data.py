import random
from datasets import DatasetDict

def reduce_dataset(dataset_original, percentage_target):
    answer= dataset_original
    if (percentage_target>=0) & (percentage_target<100):
      subset_size = max(1, int(percentage_target/100 * len(dataset_original)))
      indices_to_keep = random.sample(range(len(dataset_original)), subset_size)
      answer = dataset_original.select(indices_to_keep)
    return answer

def reduce_datasetdictionary(datasetdictionary_original, percentage_target):
    answer= DatasetDict()
    for key in datasetdictionary_original:
        dataset_original= datasetdictionary_original[key]
        dataset_reduced= reduce_dataset(dataset_original, percentage_target)
        answer[key] = dataset_reduced
    return answer