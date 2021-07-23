from youtubesearchpython import VideosSearch 

def queryName(keyWord, count, ask=False):
    
    result = VideosSearch(keyWord, limit=count) 
    
    resultParsed = {}
    
    i = 0
    for r in result.result()['result']:
        resultParsed[str(i)] = {} 
        resultParsed[str(i)]['title'] = r['title']
        resultParsed[str(i)]['link'] = r['link']
        resultParsed[str(i)]['duration'] = r['duration']

        i += 1
   
    if ask:
        print("Pick one:\n")

        for rp in resultParsed:
            print(rp + "\t" +  resultParsed[rp]['duration'] + "\t\t" + resultParsed[rp]['title'])

        print("\n> ", end="")
        option = input()

        return [resultParsed[option]['title'], resultParsed[option]['link']]

