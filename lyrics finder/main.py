# lyrics  finder addons\\
from scan_we import scan_from_file
from listen_type import listen_to_song, type_lyrics



print("LYRICS FINDER")
user_input = int(input("1 to listen\n2 to type lyrics\n"))

if user_input == 1:
    listen_to_song()
elif user_input == 2:
    type_lyrics()
else:
    print(" wrong Input")
    




