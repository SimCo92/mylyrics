#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import models as mo


parser = argparse.ArgumentParser(description='Get the lyric of a song!!',
                                epilog="easy and fast!")
parser.add_argument('-a', '--artist', type=str,  
                    help='provide the artist name')
parser.add_argument('-l', '--lyric', type=str, 
                    help='provide the lyric title')
parser.add_argument('-p','--provider',
                    help='choose the provider, if not given will search both and return only one')
parser.add_argument('-s','--save', action='store_true',
                    help='save the output in result')
args = parser.parse_args()

provider = ["azlyrics", "elyrics"]
saveflag = False

artist = args.artist
title = args.lyric
if args.provider:
    provider = args.provider
if args.save:
    saveflag = args.save


if __name__ == '__main__':

    filename = mo.create_filename(artist,title)
    song = mo.Song(artist,title)

    if song.search_in_repo() == False  :

        if "azlyrics" in provider:
            try:
                print("Searching in AZlyrics...")
                obj = mo.Azlyrics(artist,title)
                print(obj.get_lyric())
                if saveflag:
                    obj.save()
            except:
                try:
                    print("Searching in Elyrics...")
                    obj = mo.Elyrics(artist,title)
                    print(obj.get_lyric())
                    if saveflag:
                        obj.save()
                except:
                    print("no results")
        else:
            try:
                obj = mo.Elyrics(artist,title)
                print(obj.get_lyric())
                if saveflag:
                    obj.save()
            except:
                print("no results")
    
    else:
        f = open(filename + ".txt", "r")
        print(f.read())