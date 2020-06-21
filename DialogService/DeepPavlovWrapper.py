import os
from deeppavlov import configs, train_model, build_model
from deeppavlov.core.common.file import read_json

class DeepPavlovWrapper:
	def fit_model(self):
		self.model_config = read_json(configs.doc_retrieval.ru_ranker_tfidf_wiki)
		self.model_config["dataset_reader"]["data_path"] = os.path.abspath(os.getcwd())+"/Resourses"
		self.model_config["dataset_reader"]["dataset_format"] = "txt"
		self.model_config["train"]["batch_size"] = 100
		print("work!")
		self.doc_retrieval = train_model(self.model_config)
		self.squad = build_model(configs.squad.squad_ru_rubert_infer, download=True)
		self.odqa = build_model(configs.odqa.ru_odqa_infer_wiki_rubert, download=False)

	def get_answer_on_question(self, question):
		answers = self.odqa([question])
		print(answers)
		return answers

