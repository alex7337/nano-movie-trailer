class Movies:
    """
    Stores movie title, youtube trailer url and poster image url
    """
    def __init__(self, title, trailer_youtube_url, poster_image_url):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
