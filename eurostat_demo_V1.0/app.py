import datetime
import os
import json
import streamlit as st
from dotenv import load_dotenv
import logging

from models import query_engine_factory
from htmlTemplates import css
import openai

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

logging.basicConfig(level=logging.INFO)  # Set the logging level according to your needs
logger = logging.getLogger(__name__)


@st.cache_resource
def login_to_huggingface():
    logger.info("logging into HuggingFace")
    os.system(f"huggingface-cli login --token {os.environ.get('HUGGING_FACE_TOKEN')}")


@st.cache_resource
def create_query_engines():
    query_engines = dict()
    for model in query_engine_factory.get_models():
        logger.info(f"setting the query engine {model}")
        query_engines[model] = query_engine_factory.generate_query_engine(model)
        logger.info(f"query engine {model} set")
    return query_engines


def process_user_question(query_engine, model, st, query):
    logger.info(f"processing the query {model}")
    response = query_engine.query(query)
    st.write(response, unsafe_allow_html=True)
    logger.info(f"query processed {model}")
    return response


def main():
    st.set_page_config(page_title="👨‍💻 Chat with EuroStat Data:", page_icon=":")
    st.write(css, unsafe_allow_html=True)

    # login_to_huggingface()
    query_engines = create_query_engines()
    logger.info('models: %s', ', '.join(query_engines.keys()))

    # Initialize session state variables
    if 'queries_cashed' not in st.session_state:
        st.session_state.queries_cashed = {str(model): ["", ""] for model in query_engines}

    for model in query_engines:
        logger.info(f'Adding for query engine {model}')
        st.header(f"Ask {model} about EuroStat :🧊:")
        user_question = st.text_input(f"Insert question for {model}:")

        # check if question in cache
        if user_question and user_question == st.session_state.queries_cashed[str(model)][0]:
            st.write(st.session_state.queries_cashed[str(model)][1], unsafe_allow_html=True)

        #create LLM response
        elif user_question and st.session_state.queries_cashed[str(model)][0] != user_question:
            logger.info("user_question: %s", user_question)

            with open("Data/Configurations/system_prompt.json", 'r') as file:
                system_prompt = json.load(file)["system_prompt"]
            query = system_prompt + user_question
            logger.info("FULL QUERY: %s", query)

            #cashing the  query and response
            response = process_user_question(query_engines[model], model, st, query)
            st.session_state.queries_cashed[str(model)] = [user_question, response]


if __name__ == '__main__':
    main()