
import pandas as pd
import numpy as np

song_dataset_main = pd.read_csv("dataset/songs_final_2.csv")
artist_dataset_main = pd.read_csv("dataset/artists_final_2.csv")

# Dictionaries ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

artist_rating_dic = {
"Breaking Benjamin":10,
"Black Sabbath":10,
"Candlemass":10,
"Cannibal Corpse":9,
"Death":10,
"Iron Maiden":8,
"Judas Priest":8,
"Drake":0,
"Taylor Swift":0,
"Katy Perry":0,
"deadmau5":1,
"Bruno Mars":0,
"Metallica":8,
"Megadeth":9,
"Slayer":7,
"Rammstein":7,
"Foo Fighters":7,
"The Offspring":8,
"Green Day":7,
"Linkin Park":8,
"Evanescence":7,
"Nevermore":8,
"Pantera":8,
"Sabaton":7,
"System of a Down":9,
"Avenged Sevenfold":7,
"Wolfgang Amadeus Mozart":0,
"Johann Sebastian Bach":0,
"Yaşlı Amca":0,
"Goom Gum":0,
"Ghost":7
}

song_rating_dic = {
"0faXHILILebCGnJBPU6KJJ":(9,"Breaking Benjamin","The Diary of Jane - Single Version"),
"2yXyz4NLTZx9CLdXfLTp5E":(10,"Breaking Benjamin","I Will Not Bow"),
"10ASBwZsp7oUUDsJEYz3uS":(10,"Breaking Benjamin","Dance With The Devil")
}


# Utility Functions -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Returns True if given artist exists. Case Sensitive!
def existsArtist(search):
    for index, row in artist_dataset_main.iterrows():
        artist = row['artist']
        if(artist==search):
            return True
    return False

# Returns True if given song name exists for given artist. Case Sensitive!
def existsSongName(searchArtist,searchSong):
    for index, row in song_dataset_main.iterrows():
        song = row['track_name']
        artist = row['artist_1']
        if(artist==searchArtist):
            if(song==searchSong):
                return True
    return False

# Returns True if given songid exists. Case Sensitive!
def existsSongID(search):
    for index, row in song_dataset_main.iterrows():
        songid = row['track_id']
        if(songid==search):
            return True
    return False

# Return all artists matching given string sorted by maximum song popularity.
def searchArtists(search):
    artists = artist_dataset_main.copy(deep=True)
    artists = artists[artists['artist'].str.contains(search, case=False)]
    artists = artists[['artist','songs','max_pop','avg_pop']]
    artists = artists.sort_values(by=['max_pop'], ascending=False)
    return artists

# Return all songs matching given string sorted by popularity.
def searchSongs(search):
    songs = song_dataset_main.copy(deep=True)
    songs = songs[songs['track_name'].str.contains(search, case=False)]
    songs = songs[['track_id','track_name','artist_1','popularity']]
    songs = songs.sort_values(by=['popularity'], ascending=False)
    return songs

# Return all songs matching a given artist sorted by popularity.
def searchArtistSongs(search):
    songs = song_dataset_main.copy(deep=True)
    songs = songs[songs['artist_all'].str.contains(search, case=False)]
    songs = songs[['track_id','track_name','artist_all','popularity']]
    songs = songs.sort_values(by=['popularity'], ascending=False)
    return songs


# Command Functions -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# List all artists matching a search string
def com_search_artists():
    print_fun("\tSearch Artists: ")
    search = get_string_input("Artist Name> ")
    artists = searchArtists(search)
    if(artists.empty):
        print_fun("No Artists Found")
    else:
        print_fun(artists.to_string(index=False))

# List all artists matching a search string
def com_search_songs():
    print_fun("\tSearch Songs: ")
    search = get_string_input("Song Name> ")
    songs = searchSongs(search)
    if(songs.empty):
        print_fun("No Songs Found")
    else:
        print_fun(songs.to_string(index=False))

# List all songs by a given primary artist. Case Sensitive!
def com_search_artist_songs():
    print_fun("\tSearch Artist Songs: ")
    search = get_string_input("Artist Name> ")
    songs = searchArtistSongs(search)
    if(songs.empty):
        print_fun("No Songs Found")
    else:
        print_fun(songs.to_string(index=False))

