import webbrowser

class Movie():
    # Movie class to store data of per movie
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """This function initializes the Movie class
        for per movie

        Args:
            movie_title => Holds title of movie
            movie_storyline => Holds description of movie
            poster_image => Holds the link of movies poster
            trailer_youtube => holds the youtube link of trailer of movie

        Returns:
            initialized input as a class"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Function to show a movie trailer on browser
    def show_trailer(self):
        #Shows trailer of movie from the given input in ___init____
        webbrowser.open(self.trailer_youtube_url)
