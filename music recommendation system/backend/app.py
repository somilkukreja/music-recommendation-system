import streamlit as st  
import pickle

df=pickle.load(open('models/songs_df.pkl','rb'))
similarity=pickle.load(open('models/similarity.pkl','rb'))

st.title('Music Recommendation System')

user_input=st.text_input('Enter a song name')

def recommended(song):
    song = song.lower() # 4 spaces in
    
    try:
        # 8 spaces in (because it's inside 'try')
        index = df[df['song_name'].str.lower() == song].index[0]
    except:
        # 8 spaces in (because it's inside 'except')
        return []

    # These are all 4 spaces in
    distances = similarity[index]
    song_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    rec=[]
    for i in song_list:
        rec.append({
            'song_name': df.iloc[i[0]]['song_name'],
            'artist': df.iloc[i[0]]['artist'],
            'link': df.iloc[i[0]]['link'],
            'thumbnail': df.iloc[i[0]]['thumbnail'] if 'thumbnail' in df.columns else None
        })
    return rec


if st.button('Recommend'):
    try:
        recommendations = recommended(user_input)
        if not recommendations:
            st.write('No recommendations found. Please check the song name and try again.')
        else:
            st.subheader('Recommended Songs:')
            for rec in recommendations:
                col1, col2=st.columns([1,3])
                with col1:
                    if rec['thumbnail']:
                        st.image(rec['thumbnail']) 
                with col2:
                    st.write('**song**: ' + rec['song_name'])
                    st.write('**artist**: ' + rec['artist'])
                    if rec['link']:
                        st.markdown(f"[▶ **Watch on YouTube**]({rec['link']})")

    except:
        st.error('No recommendations found. Please check the song name and try again.')
        st.stop()


st.subheader('recommended songs:')
results = recommended(user_input)

for item in results:
    col1, col2=st.columns([1,3])    
    with col1:
        if item['thumbnail']:
            st.image(item['thumbnail'])
    with col2:
        st.write('**' + item['song_name']+'**')
        st.write(item['artist'])
        if item['link']:
            st.markdown(f"[▶ Watch on YouTube]({item['link']})")