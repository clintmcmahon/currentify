# Currentify

Currentify is a Python library that takes parses playlists from 89.3 The Current (https://thecurrent.org) and turns them into a Spotify playlist. 

### Prerequisites

Python3 (Python2 will require a couple code changes)

[Spotify account](https://www.spotify.com/us/signup/)

[Spotify API Credentials](https://developer.spotify.com/my-applications/#!/)

BeautifulSoup
```
pip3 install beautifulsoup4
```

Spotipy
```
pip3 install spotipy
```

Requests
```
pip3 install requests
```

### Installing

Clone this repository

```
git clone https://github.com/clintmcmahon/currentify
```

Change directory to currentify

```
cd currentify
```

Create a local_config.py file and populate with your values. Your file should look like this

```
#!/usr/bin/env python
#encoding: utf-8

SPOTIFY_USERNAME = [your Spotify username]
SPOTIFY_CLIENT_SECRET = [your Spotify API Client Secret]
SPOTIFY_CLIENT_ID = [your Spotify API Client ID]
SPOTIFY_SCOPE = 'playlist-modify-public playlist-modify-private playlist-read-collaborative'
SPOTIFY_REDIRECT_URI = 'http://localhost'
```

Run the code
```
python3 main.py [playlist_name, start_date, end_date, playlist_description]
```
A browser window will automatically open where you will authenticate with Spotify. After you've given access to your Spotify account the browser will redirect to a http://localhost url. Copy the localhost url and paste it into the command line. You'll only need to do this once, the code will create a cache authentication file on your local machine.

After you've authenticated the program will read playlist and either create a new playlist or delete the contents of the existing playlist before adding the latest tracks from the website.

## Built With

* [Spotify](http://www.spotify.com)
* [89.3 The Current](http://thecurrent.org)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [Spotipy](https://github.com/plamere/spotipy)

## Acknowledgments

* 89.3 The Current - [Keep Good Music Free - Donate today!](https://contribute.publicradio.org/contribute.php)
