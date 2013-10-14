import os
import pickle
import random
import argparse


_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data(path):
    return os.path.join(_ROOT, 'data', path)


def generate_sentence(character=None, word_count=None):
    lines = load_pickle(character)

    if not word_count:
        return random.choice(lines)['text']

    potential_matches = [line for line in lines if line['word_count'] == word_count]

    if potential_matches:
        return random.choice(potential_matches)['text']
    else:
        if word_count == 1:
            pass
        # recursive callback, trying on less word each time.
        return generate_sentence(word_count - 1)


def load_pickle(character):
    f = open(get_data('%s.pickle' % character))
    return pickle.load(f)


def main():
    parser = argparse.ArgumentParser(description='Generate Stargate Atlantis quotes.')
    parser.add_argument('-c', '--character', dest='character', type=str, help='Character to generate quote.')
    parser.add_argument('-w', '--words', dest='word_count', type=int, help='Minimum number of words.')

    args = parser.parse_args()

    print generate_sentence(args.character, args.word_count)


if __name__ == '__main__':
    main()