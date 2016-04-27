#!/usr/bin/env python
from __future__ import absolute_import
import pytify.pytifylib
from pytify.strategy import get_pytify_class_by_platform
from pytify.menu import Menu
import argparse
import sys
import curses
import re


class App:
    def __init__(self):
        self.IFL = True;
        self.pytify = get_pytify_class_by_platform()()
        self.run()

    def toggleIFL(self):
        self.IFL = False

    def menu(self, list):
        self.list = list
        curses.wrapper(self.menu_items)

    def menu_items(self, stdscreen):
        curses.curs_set(0)

        main_menu = Menu(self.list, stdscreen, self.IFL)
        main_menu.display()

    def run(self):
        parser = argparse.ArgumentParser(description='Spotify remote')
        #Removing these to focus on pure, english words instead of arguments,
        #which I see as slightly unelegant: I want flags to represent modifiers
        #and words to represent commands.

        #parser.add_argument('-n', help='for next song', action='store_true')
        #parser.add_argument('-p', help='for previous song', action='store_true')
        #parser.add_argument('-pp', help='for play and pause song', action='store_true')
        #parser.add_argument('-s', help='stop music', action='store_true')

        #Our actual modifiers.
        parser.add_argument('artist', nargs='?')
        parser.add_argument('album', nargs='?')
        parser.add_argument('-c', help='Shows original creators', action='store_true')
        parser.add_argument('-d', help='Shows debug informations.', action='store_true')
        parser.add_argument('-l', help='Shows list of songs instead of IFL', action='store_true')


        #Make sure they didn't put more than 3 things in.
        #Done before we ever parse.

#          # HACKY #3333333333333333
        if len(sys.argv) > 4:
            print("Non-parseable state")
            exit(2)
#          # HACKY #3333333333333333

        #CL Arguments
        args = parser.parse_args()

        
        #Our simple little debug flag :)
        if args.d:
            debug = True;
        else:
            debug = False;

        #Show the introduction text originally introduced
        #With this.
        if args.c:
            self.intro();

        state = self.parseExpected(debug)
        if state != 0:
            data = self.getParseableData(debug)
        else:
            print("Non-parseable state")
            exit(1);

        listString = ''

        for i in data:
            listString += ' '
            listString += i

        if not args.l:
            if listString != '':
                search = self.pytify.search(listString)
                if search is not False:
                    self.menu(list=self.pytify.list())
            else:
                print("You didn't enter anything...")
        else:
            self.toggleIFL()
            if listString != '':
                search = self.pytify.search(listString)
                if search is not False:
                    self.menu(list=self.pytify.list())
            else:
                print("You didn't enter anything...")




        #if args.n:
        #    self.pytify.next()

        #elif args.p:
        #    self.pytify.prev()

        #elif args.pp:
        #    self.pytify.play_pause()

        #elif args.s:
        #    self.pytify.stop()

        #else:
        #    self.interaction()

    def intro(self):
        print('################################################')
        print('#         ____ _  _ ____ __ ____ _  _          #')
        print('#        (  _ ( \/ (_  _(  (  __( \/ )         #')
        print('#         ) __/)  /  )(  )( ) _) )  /          #')
        print('#        (__) (__/  (__)(__(__) (__/           #')
        print('#                 by bjarneo                   #')
        print('#    <http://www.github.com/bjarneo/Pytify>    #')
        print('################################################')

    def getParseableData(self, debug):
        programName = sys.argv[0];
        parsedFlags = []
        parsedFuzzy = []

        #It works :)

        #Parsing through all our flags with our regex that I made below.

        #Hack, puts our program name in so we don't have to
        #Take that into account when we get the complimentary
        #Set.
        parsedFlags.append(sys.argv[0])

        for i in range(len(sys.argv)):
            #Use similar regex parse to below.
            currentParse = re.findall(r"(-.*)", sys.argv[i])
            #Append it to oru list.
            if len(currentParse) != 0:
                parsedFlags.append(sys.argv[i])

        for i in range(len(sys.argv)):
            #Get the subset of what we just got.
            #Im sure there is a way more efficent way to do this.
            if sys.argv[i] in parsedFlags:
                if debug:
                    print("Already in parsedFlags")
            else:
                parsedFuzzy.append(sys.argv[i])
                if debug:
                    print("Placing in parsedFuzzy.")

        if debug:
            print("Parsed Fuzzy Data:")
            print(parsedFuzzy)

        return parsedFuzzy

    def parseExpected(self, debug):
        #Flag numeric to keep number of all our flags.
        flags = 0
        state = 0;

        #State 0 is non-parseable
        #State 1 is song
        #State 2 is song and artist or album and artist
        #State 3 is song, artist, album fuzzy find.
        #State 4 is fail state.

        for i in range(len(sys.argv)):
            currentParse = re.findall(r"(-.*)", sys.argv[i])
            #Regex to parse current argument that checks if it is a flag.
            if len(currentParse) != 0:
                flags = flags + 1

        if debug == True:
            print("Amount of flags found: " + str(flags))

        if len(sys.argv) ==  flags + 1:
            if debug == True:
                print("No arguments added: How am I supposed to know what to play?.")
            state = 0; #I know its repetitive.
        elif len(sys.argv) == flags + 2:
            if debug == True:
                print("One argument added: Assuming song.")
            state = 1; #Song
        elif len(sys.argv) == flags + 3:
            if debug == True:
                print("Two argument added: Assuming artist and song, or artist and album.")
            state = 2; #Artist/Song or Arist/Album
        elif len(sys.argv) == flags + 4:
            if debug == True:
                print("I'll try to fuzzy find this as a permutation of artist, song, and album")
            state = 3 #Fuzzy.
        else:
            state = 4 #Bad State.

        return state

    def interaction(self):
        self.intro()

        while 1:
            if sys.version_info >= (3, 0):
                search_input = input('What artist / song are you searching for?\n> ')
            else:
                search_input = raw_input('What artist / song are you searching for?\n> ')

            if search_input:
                search = self.pytify.search(search_input)

                if search is not False:
                    self.menu(list=self.pytify.list())


def main():
    try:
        App()

    except KeyboardInterrupt:
        print('\n Closing application...\n')
