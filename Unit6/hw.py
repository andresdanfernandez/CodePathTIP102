"""class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def onRepeat(playlistHead):

    fast,slow = playlistHead, playlistHead
    while fast and fast.next:
        if fast == slow:
            return True
        fast = fast.next.next
        slow = slow.next
    return False

song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(onRepeat(song1))"""
