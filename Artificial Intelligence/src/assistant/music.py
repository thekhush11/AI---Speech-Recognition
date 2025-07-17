import os
import random
import webbrowser

def play_music(song_name):
    song_directory = "path_to_your_music_directory"  # Update this path
    song_path = os.path.join(song_directory, song_name + ".mp3")

    if os.path.exists(song_path):
        os.startfile(song_path)
    else:
        print("Song not found. Searching online...")
        search_online(song_name)

def search_online(song_name):
    query = f"https://www.youtube.com/results?search_query={song_name}"
    webbrowser.open(query)

def get_random_song():
    songs = ["song1", "song2", "song3"]  # Replace with actual song names
    return random.choice(songs)

def play_random_song():
    song_name = get_random_song()
    play_music(song_name)