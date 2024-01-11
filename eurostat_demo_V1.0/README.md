# Eurostat demo App - running on static indexes

##Adding access tokens to .env file
1. create a user OpenAI account -> create access token & add some funding (the price per one request is <= 0.001$, 40$ should be ok for testing)
2. create a user account on replicate.com and create access token (no funding needed) 
3. Paste tokens to .env file: openAI token -> OPENAI_API_KEY= & replicate token -> REPLICATE_API_TOKEN=

## Adding files: indexes & .env
1. Copy index directories for both models to the directory: eurostat_demo/Data/indexes/
2. add .env file with access tokens:
OPENAI_API_KEY=sk-vlo9ro..............
REPLICATE_API_TOKEN=r8_HyC7................

Index directories represent vectorized context data for question & answering with the LLM model. They are created with separate scripts
and can be accessd on gdrive: https://drive.google.com/drive/folders/18F93ZXG5FEVBGSTXLsTxMhsW_1gnW1uC

OpenAI token can be created on openai.com and needs to be credited with funding for token to enable access to OpenAI API.
Replicate token can be created on replicate.com and does not need any crediting (free). Both tokens are copied to .env file.

## Run the app manually
1. pip install requirements.txt
2. got to "eurostat_demo_V1" & run: streamlit run app.py

NOTE: the server runs on "localhost:8501". with both interfaces for the models on same page.

## Run the app as microservice
1. got to "eurostat_demo_V1" 
2. run: docker-compose build & docker-compose up

NOTE: the service runs on "localhost:8050". with both interfaces for the models on same page.
The console prints the user queries received and the gueries_full(sent to LLM).

## Changing system prompt
System prompt is saved in eurostat_demo_V1/Data/configurations/system_prompt.json
Changing the text gets dynamicaly loaded into the app (also when running in docker container). 
The current system prompt used in querying can be seen in console printouts.