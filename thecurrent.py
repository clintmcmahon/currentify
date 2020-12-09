# encoding: utf-8

import sys
import pytz
import datetime
from datetime import timedelta
from spotify import Spotify
from playlist import Playlist
import json
import requests
from bs4 import BeautifulSoup

def get_tracks(startdate, enddate):
    '''
    Takes the playlist uri and returns the tracks played
    '''
    tracks = []
    base_uri = 'https://www.thecurrent.org/playlist'
    
    thisdate = startdate
    while startdate <= thisdate <= enddate:
        year = str(thisdate.year)
        month = '{:02d}'.format(thisdate.month)
        day = '{:02d}'.format(thisdate.day)
        hour = str(thisdate.hour)
        uri = base_uri + '/' + year + '-' + month + '-' + day + '/' + hour
        print(uri)
        r = requests.get(uri)
        if r.status_code == 200:
            playlist_html = r.text
            soup = BeautifulSoup(playlist_html, 'html.parser')
            soup = BeautifulSoup(soup.prettify(), 'html.parser')
            content = soup.find('section', {'class': 'content'})
            playlist_rows = content.find_all('article', {'class': 'song'})

            for playlist_row in playlist_rows:
                artist = playlist_row.find('h5', attrs={'class': 'artist'})
                song = playlist_row.find('h5', attrs={'class': 'title'})
                airdate = playlist_row.find('time')
                if artist and song:
                    #print(artist.text.strip().replace("'", ''))
                    tracks.append({'artist': artist.text.strip().replace("'", ''),
                               'song': song.text.strip().replace("'", '').replace(',',''),
                              'airdate': airdate.text.strip()})
        thisdate = thisdate + timedelta(hours=1)
    return tracks
    
def main(args):
    '''
    Main method
    '''
    if len(args) < 4:
        print ("Please provide the necessary parameters ie thecurrent.py [playlist_name] [start_date] [end_date] [playlist_description]")
    else:
        #The name of the playlist you want to use in Spotify
        #If this playlist does not exist a new one with this name will be created
        #If this playlist exists it will be used
        playlist_name = args[0]
        
        #The start date time of the tracks you want to return. 
        #Example: 2019-02-15T02:00:00
        start_date = args[1]

        #The end date time of the tracks you want to return. 
        #Example: 2019-02-15T05:00:00
        end_date = args[2]

        #The description of the playlist you want to appear in Spotify
        playlist_description = args[3]

        #Create new Playlist object
        #Set this particular playlist properties
        #Send the playlist object into Spotify to create/update the latest
        playlist = Playlist()
        spotify = Spotify()
        playlist.name =  playlist_name
        playlist.description = playlist_description

        start = datetime.datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
        end = datetime.datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')   

        playlist.tracks = get_tracks(start, end)
        playlist.tracks.sort(key=extract_time, reverse=False)
        spotify.create_playlist(playlist)

def extract_time(json):
    try:
        return json['airdate']
    except KeyError:
        return 0

if __name__ == '__main__':
     main(sys.argv[1:])