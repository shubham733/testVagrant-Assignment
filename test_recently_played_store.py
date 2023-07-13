import pytest
from recently_played_store import RecentlyPlayedStore


def test_add_song():
    store = RecentlyPlayedStore(3)
    store.add_song("user1", "S1")
    store.add_song("user1", "S2")
    store.add_song("user1", "S3")
    store.add_song("user1", "S4")
    assert store.get_recently_played("user1") == ["S2", "S3", "S4"]


def test_get_recently_played():
    store = RecentlyPlayedStore(3)
    store.add_song("user1", "S1")
    store.add_song("user1", "S2")
    store.add_song("user1", "S3")
    assert store.get_recently_played("user1") == ["S1", "S2", "S3"]
    assert store.get_recently_played("user2") == []


def test_add_song_full_capacity():
    store = RecentlyPlayedStore(3)
    store.add_song("user1", "S1")
    store.add_song("user1", "S2")
    store.add_song("user1", "S3")
    store.add_song("user1", "S4")
    store.add_song("user1", "S5")
    assert store.get_recently_played("user1") == ["S3", "S4", "S5"]


def test_add_song_multiple_users():
    store = RecentlyPlayedStore(3)
    store.add_song("user1", "S1")
    store.add_song("user1", "S2")
    store.add_song("user2", "S3")
    store.add_song("user2", "S4")
    assert store.get_recently_played("user1") == ["S1", "S2"]
    assert store.get_recently_played("user2") == ["S3", "S4"]


def test_add_song_empty_store():
    store = RecentlyPlayedStore(3)
    store.add_song("user1", "S1")
    assert store.get_recently_played("user1") == ["S1"]


def test_add_song_nonexistent_user():
    store = RecentlyPlayedStore(3)
    store.add_song("user1", "S1")
    assert store.get_recently_played("user2") == []
