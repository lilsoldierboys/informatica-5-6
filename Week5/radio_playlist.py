import time

playlist = ["STELLA LEFTY", " Dracula", "I Knew It, I Knew You", " hate that i made you love me", " Risk It All"]


playlist.append("Be By You")
playlist.insert(0, "Bohemian Rhapsody")
playlist.pop(4)




print(playlist)
print(playlist.index(" Risk It All"))
print(len(playlist))
playlist.reverse()
print(playlist)
playlist.sort()
print(playlist)



repeat = len(playlist)
while repeat > 0:
    print(playlist)
    song = playlist[0]
    playlist.pop(0)
    playlist.append(song)
    repeat -= 1
    time.sleep(3)
