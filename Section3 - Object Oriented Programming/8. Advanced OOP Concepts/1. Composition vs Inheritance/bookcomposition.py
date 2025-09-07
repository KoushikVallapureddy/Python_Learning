# TODO: Import the MediaItem class from mediaitem.py
from mediaitem import MediaItem

class BookComposition:
    def __init__(self, title, author, year):
        self.media = MediaItem(title, author, year)
    
    def display_info(self):
        return f"Book: {self.media.title} by {self.media.creator} ({self.media.year})"