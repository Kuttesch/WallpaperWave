# WallpaperWave

WallpaperWave is a Python project that allows users to automatically download and set a random image as their desktop wallpaper.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Bugs](#bugs)
- [Future Features](#future-features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install WallpaperWave, you need to clone the repository and install the necessary Python libraries. Here are the steps:

```bash
git clone https://github.com/Kuttesch/WallpaperWave.git
cd WallpaperWave/src
pip install -r requirements.txt
```

## Usage

After installation, you can run the script by simply typing the following command in your terminal:

```bash
python main.py
```

## Features

- Automatically checks the screen resolution.
- Downloads a random image from the [PicSum API](https://picsum.photos/).
- Sets the downloaded image as the desktop wallpaper.
- Allows user to accept or reject the selected image.

## Bugs

Currently, there are no known bugs. If you encounter any issues, please open an issue in the GitHub repository.

## Future Features

- Add support for multiple operating systems.
- Allow users to specify the image category.
- Add a GUI with [Django](https://www.djangoproject.com/) with [React](https://reactjs.org/)
- Or a TUI with [Curses](https://docs.python.org/3/library/curses.html).
  - Not sure if this is the way to go, but it could be a nice feature.
  - Could add a feature to save the image to a specific folder.
  - Could add a feature to download multiple images and select one from them.
- Add installscript like in [SysInfo](https://github.com/kuttesch/SysInfo), one of my other projects.
- Add a feature to download multiple images and select one from them.
  - Could be added through the mentioned GUI/TUI.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)