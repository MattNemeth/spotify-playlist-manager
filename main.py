#grabs the first 10 liked songs for my account and prints them
#keeping this in .gitignore for now so I don't accidentally push my secret key to GH

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
                                               client_secret="",
                                               redirect_uri="https://127.0.0.1:9420",
                                               scope="user-library-read"))


"""

print("Printing out the last 10 tracks user has liked")
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

print()
print()


print('Printing out all playlists that user has created')
playlists = sp.current_user_playlists()
user_id = sp.me()['id']

for idx, item in enumerate(playlists['items']):
    pl = item['name']
    print(idx, pl)
    print('\tPlaylist ID: ', playlists['items'][idx]['id'])

print()
print()

pl_input = int(input("What playlist do you want? (Number): "))

pl_id = playlists['items'][pl_input]['id']
print('Printing out all tracks on playlist: ', pl_id)
#playlist_tracks() has a max song limit of 100 which isn't great when there is 500+ songs on the playlist. 
#hopefully can think of simple fix for this. Currently messing with the offset appears to be the only way
#but hopefully not
tracks = sp.playlist_tracks(pl_id, offset=0)

for idx, item in enumerate(tracks['items']):
    track = item['track']['name']
    print(idx, track)



"""





def show_tracks(results):
    for i, item in enumerate(results['items']):
        track = item['track']
        if i < 10:
            print("%d %s %55.32s %s" % (i, "", track['artists'][0]['name'], track['name']))
        else:
            print("%d %55.32s %s" % (i,     track['artists'][0]['name'], track['name']))


def check_duplicate(results, duplicates):
    for i, itemI in enumerate(results['items']):
        for j, itemJ in enumerate(results['items']):
            if (itemI['track']['name'] == itemJ['track']['name']) and (i != j):
                found = duplicates.append(itemI['track']['name'] + " by " + itemI['track']['artists'][0]['name'])
                return found


if __name__ == "__main__":
    #scope = 'playlist-read-private'
    #sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    playlists = sp.current_user_playlists()
    user_id = sp.me()['id']
    duplicates = []

    for playlist in playlists['items']:
        #if playlist['name'] == 'test':
        if playlist['name'] == 'You Know the Words':
            if playlist['owner']['id'] == user_id:
                print()
                print(playlist['name'])
                print('  total tracks', playlist['tracks']['total'])

                results = sp.playlist(playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                check_duplicate(tracks, duplicates)

                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
                    check_duplicate(tracks, duplicates)


                #printing out the duplicates found
                for i in duplicates:
                    print(i)

