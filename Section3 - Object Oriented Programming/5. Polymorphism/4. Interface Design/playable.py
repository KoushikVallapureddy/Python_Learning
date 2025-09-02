from abc import ABC, abstractmethod

class Playable(ABC):
    """
    Abstract base class defining the interface for playable media objects.
    All playable media must implement play, pause, and stop functionality.
    """
    @abstractmethod
    def play(self):
        """Return a string in format: 'Playing [media type]: [title]'"""
        raise NotImplementedError
    
    @abstractmethod
    def pause(self):
        """Return a string in format: 'Paused [media type]: [title]'"""
        raise NotImplementedError
    
    @abstractmethod
    def stop(self):
        """Return a string in format: 'Stopped [media type]: [title]'"""
        raise NotImplementedError

class MediaInfo(ABC):
    """
    Abstract base class defining the interface for media information.
    All media objects must implement methods to retrieve title, duration, and formatted info.
    """
    @abstractmethod
    def get_title(self):
        """Return the title of the media"""
        raise NotImplementedError
    
    @abstractmethod
    def get_duration(self):
        """Return the duration of the media in seconds"""
        raise NotImplementedError
    
    @abstractmethod
    def get_info(self):
        """
        Return formatted information about the media.
        For Song: "Song: [title] by [artist] ([minutes]:[seconds])"
        For Video: "Video: [title] ([resolution]) ([minutes]:[seconds])"
        """
        raise NotImplementedError