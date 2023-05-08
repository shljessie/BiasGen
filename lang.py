
from langchain.llms import OpenAI
import os
from langchain.prompts import PromptTemplate

# langchain prompt templates
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

os.environ["OPENAI_API_KEY"] = "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"

llm = OpenAI(temperature=0.9)
# text = "What would be a good company name for a company that makes colorful socks?"
# print(llm(text))

# for generating prompts : https://python.langchain.com/en/latest/modules/prompts/chat_prompt_template.html 


"""
What is a prompt?
A prompt template refers to a reproducible way to generate a prompt.
It contains a text string (“the template”), that can take in a set of parameters from the end user and generate a prompt.

The prompt template may contain:
* instructions to the language model,
* a set of few shot examples to help the language model generate a better response,
* a question to the language model.

Ex) 
template = "I want you to act as a naming consultant for new companies.
What is a good name for a company that makes {product}?
"

prompt = PromptTemplate(
    input_variables=["product"],
    template=template,
)
prompt.format(product="colorful socks")


< Few shot examples to a prompt template> 

from langchain import PromptTemplate, FewShotPromptTemplate

# First, create the list of few shot examples.
examples = [
    {"word": "happy", "antonym": "sad"},
    {"word": "tall", "antonym": "short"},
]

example_formatter_template = ""
Word: {word}
Antonym: {antonym}\n
""
example_prompt = PromptTemplate(
    input_variables=["word", "antonym"],
    template=example_formatter_template,
)

# Finally, we create the `FewShotPromptTemplate` object.
few_shot_prompt = FewShotPromptTemplate(
    # These are the examples we want to insert into the prompt.
    examples=examples,
    # This is how we want to format the examples when we insert them into the prompt.
    example_prompt=example_prompt,
    # The prefix is some text that goes before the examples in the prompt.
    # Usually, this consists of intructions.
    prefix="Give the antonym of every input",
    # The suffix is some text that goes after the examples in the prompt.
    # Usually, this is where the user input will go
    suffix="Word: {input}\nAntonym:",
    # The input variables are the variables that the overall prompt expects.
    input_variables=["input"],
    # The example_separator is the string we will use to join the prefix, examples, and suffix together with.
    example_separator="\n\n",
)

print(few_shot_prompt.format(input="big"))
>> just going to output strings that format 



<Generating reponses with the prompt>

from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
chain.run("colorful socks")
# -> '\n\nSocktastic!'

"""

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)


# using prompt templates directly, define your own template and then pass it in to the SystemMessagePromptTemplate
template="You are a helpful assistant that translates {input_language} to {output_language}."

system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)



# you can create your own prompt templates 
lalprompt=PromptTemplate(
    template="You are a helpful assistant that translates {input_language} to {output_language}.",
    input_variables=["input_language", "output_language"],
)
system_message_prompt_2 = SystemMessagePromptTemplate(prompt=lalprompt)





# prompt script for few shot example generation

from langchain import PromptTemplate, FewShotPromptTemplate
from langchain.chains import LLMChain

# First, create the list of few shot examples.
examples = [
    {"word": "happy", "antonym": "sad"},
    {"word": "tall", "antonym": "short"},
]

example_formatter_template = """
Word: {word}
Antonym: {antonym}\n
"""
example_prompt = PromptTemplate(
    input_variables=["word", "antonym"],
    template=example_formatter_template,
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    #instructions for model
    prefix="Give the antonym of every input",
    suffix="Word: {input}\nAntonym:",
    input_variables=["input"],
    example_separator="\n\n",
)

llm = OpenAI(temperature=0.9)
chain = LLMChain(llm=llm, prompt=few_shot_prompt)
# chain.run(examples)

print(examples)
print(chain.run('sad'))