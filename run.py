from unicodedata import category
from twitch_stuff import *
from reddit import *
import datetime
from time import sleep
cycleNum = 0
while True:
    now = datetime.datetime.now()
    if ((now.strftime("%w") == str(6) or now.strftime("%w") == str(0)) and now.hour == 21):
        
        twitch_download("LCS", 3, "day")
    
    if ((now.strftime("%w") == str(5) or now.strftime("%w") == str(6)) and now.hour == 16):
        twitch_download("LEC", 3, "day")
    
    if now.hour == 0:
        reddit_vid_download("leagueoflegends", "day", 1000)

    folder = 'C:\\Users\\Knigh\\Documents\\GitHub\\redditclips\\videos'
    for path in os.listdir(folder):
        full_path = '"' + os.path.join(folder, path) + '"'
        new_path = '"' + os.path.splitext(path)[0] + '"'
        description = '"LEAGUE OF LEGENDS FUNNY AND SAD AND EPIC MOMENTS #lol #leagueoflegends #funny #sad #reddit #good #gaming #gamingmoments #lolmoments #leaguemoments #leaguefunny #funnygaming"'
        keyword = "lol,leagueoflegends,professionallol,epic,epicfail,epicwin,funny,lolfunnymoments"
        cat = "20"
        privacy = "private"
        os.system("python upload_video.py --file=" + full_path +  " --title=" + new_path +  
                        " --description=" + description +
                        " --keywords=" + keyword +
                        " --category=" + cat +
                        " --privacyStatus=" + privacy)
        try:
                os.replace(os.path.join(folder, path), 
                        'C:\\Users\\Knigh\\Documents\\GitHub\\redditclips\\oldvids\\' + path)
        except:
            print("uh oh whimper and piss time")
    cycleNum = cycleNum + 1
    print("cycle: " + str(cycleNum) + str(now))       
    sleep(60 * 60)