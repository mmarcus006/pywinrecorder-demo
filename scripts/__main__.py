"""Record & replay example using pywinauto_recorder.player"""
from pywinauto_recorder.player import playback

if __name__ == "__main__":
    playback(filename="scripts/recorded_notepad.py")
