from llama_index import ServiceContext
from llama_index import StorageContext, load_index_from_storage
from llama_index.llms import OpenAI

from .base import BaseQueryEngine


class GPTQueryEngine(BaseQueryEngine):
    def __init__(self):
        super().__init__('GPT', 'gpt-3.5-turbo', "Data/indexes/GPT3.5_index")

    def create_llm(self):
        return OpenAI(model=self.model_id, temperature=0.3)

    def create_query_engine(self):
        print("creating instance of query_engine")
        llm = self.create_llm()
        service_context = ServiceContext.from_defaults(llm=llm)
        storage_context = StorageContext.from_defaults(persist_dir=self.model_index_dir)
        index = load_index_from_storage(storage_context, service_context=service_context)
        return index.as_query_engine()

    def get_system_prompt(self):
        return """ """
