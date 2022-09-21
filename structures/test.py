import mixer

my_song = mixer.Concrete_Song()

my_song = mixer.Vocals(my_song,'runaway')

my_song = mixer.Instruments(my_song,'pill')

print(my_song)

my_song.get_mixes().export("/home/skawy/side_projects/music-mixer/saved/combined.wav", format='wav')
print(my_song.get_names())