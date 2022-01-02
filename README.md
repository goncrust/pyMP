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
1. Install the required python libraries:
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
	-o <output file>	 Set destination file name and location (default: current/working directory, filename=video's title.mp3).
```

### Examples

- Be prompted to select a video from youtube search to download: `python3 src/main.py D -k duality -o "~/Music/Slipknot-Duality.mp3"`
- Download directly from a video's url: `python3 src/main.py D -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ"`
- Download a playlist: `python3 src/main.py D -p "https://www.youtube.com/watch?v=cwp9ojsvAus&list=PLU6YJ-jFUEF4EAoUeBkWac1di0W2fNT1_" -o ~/Music/simbiose/`

## License

The source code is licensed under the open source GPL v3.0. License is available [here](https://github.com/goncrust/pyMP/blob/master/LICENSE.md).
