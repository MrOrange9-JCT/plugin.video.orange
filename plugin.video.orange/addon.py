import sys
import xbmc
import xbmcgui
import xbmcplugin
import requests

addon_handle = int(sys.argv[1])
__url__ = sys.argv[0]

xbmcplugin.setContent(addon_handle, "movies")

def getMovieMetadata(movie_title, requested_metadata):

    tmdb_id = movie_list[movie_title][0]
    api_key = "-706d6c75628138ee3084133305f15bf6-ee30841333e3084133305f15bf6"

    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?language=es-ES&api_key={api_key.split('-')[1]}"
    response = requests.get(url)
    r = response.json()

    metadata = {"title": r["title"],
                "year": int(r["release_date"].split("-")[0]),
                "genres": r["genres"],
                "rating": r["vote_average"],
                "duration": r["runtime"] * 60,
                "tagline": r["tagline"],
                "plot": r["overview"],
                "poster": "https://www.themoviedb.org/t/p/original" + r["poster_path"],
                "fanart": "https://www.themoviedb.org/t/p/original" + r["backdrop_path"]}
    
    return metadata[requested_metadata]

def getMovieList():
    """"Get the updated movie list from Rentry.co"""
    url = "https://rentry.co/OrangeAddon_movie_list/raw"
    response = requests.get(url)

    return response.json()

def updateMovieList():
    """Update the movie list on Rentry.co"""
    url = "https://rentry.co/OrangeAddon_movie_list/raw"
    response = requests.get(url)

    global movie_list
    movie_list = response.json()

    return __url__ + "/update"

# Movies along with their TMDB ID
movie_list = getMovieList()

update_list = xbmcgui.ListItem("[COLOR lime] - Actualizar lista de películas - [/COLOR]")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=updateMovieList(), listitem=update_list, isFolder=True)

for movie in movie_list:
    list_item = xbmcgui.ListItem(f"{getMovieMetadata(movie, 'title')} [COLOR blue]({getMovieMetadata(movie, 'year')})[/COLOR]")
    list_item.setInfo("video", {"genre": getMovieMetadata(movie, 'genres'),
                                "rating": getMovieMetadata(movie, 'rating'),
                                "duration": getMovieMetadata(movie, 'duration'),
                                "plotoutline": getMovieMetadata(movie, 'tagline'),
                                "plot": getMovieMetadata(movie, 'plot'),
                                "year": getMovieMetadata(movie, 'year'),
                                "title": getMovieMetadata(movie, 'title'),})

    list_item.setArt({"poster": getMovieMetadata(movie, 'poster'), 
                "fanart": getMovieMetadata(movie, 'fanart')})

    url = movie_list[movie][1]

    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=list_item)

xbmcplugin.endOfDirectory(addon_handle)