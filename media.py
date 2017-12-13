"""
favorite movies
"""
import webbrowser
import fresh_tomatoes

class Movie:
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self._title = title
        self._storyline = storyline
        self._poster_image_url = poster_image_url
        self._trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self._trailer_youtube_url)

def main():
    """
    Test Function
    """
    movies = []
    moana = Movie("Moana",
                  "Nice movie about a girl and a demi-god",
                  "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
                  "https://www.youtube.com/watch?v=cPAbx5kgCJo")

    sing = Movie("Sing",
                  "A movie with singing animals",
                  "https://upload.wikimedia.org/wikipedia/en/b/bb/Sing_%282016_film%29_poster.jpg",
                  "https://www.youtube.com/watch?v=OrWjjOOYxhI")

    kubo = Movie("Kubo and The Two Strings",
                  "A movie about a boy, a monkey, and a beetle",
                  "https://upload.wikimedia.org/wikipedia/en/c/c4/Kubo_and_the_Two_Strings_poster.png",
                  "https://www.youtube.com/watch?v=p4-6qJzeb3A")

    #moana.show_trailer()
    movies.append(moana)
    movies.append(sing)
    movies.append(kubo)

    # Test it
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
    exit(0)