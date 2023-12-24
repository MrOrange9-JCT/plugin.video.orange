import sys
import xbmc
import xbmcgui
import xbmcplugin
import requests
import simplejson as json

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, "movies")

def getMovieMetadata(movie_title, requested_metadata):

    tmdb_id = movie_list[movie_title]
    api_key = "-706d6c75628138ee3084133305f15bf6-ee30841333e3084133305f15bf6"

    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?language=es-ES&api_key={api_key.split('-')[1]}"
    response = requests.get(url)
    r = response.json()

    metadata = {"title": r["title"],
                "year": r["release_date"].split("-")[0],
                "genres": r["genres"],
                "rating": r["vote_average"],
                "duration": r["runtime"] + " min",
                "tagline": r["tagline"],
                "plot": r["overview"],}
    
    return metadata[requested_metadata]

def getMovieList():
    """"Get the updated movie list from Rentry.co"""
    url = "https://rentry.co/OrangeAddon_movie_list/raw"
    response = requests.get(url)

    return response.json()

# Movies along with their TMDB ID
movie_list = getMovieList()

movie = xbmcgui.ListItem(f"{getMovieMetadata('matrix', 'title')} [COLOR blue]({getMovieMetadata('matrix', 'year')})[/COLOR]")
movie.setInfo("video", {})

movie.setArt({"poster": "https://www.themoviedb.org/t/p/original/qK76PKQLd6zlMn0u83Ej9YQOqPL.jpg", 
               "fanart": "https://www.themoviedb.org/t/p/original/y0jFVsgbvPE3AJqNxIPRhM7pWrO.jpg"})

url = "D:\Plex\Películas\Matrix (1999)\Matrix 1 - H265.mp4"

xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=movie)

xbmcplugin.endOfDirectory(addon_handle)