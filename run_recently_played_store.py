from recently_played_store import RecentlyPlayedStore;

store = RecentlyPlayedStore(3)
store.add_song("user1", "S1")
store.add_song("user1", "S2")
store.add_song("user1", "S3")
store.add_song("user1", "S4")
store.add_song("user2", "S3")
recentlyPlayed = store.get_recently_played("user1")
print(recentlyPlayed)
recentlyPlayed = store.get_recently_played("user2")
print(recentlyPlayed)
store.print_store()