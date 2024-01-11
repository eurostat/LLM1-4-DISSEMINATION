from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index import LangchainEmbedding
from llama_index import ServiceContext
from llama_index import StorageContext, load_index_from_storage
from llama_index.llms import HuggingFaceLLM
from llama_index.llms import Replicate

from .base import BaseQueryEngine

class LlamaQueryEngine_13B(BaseQueryEngine):
    def __init__(self):
        super().__init__('LLAMA_13B', "meta/llama-2-13b-chat:9dff94b1bed5af738655d4a7cbcdcde2bd503aa85c94334fe1f42af7f3dd5ee3", "Data/indexes/llama_13B_index")
        self.embed_model = "local:BAAI/bge-small-en-v1.5"

    def get_system_prompt(self):
        return """ """

    def create_llm(self):
        return Replicate(
            model=self.model_id,
            is_chat_model=True,
            additional_kwargs={"max_new_tokens": 512}
        )

    def create_query_engine(self):
        print("creating context service llama_13B")
        llm = self.create_llm()
        service_context = ServiceContext.from_defaults(llm=llm, embed_model=self.embed_model)
        storage_context = StorageContext.from_defaults(persist_dir=self.model_index_dir)
        print("loading llama_13B index")
        index = load_index_from_storage(storage_context, service_context=service_context)

        return index.as_query_engine(response_mode="compact")
