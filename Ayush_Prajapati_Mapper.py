#!/usr/bin/env python

import sys
import json
from collections import Counter

def parse_json():
    song_counter = Counter()
    artist_counter = Counter()
    
    for line in sys.stdin:
        try:
            entry = json.loads(line)
            song_name = entry.get('song', None)
            artist_name = entry.get('artist', None)
            if song_name: 
                song_counter[song_name] += 1
            if artist_name:
                artist_counter[artist_name] += 1
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}", file=sys.stderr)

    for song, count in song_counter.items():
        print(f"Song {song}\t{count}")
    
    for artist, count in artist_counter.items():
        print(f"Artist {artist}\t{count}")

if __name__ == "__main__":
    parse_json()
