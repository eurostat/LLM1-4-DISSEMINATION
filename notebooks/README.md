# Running Jupyter Notebooks

## Creating Indexes
The notebooks for index creation are in .notebooks/create_index/ directory:
- Create_Index_GPT.ipynb
- Create_Index_Llama2_13B.ipynb

The scripts load the data files from directory: .notebooks/Data/Jsondata.
Data files used for Index creation include description of table data, table title and description of table columns - samples of the data files are included.
The data files are created with the data preprocessing notebook in directory: ./notebooks/data_preprocesing/Data-preprocessing.ipynb
Two data directories are added:
- ./notebooks/Data/Euro-stat-sample-data/ : samples of raw eurostat data
- ./notebooks/Data/Jsondata : samples of json files used for index creation

## Running the query-answering
There are two separate jupiter notebooks to run GPT3-5 and Llama_13B models under ./notebooks directory:
 - Run_Index_GPT.ipynb
 - Run_Index_Llama2_23B.ipynb



