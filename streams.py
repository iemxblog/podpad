import os

def queue_stream(stream_number):
    os.system("mpc add \"" + streams[stream_number] + "\"")

streams = {
        0: "http://webradio-preprod.tamm-kreiz.bzh:8000/airtime_128m",              # Canalbreizh
        1: "http://direct.franceinter.fr/live/franceinter-midfi.mp3",               # France Inter
        2: "http://direct.franceculture.fr/live/franceculture-midfi.mp3",           # France Culture
        3: "http://cdn.nrjaudio.fm/audio1/fr/30401/mp3_128.mp3?origine=fluxradios"  # Rire et chansons
}
