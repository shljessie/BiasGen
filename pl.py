from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
#opensource preprocessing tools for unstructured data : https://github.com/Unstructured-IO/unstructured
#lang chain document loaders : https://python.langchain.com/en/latest/modules/indexes/document_loaders.html
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.evaluation.qa import QAGenerateChain

#load data
loader = CSVLoader('fake_news.csv')
documents = loader.load()

#split the text
# we do chunking to help the model understand the text better
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# embed the text
# Chroma is a vector store and embeddings database designed from the ground-up to make it easy to build AI applications with embeddings
# https://www.trychroma.com/
embeddings = OpenAIEmbeddings(openai_api_key = '')
docsearch = Chroma.from_documents(texts, embeddings)
qa = RetrievalQA.from_llm(llm=OpenAI(openai_api_key = ''), retriever=docsearch.as_retriever())

example_gen_chain = QAGenerateChain.from_llm(OpenAI(openai_api_key = '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'))
new_examples = example_gen_chain.apply_and_parse([{"doc": t} for t in texts[:5]])

print(new_examples)

