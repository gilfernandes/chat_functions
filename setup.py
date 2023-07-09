from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name='chat_functions', 
        description="Simple demo project showing how you can use ChatGPT functions with LangChain",
        author="Gil Fernandes",
        maintainer="Gil Fernandes",
        version='1.0', 
        packages=find_packages(where="src"),
        options={"bdist_wheel": {"universal": "1"}}
    )