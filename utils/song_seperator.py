# Spleeter
# 2 Stems- Vocals and other accompaniments separation
# 4 Stems- Vocals, drums, bass and other separation
# 5 Stems- Vocals, drums, bass, piano and other separation

from pydub import AudioSegment

sound = AudioSegment.from_wav("output/filename/vocals.wav")
sound.export("output/filename/vocals.mp3", format="mp3")