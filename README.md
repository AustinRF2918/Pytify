Pytify
=============

Search and start songs from command line.<br>
Should work in Linux and OS X.<br>
Supports both python 2 and 3. <br>

Just run 'pytify "Artist" "Song"' or 'pytify "Artist" "Album"' or whatever and hopefully
you typed it right :). It's like a Google I Feel Lucky for Spotify in the Terminal.


## Installation
```bash
$ sudo pip install pytify
```

## Or clone the repo
```bash
$ git clone https://github.com/bjarneo/pytify.git
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
