# BiasGen : Data Augementation Guide with GPT

This is code for doing Data Augmentation with GPT systems

Using 10 lines of fake_news.csv we generate <1000 lines of fake_news data

#### How to use the Code

###### 1. Install Dependencies

      `pip install -r requirements.txt`

###### 2. Use the Data of your Choice
Save the data to the same directory that the code is located.


###### 3. Choose a Data Loader

Based on your data type selected the data loader to use for loading in your data.

###### lang chain document loaders : https://python.langchain.com/en/latest/modules/indexes/document_loaders.html

The current code uses a csv file example and uses a CSV loader to call in the data.

        from langchain.document_loaders.csv_loader import CSVLoader

        loader = CSVLoader('fake_news.csv')

###### 4. Get an OpenAI API Key!
Generate an OpenAI API key. Documentation on how to do so can be found here :https://platform.openai.com/account/api-keys 

Once you generate a key, input the key here:

        embeddings = OpenAIEmbeddings(openai_api_key = 'insert_key_here')


###### 5. Get the data!

Finally run  `python3 pl.py` or  `python pl.py` to get your generated data saved to the file format of your choice.

