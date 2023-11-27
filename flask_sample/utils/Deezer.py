import os
# fix for testing just this file
if __name__ == "__main__":

    import sys
    # Get the parent directory of the current script (api.py)
    CURR_DIR = os.path.dirname(os.path.abspath(__file__))

    # Add the parent directory to the Python path
    PARENT_DIR = os.path.join(CURR_DIR, "..")  # Go up one level from utils to project folder
    sys.path.append(PARENT_DIR)
from utils.api import API
class Deezer(API):
    @staticmethod
    def search(q):
        params = {}
        params["q"] = f"{q}"
        params["datatype"] = "json"
        url = "/search"
        resp = API.get(url, params)
        return resp
    
    def Artist(id):
        params = {}
        params["id"] = f"{id}"
        params["datatype"] = "json"
        url = "/artist/" + id
        #print(url)
        resp = API.get(url, params)
        #print(resp)
        return resp


if __name__ == "__main__":
    resp1 = Deezer.search("cruel summer")
    resp2 = Deezer.Artist("12246")
    
    # print(resp1)
    # print(resp2)

    if resp1 and "data" in resp1:
        from utils.lazy import DictToObject
        data_point_search = resp1["data"][0]
        resp = DictToObject(data_point_search)
        artist = DictToObject(resp.artist)
        print("Search Result:")
        print(artist.id)

    # #Extracting one data point from the artist response
    # if resp2 and "data" in resp2:
    #     data_point_artist = resp2["data"]
    #     print("\nArtist Information:")
    #     print(data_point_artist)