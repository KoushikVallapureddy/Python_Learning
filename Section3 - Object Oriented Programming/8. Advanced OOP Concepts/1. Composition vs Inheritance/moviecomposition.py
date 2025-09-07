from mediaitem import MediaItem

class MovieComposition:
    def __init__(self, title, director, year):
        self.media = MediaItem(title, director, year)
    
    def display_info(self):
        return f"Movie: {self.media.title} directed by {self.media.creator} ({self.media.year})"