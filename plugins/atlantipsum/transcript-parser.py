import os
import pickle
import argparse
from bs4 import BeautifulSoup

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data(path):
    return os.path.join(_ROOT, 'data', path)


def fetch_transcripts(character):
    dialog = []
    for season in range(1, 6):
        directory = 'data/transcripts/%s' % season
        for episode in os.listdir(directory):
            print episode
            transcript = parse_dialog(season, episode, character)
            dialog.extend(transcript)

    f = open(get_data('%s.pickle' % character.lower()), 'wb')
    pickle.dump(dialog, f)
    f.close()


def parse_dialog(season, episode, character):
    dialog = []
    source = BeautifulSoup(open('data/transcripts/%s/%s' % (season, episode)).read().replace('<br />', ' ').replace('\n', ''))
    for x in source.find_all('blockquote'):
        if x.text.startswith(character):
            line = {}
            line['text'] = x.text[len(character):].strip()
            line['word_count'] = len(line['text'].split())
            dialog.append(line)

    return dialog


def main():
    parser = argparse.ArgumentParser(description='Parse Stargate Atlantis transcripts.')
    parser.add_argument('-c', '--character', dest='character', type=str, help='Character to parse dialog for.')
    args = parser.parse_args()

    print fetch_transcripts(args.character.upper())


if __name__ == '__main__':
    main()

# Season 1 episode 1/2 transcripts are identical.
# Season 2 missing episodes 12-20.
# Season 3 missing episode 20.