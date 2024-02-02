import json
import streamlit as st

# Load JSON data
with open('movies.json') as f:
    movies_data = json.load(f)

# Streamlit app
st.title('Movie Information')

for movie in movies_data:
    container = st.container()

    poster = movie.get('Poster')
    if poster:
        container.image(poster, caption='Movie Poster', use_column_width=True)

    title = movie.get('Title')
    container.header(title)

    for attribute in ['Year', 'Rated', 'Released', 'Runtime', 'Director', 'Writer', 'Plot', 'Actors', 'Language', 'Country']:
        attribute_value = movie.get(attribute)
        container.write(f"{attribute}: {attribute_value}")
