import pandas as pd
import requests
import time
from datetime import date
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import streamlit as st
import base64
import json
import pandas as pd
from pandas.io.json import json_normalize


today = date.today()



st.title('ContentCharts Web-Application')

sidebar_selection = st.sidebar.radio(
    'Select location data to display:',
    ['Show Global', 'Show U.S', 'Show U.K', 'Show other'],
)


sidebar_selection = st.sidebar.radio(
    'Select location data to display:',
    ['Show All', 'Show Apple Music', 'Show iTunes Store (Music)', 'Show App Store'],
)




# Apple Music (United States)
def get_data():
    Played_songs = 'https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json'
    Played_albums ='https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/albums.json'
    playedsongs = pd.read_json(Played_songs)
    playedalbums = pd.read_json(Played_albums)
    Played_playlists = 'https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/playlists.json'
    playedplaylists = pd.read_json(Played_playlists)
    Played_mvs = 'https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/music-videos.json'
    playedmvs = pd.read_json(Played_mvs)

    return playedsongs, playedalbums, playedplaylists, playedmvs

playedsongs, playedalbums, playedplaylists, playedmvs = get_data()

print("Apple Music Charts (Top 100)")
print("Top songs actively played " + str(playedsongs))
print("Top albums actively played " + str(playedalbums))
print("Top playlists actively played " + str(playedplaylists))
print("Top Music Videos actively played " + str(playedmvs))

st.header("Apple Music Charts (Top 100)")
st.subheader("**Top songs actively played** " + str(playedsongs))
st.subheader("**Top albums actively played** " + str(playedalbums))
st.subheader("**Top playlists actively played** " + str(playedplaylists))
st.subheader("**Top Music Videos actively played** " + str(playedmvs))


# iTunes Store Music (United States)
def get_data():
    Top_songs = 'https://itunes.apple.com/us/rss/topsongs/limit=100/explicit=true/json'
    topsongs = pd.read_json(Top_songs)
    Top_albums = 'https://itunes.apple.com/us/rss/topalbums/limit=100/explicit=true/json'
    topalbums = pd.read_json(Top_albums)
    Top_mvs = 'https://itunes.apple.com/us/rss/topmusicvideos/limit=100/explicit=true/json'
    topmvs = pd.read_json(Top_mvs)

    return topsongs, topalbums, topmvs

topsongs, topalbums, topmvs = get_data()
print("iTunes Store Music Charts (Top 100)")
print("Top songs actively purchased " + str(topsongs))
print("Top albums actively purchased " + str(topalbums))
print("Top Music Videos actively purchased " + str(topmvs))

st.header("iTunes Store Music Charts (Top 100)")
st.subheader("**Top songs actively purchased** " + str(topsongs))
st.subheader("**Top albums actively purchased** " + str(topalbums))
st.subheader("**Top Music Videos actively purchased** " + str(topmvs))

#App Store (United States)
# Top Free Apps
def get_data():
    Top_free = 'https://rss.applemarketingtools.com/api/v2/us/apps/top-free/50/apps.json'
    topfree = pd.read_json(Top_free)
    Top_paid = 'https://rss.applemarketingtools.com/api/v2/us/apps/top-paid/50/apps.json'
    toppaid = pd.read_json(Top_paid)

    return topfree, toppaid

topfree, toppaid = get_data()
print("App Store Charts (Top 100)")
print("Top free apps actively downloaded " + str(topfree))
print("Top paid apps actively purchased " + str(toppaid))

st.header("App Store Charts (Top 100)")
st.subheader("**Top free apps actively downloaded** " + str(topfree))
st.subheader("**Top paid apps actively purchased** " + str(toppaid))
