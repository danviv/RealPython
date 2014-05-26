#youtube webservices example
#example user id: SonyMusicIndiaVEVO

import gdata.youtube
import gdata.youtube.service

youtube_service=gdata.youtube.service.YouTubeService()

playlist=raw_input("Please enter the user id")

url="http://gdata.youtube.com/feeds/api/users/"
playlist_url=url+playlist+"/playlists"

playlist_feed = youtube_service.GetYouTubePlaylistVideoFeed(playlist_url)

#print playlist_feed

print "\nPlaylists for " + str.format(playlist) + ":\n"

for p in playlist_feed.entry:
	print p.title.text
	#print p
	
	playlistid = p.id.text.split('/')[-1]
	video_feed = youtube_service.GetYouTubePlaylistVideoFeed(playlist_id=playlistid)
	for v in video_feed.entry:
		print "\t"+v.title.text
		#print v
	