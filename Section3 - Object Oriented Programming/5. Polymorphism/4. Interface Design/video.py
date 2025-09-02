# TODO: Import the abstract base classes from playable.py
from playable import Playable, MediaInfo

class Video(Playable, MediaInfo):
    """
    Concrete implementation of a Video that implements both Playable and MediaInfo interfaces.
    """
    def __init__(self, title, resolution, duration):
        self.title = title
        self.resolution = resolution
        self.duration = duration
    
    def play(self):
        return f"Playing video: {self.title}"
    
    def pause(self):
        return f"Paused video: {self.title}"
    
    def stop(self):
        return f"Stopped video: {self.title}"
    
    def get_title(self):
        return self.title
    
    def get_duration(self):
        return self.duration
    
    def get_info(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"Video: {self.title} ({self.resolution}) ({minutes}:{seconds:02d})"