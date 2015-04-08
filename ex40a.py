class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def how_many_lines(self):
        print len(self.lyrics)

    def sing_me_a_sorted_song(self):
        for line in sorted(self.lyrics, reverse = True):
            print line

happy_bday = ["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"]

bulls_on_parade = ["They rally around tha family",
                        "With pockets full of shells"]

song_one = Song(happy_bday)
song_one.sing_me_a_song()
song_one.how_many_lines()
song_one.sing_me_a_sorted_song()

song_two = Song(bulls_on_parade)
song_two.sing_me_a_song()
song_two.how_many_lines()
song_two.sing_me_a_sorted_song()