# List all records in the artist rating dictionary.
def com_list_artist_ratings():
    print_fun("\tList Artist Ratings:")
    sorted_artist_rating_dic = dict(sorted(artist_rating_dic.items(), key=lambda item: item[0]))
    for i in sorted_artist_rating_dic:
        text = '\t {} : {}'.format(i,sorted_artist_rating_dic[i])
        print_fun(text)

# List all records in the song rating dictionaries.
def com_list_song_ratings():
    print_fun("\tList Song Ratings:")
    sorted_song_rating_dic = dict(sorted(song_rating_dic.items(), key=lambda item: item[0]))
    for i in sorted_song_rating_dic:
        text = '\t{}, {} : {}'.format(sorted_song_rating_dic[i][1], sorted_song_rating_dic[i][2], sorted_song_rating_dic[i][0])
        print_fun(text)

# Clears the artist rating dic
def com_clear_artist_ratings():
    print_fun("\tClear Artist Ratings")
    artist_rating_dic.clear()
    print_fun("\tArtist ratings deleted\n")

# Clears the song rating dic
def com_clear_song_ratings():
    print_fun("\tClear Song Ratings")
    song_rating_dic.clear()
    print_fun("\tSong ratings deleted\n")

def com_rate_artist_name():
    print_fun("\tRate Artist By Name: ")
    artist = get_string_input("Artist Name> ")
    if existsArtist(artist):
        rating = get_int_input("Rating(1-10)> ")
        artist_rating_dic[artist] = rating
        print_fun("Rating Saved")
    else:
        print_fun("ERROR: Artist not Found")

def com_rate_song_name():
    print_fun("\tRate Song By Name: ")
    artist = get_string_input("Artist Name> ")
    if existsArtist(artist):
        songs = searchArtistSongs(artist)
        song = get_string_input("Song Name> ")
        songs = songs[songs['track_name'].str.contains(song, case=False)]
        count = len(songs.axes[0])
        if (count > 1):
            print_fun("ERROR: Multiple Songs. Use 'RateSongID'")
            print_fun(temp.to_string())
        elif (count < 1):
            print_fun("ERROR: Song not found")
        else:
            print_fun(songs.to_string())
            rating = get_int_input("Rating(1-10)> ")
            print_fun(songs['track_id'].head(1))
            song_rating_dic[songs['track_id'].head(1)] = (rating,songs['artist_all'].head(1),songs['track_name'].head(1))
            print_to_console("Rating Saved")
    else:
        print_fun("Artist not Found")
        print_fun("")

def com_rate_song_id():
    pass

# Console Functions -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Take a string input from command line
def get_string_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            return user_input
        except ValueError:
            print("Invalid - Enter a string")

# Take a int input from command line
def get_int_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid - Enter an integer")

# Take a float input from command line
def get_float_input(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Invalid - Enter a float")

# arbitrary print function for later
def print_fun(str):
    print(str)


# Main --------------------------------------------------------------------------------------------
if __name__ == "__main__":

    while True:
        user_input = get_string_input("Com> ")

        if user_input.lower() == "searchartists":
            com_search_artists()

        if user_input.lower() == "searchsongs":
            com_search_songs()

        if user_input.lower() == "searchartistsongs":
            com_search_artist_songs()

        if user_input.lower() == "listartistratings":
            com_list_artist_ratings()

        if user_input.lower() == "listsongratings":
            com_list_song_ratings()

        if user_input.lower() == "clearartistratings":
            com_clear_artist_ratings()

        if user_input.lower() == "clearsongratings":
            com_clear_song_ratings()

        if user_input.lower() == "rateartist":
            com_rate_artist_name()

        if user_input.lower() == "ratesong":
            com_rate_song_name()

        if user_input.lower() == "ratesongid":
            com_rate_song_id()

        if user_input.lower() == "updateartistmodel":
            updateArtistModel()

        if user_input.lower() == "updatesongmodel":
            updateSongModel()

        if user_input.lower() == "pap":
            print(artistpred)

        if user_input.lower() == "psp":
            print(songpred)

        if user_input.lower() == 'recartists':
            recArtists(25)

        if user_input.lower() == 'recsongs':
            recSongs(25)

        if user_input.lower() == "exit":
            print("Exiting Program")
            break
