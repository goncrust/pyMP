'''
pyMP (https://github.com/goncrust/pyMP)

Copyright (C) 2021 goncrust
Released under the GPL v3.0
https://github.com/goncrust/pyMP/blob/master/LICENSE.md
'''

import sys
import query
import downloader

def help_page():
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
    print("\t-o <output file>\tSet destination file name and location.")

def main(args):
    
    # Display help
    if (len(args) < 2 or '-h' in args):
        help_page()
        
    # Download mode
    elif (args[1] == 'D'):
        
        qresult = []
        
        # Keyword
        if ('-k' in args):
            if ('-s' in args):
                qresult = query.queryName(args[args.index('-k') + 1], int(args[args.index('-s') + 1]), 2)
            else:    
                qresult = query.queryName(args[args.index('-k') + 1], 5, 2)
        
        # URL
        elif ('-u' in args):
            url = args[args.index('-u') + 1]
            qresult.append(query.queryNameFromURL(url))
            qresult.append(url)
        
        # Playlist URL
        elif ('-p' in args):
            p_url = args[args.index('-p') + 1]
            qresult = query.queryPlaylistInfo(p_url, 2)

            i = 1
            for qr in qresult:
                if ('-o' in args):
                    downloader.downloadYTURL(qr[1], str(i) + " " + qr[0], args[args.index('-o') + 1], True)
                else:
                    downloader.downloadYTURL(qr[1], str(i) + " " + qr[0])

                i += 1

            return
        
        # Keyword/URL output file
        if ('-o' in args):
            downloader.downloadYTURL(qresult[1], qresult[0], args[args.index('-o') + 1])
        else:
            downloader.downloadYTURL(qresult[1], qresult[0])
    
    # Query mode
    elif (args[1] == 'Q'):
        
        # Keyword
        if ('-k' in args):
            if ('-s' in args):
                query.queryName(args[args.index('-k') + 1], int(args[args.index('-s') + 1]), 1)
            else:    
                query.queryName(args[args.index('-k') + 1], 5, 1)
       
        # URL
        elif ('-u' in args):
            url = args[args.index('-u') + 1]
            print(query.queryNameFromURL(url))
        
        # Playlist
        elif ('-p' in args):
            p_url = args[args.index('-p') + 1]
            qresult = query.queryPlaylistInfo(p_url, 1)
    
    else:
        help_page()


main(sys.argv)
