# encoding = utf-8

"""
This file contains three different class that abstracts a movie object.
These class comprise an inherent relationship from object oriented programming.
"""

__author__ = "Gustavo Nobrega"
__license__ = "GPL"
__version__ = "1.0"
__release__ = "1.0.1"
__maintainer__ = "Gustavo Nobrega"
__email__ = "gustavonobrega@gmail.com"
__status__ = "Production"


class Video():

    def __init__(self, title, duration):
        print("Video Constructor Called")
        self.title = title
        self.duration = duration

    def __str__(self):
        print("Object Information: \nTitle: " + str(self.title) +
              "\nDuration:" + str(self.duration))


class Movie(Video):

    def __init__(self, title, duration, movie_description, movie_banner,
                 movie_url_youtube_video):
        print("Movie Constructor Called")
        Video.__init__(self, title, duration)
        self.movie_description = movie_description
        self.poster_image_url = movie_banner
        self.trailer_youtube_url = movie_url_youtube_video

    def __str__(self):
        print("Object Information: \nTitle: " + str(self.title) +
              "\nDuration:" + str(self.duration) +
              "\nDescription: " + str(self.movie_description))


class Tv_Station(Video):

    def __init__(self, title, duration, season, episode, tv_station):
        Video.__init__(self, title, duration)
        print("Tv_Station Constructor Called")
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def __str__(self):
        print("Object Information: \nTitle: " + str(self.title) +
              "\nDuration:" + str(self.duration) +
              "\nSeason: " + str(self.season) +
              "\nEpisode: " + str(self.episode))
