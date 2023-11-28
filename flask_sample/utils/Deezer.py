#Bhavya Shah
#22 November 2023
import os
# fix for testing just this file
if __name__ == "__main__":

    import sys
    # Get the parent directory of the current script (api.py)
    CURR_DIR = os.path.dirname(os.path.abspath(__file__))

    # Add the parent directory to the Python path
    PARENT_DIR = os.path.join(CURR_DIR, "..")
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


if __name__ == "__main__":
    resp1 = Deezer.search("Eminem")

    if resp1 and "data" in resp1:
        from utils.lazy import DictToObject
        data_point_search = resp1["data"][0]
        print("Search Result:")
        print(data_point_search)