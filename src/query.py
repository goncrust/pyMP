from youtubesearchpython import VideosSearch 
import youtube_dl
import math

def queryName(keyWord, count, ask=0):
    
    result = VideosSearch(keyWord, limit=count) 
    
    resultParsed = {}
    
    i = 1
    for r in result.result()['result']:
        resultParsed[str(i)] = {} 
        resultParsed[str(i)]['title'] = r['title']
        resultParsed[str(i)]['link'] = r['link']
        resultParsed[str(i)]['duration'] = r['duration']

        i += 1
   
    if ask:
        if ask == 2: 
            print("\nPick one:\n")
        elif ask == 1:
            print("\nResults:\n")

        for rp in resultParsed:
            print(rp + "\t" +  resultParsed[rp]['duration'] + "\t\t" + resultParsed[rp]['title'])
        
        if ask == 2:
            print("\n> ", end="")
            option = input()

            return [resultParsed[option]['title'], resultParsed[option]['link']]
    
    else:
        return resultParsed

def queryNameFromURL(url):
    
    with youtube_dl.YoutubeDL({}) as ydl:
        info = ydl.extract_info(url, download=False)

    return info['title']

def secondsToMinutes(seconds):
    minutes = math.floor(seconds / 60)
    rseconds = seconds - (minutes*60)

    return str(minutes) + ":" + str(rseconds)

def queryPlaylistInfo(url, ask=0):
    
    videosParsed = {}

    with youtube_dl.YoutubeDL({}) as ydl:
        videos = ydl.extract_info(url, download=False)

    for v in videos['entries']:
        videosParsed[v['title']] = {} 
        videosParsed[v['title']]['link'] = v['webpage_url']
        videosParsed[v['title']]['duration'] = v['duration']

    if ask == 1 or ask == 2:
        print("\nPlaylist:\n")

        i = 1
        for vp in videosParsed:
            print(str(i) + "\t" + secondsToMinutes(videosParsed[vp]['duration']) + "\t\t" + vp)

            i += 1
        
        if (ask == 2):
            print("\nConfirm download (y/n): ", end="")

            ans = input()

            if (ans.lower()[0] == 'y'):
                returnVideos = [] 

                for vp in videosParsed:
                    returnVideos.append([vp, videosParsed[vp]['link']])

                return returnVideos
            else:
                return
        else:
            return

    elif ask == 0:
        return videosParsed
