# TODO: Import the Media class from media.py
from media import Media

class Book(Media):
    def display_info(self):
        return f"Book: {self.title} by {self.creator} ({self.year})"