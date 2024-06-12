import requests
import shutil
import ctypes
import time
import os
import argparse
import showPic  #showPic.py is a file that I created to show the image in Terminal                                                                             

filename = "pic.jpg"
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
urlString = "https://picsum.photos"

def get_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--auto', action='store_true', help='Automatically set as desktop background')
    args = parser.parse_args()
    if args.auto:
        get_user_acceptance()
    else:
        set_background(path)

def get_screen_resolution():
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def get_url(urlString, width, height):
    return f"{urlString}/{width}/{height}.jpg?random=1"

def download_file(url, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    return filename

def set_background(filename):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, filename, 0)

def get_user_acceptance():
    print("Do you want to set this as your desktop background? (y/n/q)")
    showPic.main(path, 100)
    user_input = input()
    if user_input.lower() == 'y':
        set_background(path)
    elif user_input.lower() == 'n':
        main()
    elif user_input.lower() == 'q':
        exit()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        get_user_acceptance()

def exit():
    print("Exiting...")
    time.sleep(1)
    quit()
        

def main():
    get_arg()
    width, height = get_screen_resolution()
    print(width, height)
    url = get_url(urlString, width, height)
    print(url)
    download_file(url, path)
    print(path)
    time.sleep(1)
    get_user_acceptance()

if __name__ == '__main__':
    main()


