import os

def get_right_name(name):
    dash_list = []
    listified_name = list(name)
    for index, a in enumerate(listified_name):
        if(a == '_'):
            dash_list.append(index)
    listified_name = listified_name[dash_list[1]+1:]
    listified_name[:] = [x if x != '_' else ' ' for x in listified_name]
    listToStr = ''.join([str(elem) for elem in listified_name])
    return listToStr

def move_files():
    folder = 'C:\\Users\\Knigh\\Documents\\GitHub\\redditclips'
    for file in os.listdir(folder):
        name, extension = os.path.splitext(file)
        if extension == ".mp4":
            new_name = get_right_name(name)
            try:
                os.rename('C:\\Users\\Knigh\\Documents\\GitHub\\redditclips\\' + name + extension, 
                        'C:\\Users\\Knigh\\Documents\\GitHub\\redditclips\\videos\\' + new_name + extension)
            except:
                print("uh oh whimper and piss time")
                try:
                    os.remove('C:\\Users\\Knigh\\Documents\\GitHub\\redditclips\\' + name + extension)
                except:
                    print("actually start whimpering")