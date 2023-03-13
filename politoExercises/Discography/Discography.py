import re

#read artist.txt and create a dictionary with key name of other files and value the code
def readArtist():
    dict = {}
    with open("Discography/artists.txt") as file:
        for line in file.readlines():
            array = line.strip().split(";")
            dict[array[1]] = array[0]
    return dict

#this function read each file that is decribed in artist dict 
# for each of them create ore append into actual dictionary created (named song)
# according to the year key, other dict with name the song name as the artist the aartist code 
def readSongs():
    songs = {}
    artists = readArtist()
    for key in artists.keys():
        with open("Discography/{}".format(key)) as file:
            for line in file.readlines():
                array = line.strip().split(";")
                if array[0] in songs:
                    songs[array[0]].append({"name":array[1] , "artist":artists[key]})
                else :
                   songs[array[0]] = [{"name":array[1] , "artist":artists[key]}]  
        file.close()
    return songs


def main():
    songs = readSongs()
    # sort the dictionary according to year key that after conveted to touple using .items()
    # means the first el of touple  
    sortedSongs =dict(sorted(songs.items(), key= lambda x : x[0]))
    for key , value in sortedSongs.items():
        print("{0}:".format(key))
        for el in value: 
            print("{:35s} {}".format(el["name"] , el["artist"]))


if __name__== "__main__" :
    main()
