from pydub import AudioSegment

def mix(sound1_path , sound2_path) -> None:
    sound1 = AudioSegment.from_file(sound1_path)
    sound2 = AudioSegment.from_file(sound2_path)

    combined = sound1.overlay(sound2) if len(sound1) > len(sound2) else sound2.overlay(sound1)

    combined.export("/home/skawy/side_projects/music-mixer/audio_output/song1/combined.wav", format='wav')
