import PySimpleGUI as sg
import pygame
from pydub import AudioSegment

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
        [sg.Text("Choose a Song To Separate: "), sg.Input(), sg.FileBrowse(key="-TO_SEPARATE_PATH-")],
        
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

    while True:
        event, values = audio_player_window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            break
        
        empty_song = AudioSegment.silent(duration=10000)

        empty_song.export("/home/skawy/side_projects/music-mixer/saved/empty.wav", format='wav')

       # sound_path = '/home/skawy/side_projects/music-mixer/audio_output/song1/accompaniment.wav'
        sound_path = '/home/skawy/side_projects/music-mixer/saved/empty.wav'
        # sound_path = values["-SOUND_PATH-"]
        # if not sound_path:
        #     sg.Popup("No song specified.")
        #     continue

        song = pygame.mixer.Sound(sound_path)
        # song_length = song.get_length()
        song_channel = pygame.mixer.Channel(2)

        if event == '-PLAY-':
            audio_player_window['-STATUS-'].update('Playing')
            audio_player_window['-SONG-'].update(sound_path)
            song_channel.unpause() if is_paused else song_channel.play(song)
            is_paused = False
        elif event == '-PAUSE-':
            song_channel.pause()
            audio_player_window['-STATUS-'].update('Paused')
            is_paused = True

        elif event == '-STOP-':
            song_channel.stop()
            audio_player_window['-STATUS-'].update('Stopped')

        elif event == '-VOLUME-':
            volume = values['-VOLUME-']
            song_channel.set_volume(volume/100)

    audio_player_window.close()

if __name__ == '__main__':
    gui()