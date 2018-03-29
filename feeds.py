import feedparser
import sys
import os
import sound

def queue_last_episode(feed_number):
    feed = feeds[feed_number]
    episodes = feedparser.parse(feed).entries
    enclosures = [li['href'] for li in episodes[0].links if li['rel'] == 'enclosure']
    if len(enclosures) == 1:
        os.system("mpc add \"" + enclosures[0] + "\"")
    else:
        raise Exception("No enclosure for this rss feed.")

feeds = {
        0:  "http://radiofrance-podcast.net/podcast09/rss_10070.xml",   # Mauvais genres
        1: "",
        2: "",
        3: "http://feeds.feedburner.com/Odli",                          # Signé G
        4: "http://radiofrance-podcast.net/podcast09/rss_11549.xml",    # Sur les épaules de Darwin
        5: "http://radiofrance-podcast.net/podcast09/rss_14312.xml",    # La méthode scientifique
        6: "http://radiofrance-podcast.net/podcast09/rss_10212.xml",    # La tête au carré
        7: "http://radiofrance-podcast.net/podcast09/rss_10078.xml",    # Les pieds sur terre
        8: "http://radiofrance-podcast.net/podcast09/rss_10177.xml",    # La série documentaire
        9: "http://radiofrance-podcast.net/podcast09/rss_18081.xml",    # L'expérimentale
}
