import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'file:///D:/Plex/Películas/Matrix%20(1999)/Matrix%201%20-%20H265.mp4'
li = xbmcgui.ListItem('My First Video!', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)