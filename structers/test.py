import mixer

my_song = mixer.Concrete_Song()

print(my_song.get_mixes())

my_song = mixer.Vocals(my_song)

print(my_song.get_mixes())

my_song = mixer.Instruments(my_song)

print(my_song.get_mixes())