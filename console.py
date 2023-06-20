import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


artist1 = Artist("Harry", "Styles")
artist_repository.save(artist1)

artist2 = Artist("Maisie", "Peters")
artist_repository.save(artist2)

album1 = Album("Fine Line", "Pop rock", artist1 )


album2 = Album("Dressed Too Nice For a Jacket", "Pop", artist2 )






pdb.set_trace()