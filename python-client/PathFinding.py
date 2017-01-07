import requests

class PathFinding:
    def __init__(self):
        self.path = "http://game.blitz.codes:8081/pathfinding/direction"
    def getPath(self, theMap, size, start, target):
        url = ""
        url += self.path + "?size=" + size
        url += "&start=" + start
        url += "&target=" + target
        url += "&map=" + theMap
        response = requests.get(self.path)
        return response["direction"]
