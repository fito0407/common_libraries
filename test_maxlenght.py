from datasets import Dataset, DatasetDict
import fitos.fito_module_data as fm

sample ={
	"question": [
		"What is the moon?",
		"What is the sun?"
	],
	"options": [
		[
			"A star",
			"A satellite",
			"A planet",
			"A comet"
		],
		[
			"It provides energy",
			"It causes cold",
			"It spins fast"
		]
	],
	"input_ids": [
		[
			[18,24,75],
			[18,24],
			[18,24],
			[18,24]
		],
		[
			[18,24,35,18,24],
			[18,24,35],
			[18,24,35],
		]
	]

}


datasetdict = DatasetDict({
    "train": Dataset.from_dict(sample)
    ,"validation": Dataset.from_dict(sample)
})

aa=fm.get_maxlenght_datasetdictionary(datasetdict)
a=1