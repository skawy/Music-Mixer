from genericpath import isdir
import PySimpleGUI as sg
import pygame

import sys
from pathlib import Path

from pydub import AudioSegment
import structures.mixer as mixer
from utils.song_separator import song_separator

sys.path.append("/home/skawy/side_projects/music-mixer/structures")
sys.path.append("/home/skawy/side_projects/music-mixer/utils")

def gui():
    audio_player_column = [
        # [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-SOUND_PATH-")],
        [sg.Text(size=(12, 1), key='-STATUS-')],
        [
            sg.Button('Play', pad=(10, 0), key="-PLAY-"),
            sg.Button('Pause', pad=(10, 0), key="-PAUSE-"),
            sg.Button('Stop', pad=(10, 0), key="-STOP-"),
            sg.Button('Save', pad=(20, 0), key="-SAVE-" , button_color = 'green'),
        ],
        [sg.Slider(range=(0,100), orientation='h', size=(40, 20), enable_events=True, key="-VOLUME-", default_value=100)],
        [sg.Text(size=(50, 3), key='-SONG-')]
    ]

    audio_separator_column = [
        [sg.Text("Choose a Song To Separate: "), sg.Input( enable_events= True , key = "-SEPARATE-"), sg.FileBrowse()],
        
        [sg.Text("You can add Vocals or instruments of chosen file your current music ")],

        [
            sg.Button('Add Vocals', pad=(10, 0), key="-VOCALS-"),
            sg.Button('Add Instruments', pad=(10, 0), key="-INSTRUMENTS-"),
        ],
    ]

    layout = [
        [
            sg.Column(audio_player_column),
            sg.VSeparator(),
            sg.Column(audio_separator_column),

        ]
    ]

    audio_player_window=sg.Window('Music Mixer', layout, finalize=True)

    pygame.init()
    pygame.mixer.init()
    is_paused = False

    empty_song = AudioSegment.silent(duration=10000)

    empty_song.export("/home/skawy/side_projects/music-mixer/empty.wav", format='wav')

    sound_path = '/home/skawy/side_projects/music-mixer/empty.wav'

    my_song = mixer.Concrete_Song()

    while True:

        event, values = audio_player_window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            break
        
        song = pygame.mixer.Sound(sound_path)
        # song_length = song.get_length()
        song_channel = pygame.mixer.Channel(2)

        separated_song_path = values["-SEPARATE-"]

        if event == '-SEPARATE-':
            separated_song_path = values["-SEPARATE-"]
            song_name = separated_song_path.split("/")[-1].replace('.mp3','')
            if Path(f'/home/skawy/side_projects/music-mixer/audio_output/{song_name}').is_dir():
                print("Already Separated")
                continue
            song_separator(separated_song_path)

        match event:
            case '-VOCALS-':
                if separated_song_path == "":
                    print("Choose File To Separate")
                    continue
                
                song_name = separated_song_path.split("/")[-1].replace('.mp3','')
                my_song = mixer.Vocals(my_song,song_name)
                my_song.get_mixes().export("/home/skawy/side_projects/music-mixer/combined.wav", format='wav')
                sound_path = "/home/skawy/side_projects/music-mixer/combined.wav"
                song_channel.stop()


            case '-INSTRUMENTS-':
                if separated_song_path == "":
                    print("Choose File To Separate")
                    continue
                song_name = separated_song_path.split("/")[-1].replace('.mp3','')
                my_song = mixer.Instruments(my_song,song_name)
                my_song.get_mixes().export("/home/skawy/side_projects/music-mixer/combined.wav", format='wav')
                sound_path = "/home/skawy/side_projects/music-mixer/combined.wav"
                song_channel.stop()

            case '-PLAY-':
                audio_player_window['-STATUS-'].update('Playing')
                audio_player_window['-SONG-'].update(sound_path)
                song_channel.unpause() if is_paused else song_channel.play(song)
                is_paused = False

            case '-PAUSE-':
                song_channel.pause()
                audio_player_window['-STATUS-'].update('Paused')
                is_paused = True
      
            case '-STOP-':
                song_channel.stop()
                audio_player_window['-STATUS-'].update('Stopped')

            case '-SAVE-':
                mix =  my_song.get_names()
                my_song.get_mixes().export(f'/home/skawy/side_projects/music-mixer/saved/{mix}.wav', format='wav')

            case '-VOLUME-':
                volume = values['-VOLUME-']
                song_channel.set_volume(volume/100)

    audio_player_window.close()

if __name__ == '__main__':
    gui()