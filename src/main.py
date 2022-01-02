'''
pyMP (https://github.com/goncrust/pyMP)

Copyright (C) 2022 goncrust
Released under the GPL v3.0
https://github.com/goncrust/pyMP/blob/master/LICENSE.md
'''

import sys
import query
import downloader
import utils


def main(args):
    """pyMP main function
    """

    def keywordM():
        nonlocal mode_D
        nonlocal args

        size = 5
        if '-s' in args:
            size = int(args[args.index('-s') + 1])

        qresult = query.queryKeywordPlus(args[args.index('-k') + 1], size)
        
        if qresult == -1 or qresult is None:
            print("ERROR: no videos found")
            exit(-1)

        if mode_D:
            print("\nPick one:\n")
        else:
            print("\nResults:\n")

        for rp in qresult:
            print(rp + "\t" +  qresult[rp]['duration'] + "\t\t" + qresult[rp]['title'])

        if mode_D:
            print("\n> ", end="")
            option = input()

            return [qresult[option]['title'], qresult[option]['link']]


    def urlM():
        nonlocal args
        nonlocal mode_D
        url = args[args.index('-u') + 1]

        if mode_D:
            print("Starting download, please wait...")
        else:
            print("Getting information, please wait...")
        name = query.queryNameFromURL(url)

        if name == -1:
            print("ERROR: invalid URL")
            exit(-1)

        return [name, url]
    

    def plM():
        nonlocal mode_D
        nonlocal args

        p_url = args[args.index('-p') + 1]

        print("Getting information about the playlist, please wait...")
        qresult = query.queryPlaylistInfo(p_url)

        if qresult == -1:
            print("ERROR: playlist not found")
            exit(-1)

        print("\nPlaylist:\n")
        i = 1
        for qr in qresult:
            print(str(i) + "\t" + utils.secondsToMinutes(qresult[qr]['duration']) + "\t\t" + qr)
            i += 1
            
        if mode_D:
            print("\nConfirm download (Y/n): ", end="")

            ans = input()

            if (ans != '' and ans.lower()[0] != 'y'):
                exit(0)

        returnVideos = [] 
        for qr in qresult:
            returnVideos.append([qr, qresult[qr]['link']])

        return returnVideos

    # Display help
    if len(args) < 4 or '-h' in args or args[1] not in ('D', 'Q', 'd', 'q'):
        help_page()
        
    mode_D = args[1] in ('D', 'd')
    
    if '-k' in args:
        qresult = keywordM()
        if not mode_D:
            exit(0)

    elif ('-u' in args):
        qresult = urlM()
        if not mode_D:
            print(f"\n{qresult[1]}:\t{qresult[0]}")
            exit(0)
            
    elif ('-p' in args):
        qresult = plM()
        if not mode_D:
            exit(0)

        # Download (for playlists)
        i = 1
        for qr in qresult:
            if ('-o' in args):
                downloader.downloadYTURL(qr[1], str(i) + " " + qr[0], args[args.index('-o') + 1], True)
            else:
                downloader.downloadYTURL(qr[1], str(i) + " " + qr[0])
            i += 1

        print("Finished download!")
        exit(0)
    
    # Download
    if ('-o' in args):
        downloader.downloadYTURL(qresult[1], qresult[0], args[args.index('-o') + 1])
    else:
        downloader.downloadYTURL(qresult[1], qresult[0])

    print("Finished download!")
    exit(0)
    

def help_page():
    """Display help page
    """

    print("usage: python src/main.py [mode] [options] [...]\n")
    print("modes:")
    print("\tD\t\t\tDownload mode.")
    print("\tQ\t\t\tQuery mode.\n")
    print("options:")
    print("\t-h\t\t\tDisplays this help message.")
    print("\t-k <keyword>\t\tKeyword for query (also works with D mode).")
    print("\t-s <number>\t\tQuery size (default: 5).")
    print("\t-u <URL>\t\tURL for download.")
    print("\t-p <URL>\t\tURL for playlist download.")
    print("\t-o <output file>\tSet destination file name and location (default: current/working directory, filename=video's title.mp3).")

    exit(0)


if __name__ == '__main__':
    main(sys.argv)

