import media
import fresh_tomatoes

# media.py is imported to create class for all movies
# fresh_tomatoes is given to create a nice website


# Below are the movies I've selected, inputs are "Title","Description","Movie Poster","Trailer"
independence_day = media.Movie("Independence Day",
                               "The aliens are coming and their goal is to invade and destroy Earth. Fighting superior technology, mankind's best weapon is the will to survive.",
                               "https://upload.wikimedia.org/wikipedia/en/b/bb/Independence_day_movieposter.jpg",
                               "https://www.youtube.com/watch?v=kA2WzBi2grE")

ghost_in_the_shell = media.Movie("Ghost in the Shell",
                                 "A cyborg policewoman and her partner hunt a mysterious and powerful hacker called the Puppet Master.",
                                 "https://images.fandango.com/ImageRenderer/300/0/redesign/static/img/default_poster.png/0/images/masterrepository/Fandango/728/gits-400x600.jpg",
                                 "https://www.youtube.com/watch?v=p2MEaROKjaE")

hurt_locker = media.Movie("Hurt Locker",
                          "During the Iraq War, a Sergeant recently assigned to an army bomb squad is put at odds with his squad mates due to his maverick way of handling his work.",
                          "https://static.rogerebert.com/uploads/movie/movie_poster/the-hurt-locker-2009/large_uToiRjgTYfGrXnMNxpyiGZPgvM0.jpg",
                          "https://www.youtube.com/watch?v=JIgEhiUVKh8")
die_hard = media.Movie("Die Hard",
                       "John McClane, officer of the NYPD, tries to save his wife Holly Gennaro and several others that were taken hostage by German terrorist Hans Gruber during a Christmas party at the Nakatomi Plaza in Los Angeles.",
                       "https://upload.wikimedia.org/wikipedia/en/7/7e/Die_hard.jpg",
                       "https://www.youtube.com/watch?v=2TQ-pOvI6Xo")

heat = media.Movie("Heat",
                   "A group of professional bank robbers start to feel the heat from police when they unknowingly leave a clue at their latest heist, while both sides attempt to find balance between their personal and their professional lives.",
                   "https://upload.wikimedia.org/wikipedia/en/6/6c/Heatposter.jpg",
                   "https://www.youtube.com/watch?v=0xbBLJ1WGwQ")

boondock_saints = media.Movie("Boondock Saints",
                              "Fraternal twins set out to rid Boston of the evil men operating there while being tracked down by an FBI agent.",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BYzVmMTdjOTYtOTJkYS00ZTg2LWExNTgtNzA1N2Y0MDgwYWFhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY1200_CR82,0,630,1200_AL_.jpg",
                              "https://www.youtube.com/watch?v=VoRrQiORYck")

movies = [independence_day,ghost_in_the_shell,hurt_locker,die_hard,heat,boondock_saints]
fresh_tomatoes.open_movies_page(movies)

# Originally: fresh_tomatoes takes movie list as input, then extracts needed data to create a website called "Fresh Tomatoes Movie Trailers"
# After modifying:
"""Title and page name changed into "Mivvv's Movie List
When hovered over a movie, it displays description of the movie"""
