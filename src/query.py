'''
pyMP (https://github.com/goncrust/pyMP)

Information gathering about youtube videos/playlists

Copyright (C) 2022 goncrust
Released under the GPL v3.0
https://github.com/goncrust/pyMP/blob/master/LICENSE.md
'''

from youtubesearchpython import VideosSearch 
from yt_dlp import YoutubeDL
import utils


class DowloadLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


ydl_opts = {'logger': DowloadLogger()}


def queryKeywordPlus(keyword, count):
    """Query video title, URL and duration
    """
    
    result = VideosSearch(keyword, limit=count) 
    resultParsed = {}
    
    i = 1
    for r in result.result()['result']:
        resultParsed[str(i)] = {} 
        resultParsed[str(i)]['title'] = r['title']
        resultParsed[str(i)]['link'] = r['link']
        resultParsed[str(i)]['duration'] = r['duration']

        i += 1

    if not len(resultParsed):
        return -1
   
    return resultParsed


def queryNameFromURL(url):
    """Query video title from URL
    """
    
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    if info is None:
        return -1

    return info['title']


def queryPlaylistInfo(url):
    """Query playlist videos titles, URLs and durations; prompt user to confirm

    if ask == 0: just return the query
    elif ask == 1: print
    elif ask == 2: print and prompt user to confirm download
    """
    
    videosParsed = {}

    with YoutubeDL(ydl_opts) as ydl:
        videos = ydl.extract_info(url, download=False)

    if videos is None:
        return -1

    for v in videos['entries']:
        videosParsed[v['title']] = {} 
        videosParsed[v['title']]['link'] = v['webpage_url']
        videosParsed[v['title']]['duration'] = v['duration']

    return videosParsed

