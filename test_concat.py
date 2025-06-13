from datasets import Dataset, DatasetDict

sample = {
    "question": [
        "What is the moon?",
        "What is the sun?"
    ],
    "options": [
        [
            "A star", "A satellite", "A planet", "A comet"
        ],
        [
            "It provides energy", "It causes cold", "It spins fast"
        ]
    ]
        }


datasetdict = DatasetDict({
    "train": Dataset.from_dict(sample)
})

def concact_strategy_001(items):
    list_of_list_concatenated = []

    questions = [str(i) for i in items["question"]]
    all_options = items["options"]
    for index_question, question in enumerate(questions):
        list_concatenated = []
        options_cell = all_options[index_question]
        for option in options_cell:
            concatenated = question + ' ' + option
            list_concatenated.append(concatenated)

        list_of_list_concatenated.append(list_concatenated)

    return {
        "segment_2": list_of_list_concatenated
    }


def data_concat_datasetdict(datasetdict):
  answer= DatasetDict()
  for key in datasetdict:
    modified_dataset = datasetdict[key].map(concact_strategy_001,batched=True)
    answer[key] = modified_dataset
  return answer

enriched_dataset = data_concat_datasetdict(datasetdict)

print()
print("printing:")
print()

for split, dataset in enriched_dataset.items():
    for example in dataset.select(range(1)):
        print(f"question: {example['question']}")
        print(type(example['options']))
        print(type(example['segment_2']))
        print(len(example['segment_2']))
        for segment in example['segment_2']:
          print(f"segment_2: {segment}")
        print()