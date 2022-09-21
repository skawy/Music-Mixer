from abc import ABC, abstractmethod
from typing_extensions import Self
from pydub import AudioSegment

class Abstract_Song(ABC):
    @abstractmethod
    def get_mixes(self) -> None:
        pass
    def get_names(self):
        pass

class Concrete_Song(Abstract_Song):
    audio_path = '/home/skawy/side_projects/music-mixer/empty.wav'
    def get_mixes(self) -> AudioSegment:
        return  AudioSegment.from_file(self.audio_path)
    def get_names(self) -> str:
        return ""

class Abstract_Song_Decorator(Abstract_Song):
    def __init__(self,decorated_song,song_name) -> None:
        self.song_name =  song_name
        self.decorated_song = decorated_song
    def get_mixes(self) -> AudioSegment:
        return self.decorated_song.get_mixes()
    def get_names(self) -> str:
       return self.decorated_song.get_names()

class Vocals(Abstract_Song_Decorator):
   
   def __init__(self,decorated_song, song_name) -> None:
      Abstract_Song_Decorator.__init__(self,decorated_song , song_name)  # type: ignore
   
   def get_mixes(self) -> AudioSegment:
      wrapped_audio =  AudioSegment.from_file(f'/home/skawy/side_projects/music-mixer/audio_output/{self.song_name}/vocals.wav')
      if len(self.decorated_song.get_mixes()) > len(wrapped_audio):
        return self.decorated_song.get_mixes().overlay(wrapped_audio) 
      else:
        return wrapped_audio.overlay(self.decorated_song.get_mixes()) 

   def get_names(self) -> str:
       return self.decorated_song.get_names() + f'-{self.song_name}_vocals'

class Instruments(Abstract_Song_Decorator):
   
   def __init__(self,decorated_song,song_name) -> None:
      Abstract_Song_Decorator.__init__(self,decorated_song , song_name)  # type: ignore

   def get_mixes(self) -> AudioSegment:
      wrapped_audio =  AudioSegment.from_file(f'/home/skawy/side_projects/music-mixer/audio_output/{self.song_name}/accompaniment.wav')
      if len(self.decorated_song.get_mixes()) > len(wrapped_audio):
        return self.decorated_song.get_mixes().overlay(wrapped_audio) 
      else:
        return wrapped_audio.overlay(self.decorated_song.get_mixes()) 

   def get_names(self) -> str:
      return self.decorated_song.get_names() + f'-{self.song_name}_Instruments'

