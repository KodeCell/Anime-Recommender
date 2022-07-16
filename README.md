# Anime-Recommender


## Description

An anime recommender webapp hosted on streamlit.

* Basic Text preprocessing was done on the descriptions and genres columns.
* New atrribute 'Tags' was formed from all the text fields in the dataset.
* Tags were converted into vectors to get the group of similar animes together.More about this topic can be found out [here](https://www.geeksforgeeks.org/using-countvectorizer-to-extracting-features-from-text/)
* Cosine Similarity was used to get the top 5 similar animes from our vector space.
## Cosine Similarity
![image](https://user-images.githubusercontent.com/66371234/179339903-34b64b46-aae0-4ba9-a9c6-53b5909ca658.png)<br />
Cosine similarity can be understood by the above image. In the dataset we convert texts to vectors in a n dimensional space which will help us to find the items close to each other based on the angles between them.

## Demo 


https://user-images.githubusercontent.com/66371234/179339520-e726b364-954a-4e7a-bfd6-9a5977fc0d32.mp4

The long running time of the app is due to the huge dataset and the limitation of streamlit to run such huge dataset.

## Datasets
Anime csv can be downloaded from : *https://raw.githubusercontent.com/KodeCell/Anime-Recommender/master/data/anime.csv* <br />
Ratings csv can be downloaded from : *https://raw.githubusercontent.com/KodeCell/Anime-Recommender/master/data/rating.csv*
