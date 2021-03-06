import requests
import sys


# Fetch songs with spotify api
class Pytifylib:
    # Api url
    url = 'https://api.spotify.com/v1/search?q=%s&type=track,artist'

    # hold songs
    _songs = {}

    # Hold "I Feel Lucky" Song.
    _song = {}

    # history
    _history = []

    # limit output songs
    _limit = 15

    # Search for song / album / artist

    #Search fills songs with response JSON
    #All we have to do is automate getting the FIRST thing.
    def search(self, query):
        try:
            search = '+'.join(query.split())

            try:
                response = requests.get(self.url % search)
            except requests.exceptions.Timeout:
                response = requests.get(self.url % search)
            except requests.exceptions.TooManyRedirects:
                print('Something wrong with your request. Try again.')

                return False
            except requests.exceptions.RequestException as e:
                print(e)
                sys.exit(1)

            self._history.append(query)

            self.set_songs(data=response.json())

            return True
        except StandardError:
            print('Search went wrong? Please try again.')

            return False

    def set_songs(self, data):
        for index, song in enumerate(data['tracks']['items']):
            if index == self._limit:
                break

            if sys.version_info >= (3, 0):
                artist_name = song['artists'][0]['name'][:25]
                song_name = song['name'][:30]
                album_name = song['album']['name'][:30]
            else:
                artist_name = song['artists'][0]['name'][:25].encode('utf-8')
                song_name = song['name'][:30].encode('utf-8')
                album_name = song['album']['name'][:30].encode('utf-8')

            self._songs[index + 1] = {
                'href': song['uri'],
                'artist': artist_name,
                'song': song_name,
                'album': album_name
            }
            _song = data['tracks']['items'][0];


    def get_song(self):
        return self._song

    def get_songs(self):
        return self._songs

    # List all. Limit if needed
    def list(self):
        list = []
        space = '{0:3} | {1:25} | {2:30} | {3:30}'

        list.append(space.format('#', 'Artist', 'Song', 'Album'))

        # Just to make it pwitty
        list.append(space.format(
            '-' * 3,
            '-' * 25,
            '-' * 30,
            '-' * 30
        ))

        for i in self.get_songs():
            list.append(space.format(
                '%d.' % i,
                '%s' % self.get_songs()[i]['artist'],
                '%s' % self.get_songs()[i]['song'],
                '%s' % self.get_songs()[i]['album']
            ))

        return list

    def _get_song_uri_at_index(self, index):
        if len(self._songs) != 0:
            return str(self._songs[index]['href'])
        else:
            print("No song has been found related to this pattern.")
            exit(2)

    def _get_song_name_at_index(self, index):
        return str('%s - %s' % (self._songs[index]['artist'], self._songs[index]['song']))

    def listen(self, index):
        raise NotImplementedError()

    def print_history(self):
        if len(self._history) > 5:
            self._history.pop(0)

        print('\nLast five search results:')

        for song in self._history:
            print(song)

    def next(self):
        raise NotImplementedError()

    def prev(self):
        raise NotImplementedError()

    def play_pause(self):
        raise NotImplementedError()

    def pause(self):
        raise NotImplementedError()
