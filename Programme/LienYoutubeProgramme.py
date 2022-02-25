import urllib.request
import re

search_keyword="umaru chan op"
new_string = search_keyword.replace(" ", "+")

html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + new_string)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
print("https://www.youtube.com/watch?v=" + video_ids[0])