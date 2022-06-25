import pandas as pd
from nltk.tokenize import RegexpTokenizer
anime = pd.read_csv('data/anime.csv')

def preprocessed(anime):

    data = anime.copy()

    # dropping na values:

    data.dropna(inplace = True)

    data = data[data.type != 'Music']

    # creating a new feature to have all the tags
    data['tags'] = data['genre'] + ' ' + data['type']
    # taking out the NSFW tags
    data = data[data['tags'].str.contains('Hentai') == False]
    tokenizer = RegexpTokenizer(r'\w+')

    def clean(data1):
        data1 = tokenizer.tokenize(data1)
        data1 = " ".join(data1).lower()

        return data1
    data['tags'] = data['tags'].apply(clean)
    data['name'] = data['name'].apply(clean)

    return data








