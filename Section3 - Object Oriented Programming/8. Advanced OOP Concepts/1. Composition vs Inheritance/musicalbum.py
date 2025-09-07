# TODO: Import the Media class from media.py
from media import Media

class MusicAlbum(Media):
    # TODO: No need to implement __init__ as it will use the parent class constructor
    
    def display_info(self):
        return f"Music Album: {self.title} by {self.creator} ({self.year})"