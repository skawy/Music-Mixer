from abc import ABC, abstractmethod

class Abstract_Song(ABC):
    @abstractmethod
    def get_mixes(self) -> None:
        pass


class Concrete_Song(Abstract_Song):
    def get_mixes(self) -> str:
        return "Empty Song"  

class Abstract_Song_Decorator(Abstract_Song):
    def __init__(self,decorated_song) -> None:
        self.decorated_song = decorated_song
    def get_mixes(self) -> None:
        return self.decorated_song.get_mixes()

class Vocals(Abstract_Song_Decorator):
   
   def __init__(self,decorated_song) -> None:
      Abstract_Song_Decorator.__init__(self,decorated_song)
   
   def get_mixes(self) -> str:
	   return self.decorated_song.get_mixes() + ', Vocals'

class Instruments(Abstract_Song_Decorator):
   
   def __init__(self,decorated_song) -> None:
      Abstract_Song_Decorator.__init__(self,decorated_song)
   
   def get_mixes(self) -> str:
	   return self.decorated_song.get_mixes() + ', Instruments'

