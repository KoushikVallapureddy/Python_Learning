from playable import Playable

class MediaPlayer:
    """
    Media player class that can work with any object implementing the Playable interface.
    """
    def __init__(self):
        self.current_media = None
    
    def set_media(self, media):
        if isinstance(media, Playable):
            self.current_media = media
        else:
            raise TypeError("Media must implement Playable interface")
    
    def play(self):
        if self.current_media is None:
            return "No media set"
        return self.current_media.play()
    
    def pause(self):
        if self.current_media is None:
            return "No media set"
        return self.current_media.pause()
    
    def stop(self):
        if self.current_media is None:
            return "No media set"
        return self.current_media.stop()