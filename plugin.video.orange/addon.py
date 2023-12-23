import sys
import xbmc
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, "movies")

def getMovieMetadata(imdb_id, key):
    info = xbmc.InfoTagVideo()

    info.setIMDBNumber(imdb_id)
    metadata = {"title": info.getTitle(),
                "year": info.getYear(),
                "genre": info.getGenres(),
                "rating": info.getRating("imdb"),
                "plot": info.getPlot()}
    
    return metadata[key]

# Movies along with their IMDB ID
movies_list = {"matrix": "tt0133093"}

movie = xbmcgui.ListItem(f"{getMovieMetadata(movies_list['matrix'], 'title')} [COLOR blue]({getMovieMetadata(movies_list['matrix'], 'year')})[/COLOR]")
#movie.setInfo("video", {})

movie.setArt({"poster": "https://www.themoviedb.org/t/p/original/qK76PKQLd6zlMn0u83Ej9YQOqPL.jpg", 
               "fanart": "https://www.themoviedb.org/t/p/original/y0jFVsgbvPE3AJqNxIPRhM7pWrO.jpg"})

url = "D:\Plex\Películas\Matrix (1999)\Matrix 1 - H265.mp4"

xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=movie)

xbmcplugin.endOfDirectory(addon_handle)