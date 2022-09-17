import subprocess
# Spleeter
# 2 Stems- Vocals and other accompaniments separation
# 4 Stems- Vocals, drums, bass and other separation
# 5 Stems- Vocals, drums, bass, piano and other separation

def song_separator(song_path) -> tuple:
    #subprocess.call(['spleeter' , 'separate' , song_path, '-o' , 'audio_output'])
    song_name = song_path.split("/")[-1].replace('.mp3','')
    vocals_path = f'/home/skawy/side_projects/music-mixer/audio_output/{song_name}/vocals.wav'
    instruments_path = f'/home/skawy/side_projects/music-mixer/audio_output/{song_name}/audio_output/runaway/accompaniment.wav'
    return(vocals_path , instruments_path)

