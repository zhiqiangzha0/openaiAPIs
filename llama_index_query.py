import os
import logging
import sys
from llama_index import GPTVectorStoreIndex, SimpleWebPageReader
from IPython.display import display


os.environ["OPENAI_API_KEY"] = 'your openai API Key'

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

documents = SimpleWebPageReader().load_data(['http://usada.sakura.vg/contents/sstp.html'])
index = GPTVectorStoreIndex(documents)

response = index.query(
    "SSTPのリクエスト仕様としてCharsetに指定可能な値を全て教えてください。回答には出典のリンクを含めるようにしてください。未定義の場合はundefinedと返してください。")
display(response)