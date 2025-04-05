import os
import subprocess as sp

paths = {
    'spotify': r"C:\Users\NewUser\AppData\Roaming\Spotify\Spotify.exe",
    'browser': r"C:\Program Files\Mozilla Firefox\firefox.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'telegram': r"C:\Users\NewUser\AppData\Roaming\Telegram Desktop\Telegram.exe",
    'dota': r"E:\SteamLibrary\steamapps\common\dota 2 beta\game\bin\win64\dota2.exe"
}


def open_spotify():
    os.startfile(paths['spotify'])


def open_browser():
    os.startfile(paths['browser'])


def open_cmd():
    os.system('start cmd')


def open_calc():
    sp.Popen(paths['calculator'])


def open_telegram():
    os.startfile(paths['telegram'])


def open_dota():
    os.startfile(paths['dota'])