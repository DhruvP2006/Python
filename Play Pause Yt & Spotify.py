import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import time

# Spotify setup
SPOTIFY_CLIENT_ID = '4cdd9f85fdb644df83d22618f206ee01'
SPOTIFY_CLIENT_SECRET = '200a12ce107e4b53aaf759cd613b6c5d'
SPOTIFY_REDIRECT_URI = 'http://localhost:8080'  # Standard redirect URI for Spotify
scope = "user-read-playback-state user-modify-playback-state"

# Selenium setup for YouTube
CHROME_DRIVER_PATH = "D:\chromedriver_win32\chromedriver.exe"  # Update this with your chromedriver path

# Initialize Spotify API client
spotify = Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope=scope
))

# Selenium WebDriver
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
youtube_tab = None

def toggle_spotify():
    """Toggle Spotify play/pause."""
    playback = spotify.current_playback()
    if playback and playback['is_playing']:
        spotify.pause_playback()
    else:
        spotify.start_playback()

def toggle_youtube():
    """Toggle YouTube play/pause."""
    global youtube_tab
    if not youtube_tab:
        youtube_tab = driver.current_window_handle
    driver.switch_to.window(youtube_tab)
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.SPACE)

def play_pause_handler():
    """Handle play/pause key toggle."""
    playback = spotify.current_playback()
    if playback and playback['is_playing']:
        toggle_spotify()
        print("Spotify paused; playing YouTube.")
        toggle_youtube()
    else:
        toggle_youtube()
        print("YouTube paused; playing Spotify.")
        toggle_spotify()

# Start the YouTube session
def start_youtube(url):
    """Open YouTube and prepare for control."""
    driver.get(url)
    time.sleep(3)  # Allow the page to load

# Run the program
if __name__ == "__main__":
    youtube_url = input("Enter the URL of the YouTube video: ")
    start_youtube(youtube_url)

    print("Script is running. Press the play/pause media key to toggle between YouTube and Spotify.")
    keyboard.add_hotkey('play/pause media', play_pause_handler)
    keyboard.wait('esc')
    print("Exiting script...")
    driver.quit()
