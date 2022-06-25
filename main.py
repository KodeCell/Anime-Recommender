import pandas as pd
import streamlit as st
import pandas as pd
import preprocessing
import recommendations
import animeDetails
st.set_page_config(layout="wide")

# getting the dataset and cleaning it
anime = pd.read_csv('data/anime.csv')
anime = preprocessing.preprocessed(anime)
anime_list = anime['name'].values

vectors = recommendations.distances(anime)
similarity = recommendations.similarity(vectors)


def recommend(name):
    names,posters,types,episodes,statuses,genres,mal_link,summary = ([] for i in range(8))

    movie_index = anime[anime['name'] == name].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    indexes = distances[1:7]
    for i in indexes:
        a = anime.iloc[i[0]]['name']
        names.append(a.title())
        anime_id = anime.iloc[i[0]]['anime_id']
        poster,type,episode,status,genre,mal_links,summaries = animeDetails.get_anime_data(anime_id)
        posters.append(poster)
        types.append(type)
        episodes.append(episode)
        statuses.append(status)
        genres.append(genre)
        mal_link.append(mal_links)
        summary.append(summaries)

    return names, posters, types, episodes, statuses, genres, mal_link, summary




st.title('Anime Recommender')

anime_selected = st.selectbox('Name of the anime',anime_list)

if st.button('Recommend'):
    anime_name,poster,type,episodes,status,genres,mal_links,anime_summary = recommend(anime_selected)

    i = 0
    while i<5:

        col1,col2,col3 = st.columns([2,2,8])
        with col1:
            st.image(poster[i])
        with col2:
            st.write(f'[{anime_name[i]}]({mal_links[i]})')
            st.markdown(f'**Name : {anime_name[i]}**')
            st.markdown(f'**Episodes : {episodes[i]}**')
            st.markdown(f'**Status : {status[i]}**')
            st.markdown(f'**Genre : {genres[i]}**')
        with col3:
            st.markdown(f'**Summary** : {anime_summary[i]}')


        i= i+1
