import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, "movies")

url = "D:\Plex\Películas\Matrix (1999)\Matrix 1 - H265.mp4"

matrix = xbmcgui.ListItem("Matrix [COLOR blue](1999)[/COLOR]")
matrix.setArt({"poster": "https://www.themoviedb.org/t/p/original/qK76PKQLd6zlMn0u83Ej9YQOqPL.jpg", 
               "fanart": "https://www.themoviedb.org/t/p/original/y0jFVsgbvPE3AJqNxIPRhM7pWrO.jpg"})

xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=matrix)

xbmcplugin.endOfDirectory(addon_handle)