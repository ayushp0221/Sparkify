#!/usr/bin/env python

import sys
from collections import Counter

new_song_counter = Counter()
new_artist_counter = Counter()

for line in sys.stdin:

    try:
        # Split the input line into song/artist and count
        item, count = line.strip().split('\t')
        count = int(count)

        # Check if the item is a song or an artist
        if item.startswith('Song'):
            new_song_counter[item] += count
        elif item.startswith('Artist'):
            new_artist_counter[item] += count
    except ValueError:
        # Skip lines with incorrect format
        continue

# Combine the counters from all inputs
new_song = dict(new_song_counter)
song_sorted = sorted(new_song.items(), key=lambda item: item[1], reverse=True)

new_artist = dict(new_artist_counter)
artist_sorted = sorted(new_artist.items(), key=lambda item: item[1], reverse=True)

# Output the sorted song and artist counts
for song, count in song_sorted:
    print(f"{song}\t{count}")

for artist, count in artist_sorted:
    print(f"{artist}\t{count}")
