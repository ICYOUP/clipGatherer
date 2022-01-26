import os
import sys
import subprocess
import twitchdl


os.system("twitch-dl clips loltyler1 --period last_day --download --limit 10")

folder = 'C:\\Users\\Knigh\\Documents\\GitHub\\redditclips'

def get_right_name(name):
    dash_list = []
    listified_name = list(name)
    print(listified_name)
    for index, a in enumerate(listified_name):
        if(a == '_'):
            dash_list.append(index)
    print(str(dash_list[1]) + "bruhh")
    listified_name = listified_name[dash_list[1]+1:]
    listified_name[:] = [x if x != '_' else ' ' for x in listified_name]
    listToStr = ''.join([str(elem) for elem in listified_name])
    return listToStr

for file in os.listdir(folder):
    name, extension = os.path.splitext(file)
    if extension == ".mp4":
        new_name = get_right_name(name)
        os.rename('C:\\Users\\Knigh\\Documents\\GitHub\\redditclips\\' + name + extension, 
                   'C:\\Users\\Knigh\\Documents\\GitHub\\redditclips\\videos\\' + new_name + extension)



print(get_right_name('20220125_1458858278_loltyler1_mods'))

