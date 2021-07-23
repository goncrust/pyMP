import sys
import query
import downloader

qresult = query.queryName(sys.argv[1], 5, True)

downloader.downloadYTURL(qresult[1], qresult[0])
