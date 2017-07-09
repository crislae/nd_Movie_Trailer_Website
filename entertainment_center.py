# -*- coding: cp1252 -*-
"""
    Title:	    "entertainment_center.py" Nanodegree project: Movie Trailer Website
    Author:         crislae @github
    Content:        Initialiates, with real examples of movies, the Media Data and it
                    creates the movie trailer website.
    Status:	    to be submitted and evaluated - nanodegree Full Stack Web Developer
    Created:	    01-Jul-2017
    Post-History:   09-Jul-2017
"""


import media
import fresh_tomatoes

# Variables for Rating of a video
G = "General Audiences, with all ages admitted"
PG = "Parental Guidance, as some material may not be suitable for children"
PG13 = "Parental Guidance-13, with parents strongly cautioned, as some material may not be suitable for children under 13"
R = "Restricted, with no one under 17 admitted without an accompanying parent or guardian"

# Movie type: Action, Adventure, Fantasy, Cartoons, Romance, Drama
ac = "Action"
ad = "Adventure"
f = "Fantasy"
c = "Cartoons"
r = "Romance"
d = "Drama"


# Create data structures - movies and tvshows
indianaJones1 = media.Movie ("Indiana Jones and the Raiders of the Lost Ark",
                            " 1h 55min",
                            "1981",
                            "Indiana Jones first movie",
                            "https://upload.wikimedia.org/wikipedia/en/4/4c/Raiders_of_the_Lost_Ark.jpg",
                            "https://www.youtube.com/watch?v=6b5RoI-jeGI",
                            PG,
                            ac+" "+ad+" "+f,
                            "Filming Locations: Yuma, Arizona, USA...")


indianaJones2 = media.Movie ("Indiana Jones and the Temple of Doom",
                            "1h 58min",
                            "1984",
                            "Indiana Jones second movie",
                            "https://upload.wikimedia.org/wikipedia/en/1/10/Indiana_Jones_and_the_Temple_of_Doom_PosterB.jpg",
                            "https://www.youtube.com/watch?v=HOwWfns4qqw",
                            PG,
                            ac+" "+ad+" "+f,
                            "Filming Locations: University of the Pacific, Stockton, California, USA")

indianaJones3 = media.Movie ("Indiana Jones and the Last Crusade",
                            "2h 7min",
                            "1989",
                            "Indiana Jones third movie",
                            "https://upload.wikimedia.org/wikipedia/en/f/fc/Indiana_Jones_and_the_Last_Crusade_A.jpg",
                            "https://www.youtube.com/watch?v=0ZOcoxjeUYo",
                            PG,
                            ac+" "+ad+" "+f,
                            "Filming Locations: Palazzi Barbaro, Grand Canal, Venice, Veneto, Italy...")

lion_king = media.Movie ("The Lion King",
                        "1h 28min",
                        "1994",
                        "The Lion King tells the story of Simba, a young lion who is to succeed his father, Mufasa, as King of the Pride Lands",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                        "https://www.youtube.com/watch?v=4sj1MT05lAA",
                        G,
                        c,
                        "")
                         
aladdin = media.Movie("Aladdin",
                    "1h 30min",
                    "1992",
                    "The adventures of Aladdin, a poor street thief who spends his time stealing food from the marketplace in the city of Agrabah.",
                    "https://upload.wikimedia.org/wikipedia/en/3/3e/AatKoT2.jpg",
                    "https://www.youtube.com/watch?v=gWLa6y7Z2TE",
                    G,
                    c,
                    "")

beauty_and_the_beast = media.Movie("Beauty and the Beast",
                                   "1h 24min",
                                   "1991",
                                   "The Disney story about a beauty and a beast, animated and musical. The film is based on the fairy tale La Belle et la Bete...",
                                   "https://upload.wikimedia.org/wikipedia/en/7/7c/Beautybeastposter.jpg",
                                   "hhttps://www.youtube.com/watch?v=tRlzmyveDHE",
                                   G,
                                   c,
                                   "")

the_goonies = media.Movie("The Goonies",
                          "1h 54min",
                          "1985",
                          "A group of kids set out on an adventure in search of pirate treasure...",
                          "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Goonies.jpg",
                          "https://www.youtube.com/watch?v=hJ2j4oWdQtU",
                          G,
                          ac+" "+ad,
                          "")

princess_bride = media.Movie("The Princess Bride",
                          "1h 38min",
                          "1987",
                          "Story about a farmhand named Westley who must rescue his true love Princess Buttercup from the odious Prince Humperdinck.",
                          "https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",
                          "https://www.youtube.com/watch?v=WNNUcHRiPS8",
                          G,
                          ac+" "+ad,
                          "")

back_to_the_future = media.Movie("Back to the Future ",
                          "1h 56min",
                          "1985",
                          "Marty McFly is accidentally sent 30 years into the past in a time-traveling DeLorean invented by the scientist Doc Brown",
                          "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
                          "https://www.youtube.com/watch?v=2LnShmQ_hLc",
                          G,
                          ac+" "+ad,
                          "")

gamesofthroess01e01 = media.TvShow("Game of Thrones, S01E01: Winter Is Coming ",
                                   "56min",
                                   "2011-",
                                   01,
                                   01,
                                   "HBO",
                                   PG13,
                                   "The series is based on A Game of Thrones, the first novel in the A Song of Ice and Fire series by George R. R. Martin",
                                   "https://upload.wikimedia.org/wikipedia/en/e/e8/Game_of_Thrones_Season_1.jpg",
                                   "https://www.youtube.com/watch?v=JjfBu2RZFHI",
                                   ad)

gamesofthroess01e02 = media.TvShow("Game of Thrones, S01E02: The Kingsroad ",
                                   "56min",
                                   "2011-",
                                   01,
                                   01,
                                   "HBO",
                                   PG13,
                                   "The series is based on A Game of Thrones, the first novel in the A Song of Ice and Fire series by George R. R. Martin",
                                   "https://upload.wikimedia.org/wikipedia/en/e/e8/Game_of_Thrones_Season_1.jpg",
                                   "https://www.youtube.com/watch?v=kPrW3Swrp4E",
                                   ad)

gamesofthroess01e03 = media.TvShow("Game of Thrones, S01E03: Lord Snow ",
                                   "56min",
                                   "2011-",
                                   01,
                                   01,
                                   "HBO",
                                   PG13,
                                   "The series is based on A Game of Thrones, the first novel in the A Song of Ice and Fire series by George R. R. Martin",
                                   "https://upload.wikimedia.org/wikipedia/en/e/e8/Game_of_Thrones_Season_1.jpg",
                                   "https://www.youtube.com/watch?v=68KrOZgmXZw",
                                   ad)


# array with the all the movies. The are going to be shown, 3 per line. 
movies = [
        indianaJones1, indianaJones2, indianaJones3,
        lion_king, aladdin, beauty_and_the_beast,
        the_goonies, princess_bride, back_to_the_future,
        gamesofthroess01e01, gamesofthroess01e02, gamesofthroess01e03
        ]

# creates the website with all the movies
fresh_tomatoes.open_movies_page(movies)

print("Website created")
print("© 2017 crislae ")


#print(media.Movie.__doc__)
#print(media.Video.__doc__)






















