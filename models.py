import requests
from bs4 import BeautifulSoup
import os
import re


HOME_FOLDER = os.path.dirname(os.path.realpath(__file__))

def create_filename(artist,lyric):
    artist_str = artist.replace(" ", "_").replace("'","_").lower()
    lyric_str = lyric.replace(" ", "_").replace("'","_").lower()
    filename = artist_str + "-" + lyric_str
    return filename



class Song:

    def __init__(self,artist,lyric):
        self.artist = artist
        self.lyric = lyric
    
    def search_in_repo(self):
        filename = create_filename(self.artist,self.lyric)
        filelist = os.listdir(HOME_FOLDER)

        if filename + ".txt" in filelist:
            print("Already searched!")
            return True
            
        return False



class Search(Song):

    def __init__(self, artist, lyric, provider=["azlyrics","elyrics"], saveflag=False):
        super().__init__(artist, lyric)
        self.provider = provider
        self.saveflag = saveflag

    def connection(self):
        url = self.get_url()
        try:
            response = requests.get(url, timeout=3)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def lyric(self):
        lyric = self.get_lyric()
        return lyric

    def save(self):
        filename = create_filename(self.artist,self.lyric)
        f = open(filename + '.txt', 'w')
        text = self.get_lyric()
        f.write("\n".join(text).strip())
        return None



class Azlyrics(Search):

    def get_url(self):
        artist = str(self.artist).lower().replace(" ", "").replace("'", "")
        lyric = str(self.lyric).lower().replace(" ", "").replace("'", "")
        url = 'http://azlyrics.com/lyrics/'+artist+'/'+lyric +'.html'
        return url

    def get_lyric(self):
        try:
            response = self.connection()
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.find_all("div", attrs={"class": None, "id": None})
            text = [x.getText() for x in text]
            self.text = text
            return text
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
    


class Elyrics(Search):

    def get_url(self):
        artist = str(self.artist).lower().replace(" ", "-").replace("'","_")
        lyric = str(self.lyric).lower().replace(" ", "-").replace("'","_")
        url = 'http://elyrics.net/read/r/'+artist+'/'+lyric +'-lyrics.html'
        return url

    def get_lyric(self):
        response = self.connection()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.find_all("div", attrs={"id": "inlyr"})
        text = [x.getText()for x in text]
        self.text = text
        return text
