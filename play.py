#!python3
#encoding=utf-8
from __future__ import print_function, division, absolute_import

import sys
import time
import re
import os
from pathlib import Path

winamp_path = Path(r'C:\\Program Files (x86)\\Winamp')
music_path = Path('C:/Users/Leonardo/Music')

def getFolders(bands):
    result = []
    folders = music_path.glob('*')
    for folder in folders:
        for band in bands:
            if folder.match('*'+band+'*'):
                if not folder in result: result += [folder];
    return result

def getPlayFolders(folders, answer):
    result = []
    if answer == '*' or answer == 'all':
        result = [folder for folder in folders]
    else:
        numbers = re.findall(r'\d+', answer)
        result = [folders[int(x) - 1] for x in numbers]
    return result

def main(bands):
    folders = getFolders(bands)
    play_folders = []
    if len(folders) == 0:
        print('Bands "'+', '.join(bands)+'" not found')
        input()
        sys.exit(0)
    elif len(folders) > 1:
        print('Type what you want to listen:')
        i = 1
        for folder in folders:
            print('%3d \t %s' % (i, folder.name))
            i += 1
        while 1:
            play_folders = getPlayFolders(folders, input())
            if len(play_folders) == 0:
                print('Please, insert valid numbers')
            else:
                break
    else:
        play_folders += [folders[0]]
        print('Folder "'+play_folders[0].name+'" found.')

    def execmd(command):
        print(command)
        os.system(command)

    execmd('vlc --playlist-tree --random --qt-start-minimized '+' '.join(['"'+str(f)+'"' for f in play_folders]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Type what do you want to listen, like: <band, band, band>')
        print('Type * to listen all')
        bands = input()
        if bands == 'all' or bands == '*':
            bands = ['*']
        elif bands == 'root':
            bands = ['*.mp3']
        else:
            matches = re.findall(r'\w+', bands)
            bands = [x for x in matches]
        main(bands)
    elif sys.argv[1] == '--help':
        print('Usage: play <band>')
    else:
        bands = [sys.argv[1], sys.argv[1].replace('_', ' ')]
        if bands[1] == bands[0]:
            bands.pop()
        main(bands)
