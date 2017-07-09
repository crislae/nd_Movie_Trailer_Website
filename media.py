# -*- coding: cp1252 -*-

"""
    Title:	    Media.py - Nanodegree project: Movie Trailer Website
    Content:        Defines the data structures in order to store movies, including
                    among others movie title, poster URL and a YouTube link to the
                    movie trailer.   
    Author:         crislae @github
    Status:	    to be submitted and evaluated - nanodegree Full Stack
                    Web Developer
    Created:	    01-Jul-2017
    Post-History:   09-Jul-2017
"""

import webbrowser

class Video:
    """ Defines the parent class Video. It creates a data structure to store
        movies, including among others movie title, poster URL and a YouTube
        link to the movie trailer. 

    Attributes:
        - title (str):                  Indicates the title of the video        
        - duration (str):               Indicates the duration of the video xh xxmin        
        - year (str):                   Year it aired        
        - rating of a Video (str): 
            - G:                        General Audiences, with all ages admitted.            
            - PG:                       Parental Guidance, as some material may not
                                        be suitable for children.                                        
            - PG-13:                    Parental Guidance-13, with parents strongly
                                        cautioned, as some material may not be suitable
                                        for children under 13.                                         
            - R:                        Restricted, with no one under 17 admitted
                                        without an accompanying parent or guardian.                                         
        - video type (str):             Use either: Action, Adventure, Fantasy, Cartoons,
                                        Romance, Drama.                                         
        - storyline (str):              Indicates what a movie is about.        
        - poster_image_url (str):       It is the url of the image to be used as "poster
                                        of the movie".                                         
        - trailer_youtube_url (str):    It is the url where the trailer of the movie
                                        is located in youtube.        
    Methods:
        set_rating:                     Set function to access the attributes.
        show_info:                      Shows info of the video like title and duration.
        show_video:                     Opens the video in a browser.
     """  

    #Constructor
    def __init__(self, title, duration, year, rating, video_type,
                 storyline, poster_image_url, trailer_youtube_url):
        
                self.title = title  # Tittle of the video
                self.duration  = duration  # duration of the video in hours and minutes
                self.year = year  # year it aired
                self.rating = rating  # Rating of the video: G, PG, PG13, R
                self.video_type = video_type  
                self.storyline = storyline
                self.poster_image_url = poster_image_url
                self.trailer_youtube_url = trailer_youtube_url  

    #Class methods
       
    def set_rating(self, rating):
        """ sets a new rating """
        self.rating = rating        
  
    def show_info(self):
        """ It shows information like tittle and duration of the video.
        Purpuose testing """
        print(self.Title+" "+self.Duration)

    def show_video(self):
        """ It opens the video in the browser """
        webbrowser.open(self.trailer_youtube_url)

    
class Movie(Video):
    """ Inherits from class Video. Defines the class Movie. Creates any kind of movie.
        Attributes:
        - didyouknow (str): Trivia facts of the movie, like famous quotes or location
    """   

    #Constructor
    def __init__(self, title, duration, year, storyline, poster_image_url,
                 trailer_youtube_url, rating, video_type, didyouknow):
        
                 Video.__init__(self, title, duration, year,rating, video_type,
                                storyline, poster_image_url,trailer_youtube_url)
                 self.didyouknow = didyouknow

    #Class methods                 
    def show_didyouknow(self):
        """ Prints didyouknow factors of the movie """
        print(self.didyouknow)



class TvShow(Video):
    """ Inherits from class Video. Creates TV Show videos, like series... 
        Attributes:
        - season (str):     season number where the episode appers
        - episode (str):    episode inside the season
        - tv_station (str): tv station it aired or airs. 
    """
                 
    def __init__(self, title, duration, year, season, episode, tv_station, rating,
                 storyline, poster_image_url, trailer_youtube_url, video_type):
        
                Video.__init__(self, title, duration, year,rating, video_type,
                               storyline, poster_image_url,trailer_youtube_url)
                self.season = season
                self.episode = episode
                self.tv_station = tv_station






        
    
