from abc import abstractmethod

from llama_index.prompts.prompts import SimpleInputPrompt


class BaseQueryEngine:
    def __init__(self, model_name, model_id, model_index_dir):
        self.model_name = model_name
        self.model_id = model_id
        self.model_index_dir = model_index_dir

    @abstractmethod
    def create_query_engine(self):
        pass
    
    @abstractmethod
    def get_system_prompt(self):
        pass

    @abstractmethod
    def create_llm(self):
        pass

    def get_query_wrapper_prompt(self):
        # read from file
        final_prompt = SimpleInputPrompt("[INST]<<SYS>>\n" + self.get_system_prompt() + "<</SYS>>\n\n{query_str}[/INST]")
        print (final_prompt)
        return final_prompt