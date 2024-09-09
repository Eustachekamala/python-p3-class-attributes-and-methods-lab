class Song:
    count = 0  # Class attribute to keep track of the number of songs
    genres = []  # Class attribute to store unique genres
    artists = []  # Class attribute to store unique artists
    genre_count = {}  # Class attribute to count the number of songs for each genre
    artist_count = {}  # Class attribute to count the number of songs for each artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update class attributes
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    # Class methods to update class attributes
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
        
    # Add a song to the genres list if it doesn't exist
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            
    # Add a song to the artists list if it doesn't exist
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
            
    # Add a song to the genre count if it doesn't exist
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
            
    # Add a song to the artist count if it doesn't exist
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
            
    # Class methods to get class attributes
    @classmethod
    def show_genre_count(cls):
        return cls.genre_count
    
    # Class methods to get class attributes
    @classmethod
    def show_artist_count(cls):
        return cls.artist_count

# Example usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
print(ninety_nine_problems.name)  
print(ninety_nine_problems.artist)
print(ninety_nine_problems.genre)

# Create more songs to test
song1 = Song("Song1", "Artist1", "Rock")
song2 = Song("Song2", "Artist1", "Rap")
song3 = Song("Song3", "Artist2", "Country")
song4 = Song("Song4", "Artist3", "Rap")

print(Song.count) 
print(Song.genres)
print(Song.artists)
print(Song.show_genre_count())
