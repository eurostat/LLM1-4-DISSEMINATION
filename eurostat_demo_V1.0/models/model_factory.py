from .gpt_model import GPTQueryEngine
from .llama_model_13b import LlamaQueryEngine_13B

class ModelFactory:
    def __init__(self):
        self.supported_models = {'GPT': GPTQueryEngine, 'LLAMA_13B': LlamaQueryEngine_13B}

    def get_models(self):
        return self.supported_models

    def generate_query_engine(self, model):
        if model not in self.supported_models:
            return None
        selected_model = self.supported_models[model]
        return selected_model().create_query_engine()

query_engine_factory = ModelFactory()
