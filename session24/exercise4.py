class Song:
    """
    Attribute:
        Song Name:
        Artist:
        Song Length:
    Methods:
        __init__
        __str__
        __add__
    """

    def __init__(self, name, artist, length, songs = None):
        self.name = name
        self.artist = artist
        self.length = length
        if songs == None:
            songs = []
        self.songs_list = songs

    def __str__(self):
        return f"{self.name},{self.artist},{self.length}"
    
class Songlist:

    def __init__(self):
        self.song_list = []

    def add_song(self,song):
        self.song_list.append(song)

    def total_length(self):
        total = 0
        for song in self.song_list:
            total += int(song.length.split(":")[0]) * 60 + int(song.length.split(":")[1])
        return f"{total // 60}:{total % 60:02d}"

    def __str__(self):
        result = ""
        for i, song in enumerate(self.song_list):
            result += f"{i+1}. {str(song)}\n"
        return result.strip()

song_list = Songlist()

song1 = Song("Flowers", "Jisoo", "3:15")
song2 = Song("Leave the door open", "Bruno Mars", "4:20")

song_list.add_song(song1)
song_list.add_song(song2)

print(song_list)

