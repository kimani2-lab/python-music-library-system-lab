class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        """
        Initialize a Song instance with name, artist, and genre.
        Automatically updates global song statistics.
        
        Args:
            name (str): The name of the song
            artist (str): The artist who created the song
            genre (str): The genre of the song
        """
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment total song count
        Song.count += 1
        
        # Add to unique genres if not already present
        if genre not in Song.genres:
            Song.genres.append(genre)
        
        # Add to unique artists if not already present
        if artist not in Song.artists:
            Song.artists.append(artist)
        
        # Update genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        
        # Update artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
