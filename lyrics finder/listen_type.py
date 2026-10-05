# from scan_we import scan_from_file
from scan_we import *


def listen_to_song():
    microphone = int(input("Type 1 to enable microphone: "))
    
    if microphone == 1:
        print("Microphone enabled.\nSearching for song...\n")
        time.sleep(0.5)
        scan_from_file()
    else:
        print("WRONG INPUT")
        
def type_lyrics():
    print("type lyrics here")
    lyrics_str = str(input("Song: " ))
    print(f"searching for {lyrics_str} ")
    scan_from_file()
        
        
        
# listen_to_song()
# type_lyrics()
        