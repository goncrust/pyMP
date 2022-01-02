# pyMP
**Python Music Downloader**

## Installation

### Requirements

- python (3 or above)
- yt-dlp (fork of youtube-dl)
- youtube-search-python
- ffmpeg

### Step by step

1. Install [python 3](https://www.python.org/)
1. Install the required python librarys:
    - `pip install yt-dlp`
    - `pip install youtube-search-python`
1. Clone the repo: `git clone https://github.com/goncrust/pyMP.git`
1. Go to the directory: `cd pyMP`
1. Run: `python3 src/main.py`

## Usage

```
usage: python3 src/main.py [mode] [options] [...]

modes:
	D			Download mode.
	Q			Query mode.

options:
	-h			Displays this help message.
	-k <keyword>		Keyword for query (also works with D mode).
	-s <number>		Query size (default: 5).
	-u <URL>		URL for download.
	-p <URL>		URL for playlist download.
	-o <output file>	 Set destination file name and location.
```

## License

The source code is licensed under the open source GPL v3.0. License is available [here](https://github.com/goncrust/pyMP/blob/master/LICENSE.md).
