# Chat Functions Playground

Simple playground chat app that interacts with OpenAI's functions with memory and custom tools. 

This project contains two attempts at creating an agent with LangChain:
You can find a simple command line application in file 
[agent_cli.py](agent_cli.py).
You can find a small Streamlit application in the file [agent_streamlit.py](agent_streamlit.py)

The agent is in both cases the same and shows how you can create custom tools.

## Pre-requisites

On Linux systems you might need to install g++ before installing ChromaDB.

```
sudo apt install g++
```

Please install a conda environment by running the following commands so that you can run this simple agent.

```
conda activate langchain_streamlit
pip install langchain
pip install prompt_toolkit
pip install wikipedia
pip install arxiv
pip install python-dotenv
pip install streamlit
pip install openai
pip install duckduckgo-search
```



And make sure you have a `.env` file in the root folder with the OPENAI_API_KEY system variable, like e.g:

```
OPENAI_API_KEY=<key>
```

## Build

```
pip install -U pip build twine
```

## Run 

You can run the command line agent on the console by typing:
```bash
python.exe ./agent_playground.py 
```

You can run the Streamlit agent on the console by typing:
```bash
streamlit run ./agent_streamlit.py --server.port 8080
```



