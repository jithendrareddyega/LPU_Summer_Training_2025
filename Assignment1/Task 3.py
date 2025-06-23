

def add_album(library, album_info):
    artist, title, year, songs = album_info
    library[title] = (artist, year, songs)
    return library

def create_playlist(library, selections):
    playlist = []
    for album_title, song in selections:
        if album_title in library and song in library[album_title][2]:
            playlist.append(song)
    return playlist

def add_song_to_album(library, album_title, song):
    if album_title in library:
        artist, year, songs = library[album_title]
        if song not in songs:
            songs.append(song)
            library[album_title] = (artist, year, songs)
    return library

def remove_song_from_playlist(playlist, song):
    if song in playlist:
        playlist.remove(song)
    return playlist


library = {}
playlist = []

while True:
    print("\n===== Music Library Menu =====")
    print("1. Add a new album")
    print("2. Create a playlist")
    print("3. Add a song to an album")
    print("4. Remove a song from playlist")
    print("5. View album library")
    print("6. View playlist")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        artist = input("Enter artist name: ")
        title = input("Enter album title: ")
        year = int(input("Enter release year: "))
        songs = input("Enter songs (comma separated): ").split(",")
        songs = [song.strip() for song in songs]
        album_info = (artist, title, year, songs)
        library = add_album(library, album_info)
        print("Album added successfully.")

    elif choice == "2":
        selections = []
        n = int(input("How many songs to add to playlist? "))
        for _ in range(n):
            album_title = input("Enter album title: ")
            song = input("Enter song name: ")
            selections.append((album_title, song))
        playlist = create_playlist(library, selections)
        print("Playlist created/updated.")

    elif choice == "3":
        album_title = input("Enter album title: ")
        new_song = input("Enter new song to add: ")
        library = add_song_to_album(library, album_title, new_song)
        print("Song added to album.")

    elif choice == "4":
        song = input("Enter song to remove from playlist: ")
        playlist = remove_song_from_playlist(playlist, song)
        print("Song removed from playlist.")

    elif choice == "5":
        print("\n--- Music Library ---")
        for title, (artist, year, songs) in library.items():
            print(f"Album: {title}, Artist: {artist}, Year: {year}, Songs: {songs}")

    elif choice == "6":
        print("\n--- Playlist ---")
        print(playlist)

    elif choice == "7":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
