Pytify
=============

### Original Repo
https://github.com/bjarneo/Pytify

<br>
Start songs from command line.<br>
Should work in Linux and OS X. (As far as I know.)<br>
Supports both Python 2 and 3. <br>

Just run 'pytify "Artist" "Song"' or 'pytify "Artist" "Album"' or whatever and hopefully
you typed it right :). It's like a Google I Feel Lucky for Spotify in the Terminal.

### Note
I Just made this for myself, I can't guarantee it will work for someone else, at 
any rate it works on a Debian/Ubuntu system.


## Installation
```bash
$ git clone https://github.com/AustinRF2918/pytify.git
$ cd pytify
$ sudo python setup.py install
```

### Usage
```bash
# To use I Feel Lucky mode, just type
$ pytify "artist" "song"
# To use Search mode, type
$ pytify "artist" "song" -l
```

### Dependency
```bash
pip install requests
```

### Contributing
Contributions are appreciated.

### Contributors
- [@joined](https://github.com/joined/) - OS X
- [@adam410](https://github.com/adam410/) - OS X issue
- [@Newky](https://github.com/Newky) - Better structure
- [@ymski](https://github.com/ymski) - OS X
- [@wohlfea](https://github.com/wohlfea) - Made it compatible with python 3.5
