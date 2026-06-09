class Song:
    count = 0
    genres = []
    artists = []
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
    
