from mediaitem import MediaItem

class MusicAlbumComposition:
    def __init__(self, title, artist, year):
        self.media = MediaItem(title, artist, year)
    
    def display_info(self):
        return f"Music Album: {self.media.title} by {self.media.creator} ({self.media.year})"