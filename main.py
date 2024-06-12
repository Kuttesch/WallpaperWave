import requests
import shutil
import ctypes
import time
import os
import argparse

filename = "pic.jpg"
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
url = "https://pixabay.com/api/?key=44350029-157b87ae5b114d717fab1bab3&image_type=photo"


def get_screen_resolution():
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def get_url_string(url, width, height):
    return f"{url}&min_width={width}&min_height={height}"



def download_file(url, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    return filename

def set_background(filename):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, filename, 0)

def main():
    width, height = get_screen_resolution()
    print(width, height)
    download_file(url_string, path)
    print(path)
    time.sleep(1)
    set_background(path)


width, height = get_screen_resolution()
print(width, height)
urlString = get_url_string(url, width, height)
print(urlString)