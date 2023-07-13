from collections import deque
from typing import List

class RecentlyPlayedStore:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}

    def add_song(self, user: str, song: str):
        if user not in self.store:
            self.store[user] = deque(maxlen=self.capacity)
        self.store[user].append(song)

    def get_recently_played(self, user: str) -> List[str]:
        if user in self.store:
            return list(self.store[user])
        return []

    def print_store(self):
        for user, songs in self.store.items():
            print(f"User: {user}")
            for song in songs:
                print(f"   - {song}")
