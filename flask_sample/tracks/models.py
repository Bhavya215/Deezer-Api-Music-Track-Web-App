from datetime import datetime
from decimal import Decimal
from numbers import Integral
from common.utils import JsonSerializable

class Track(JsonSerializable):
    def __init__(self, track_id: int, readable: bool, title: str, title_short: str,
                track_link: str , duration: int, track_rank: int,
                artist_name: str, album_name: str,
                created: datetime = None, modified: datetime = None):
        self.track_id = track_id
        self.readable = readable
        self.title = title
        self.title_short = title_short
        self.track_link = track_link
        self.duration = duration
        self.track_rank = track_rank
        self.artist_name = artist_name
        self.album_name = album_name
        self.created = created
        self.modified = modified