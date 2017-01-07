import requests
import urllib

class PathFinding:
    def __init__(self):
        self.path = "http://game.blitz.codes:8081/pathfinding/direction"
    def getPath(self, theMap, size, start, target):
        try:
            start_f = "(" + str(start["x"]) + "," + str(start["y"]) + ")"
            target_f = "(" + str(target[0]) + "," + str(target[1]) + ")"
            url = ""
            url += self.path + "?size=" + str(size)
            url += "&start=" + start_f
            url += "&target=" + target_f +"&"
            theRealMap = {}
            theRealMap["map"] = theMap["tiles"]
            url +=  urllib.parse.urlencode(theRealMap)

            response = requests.get(url, timeout=0.200)

            return response.json()["direction"]
        except:
            print("Alert shit happened")
            return 'Stay'
