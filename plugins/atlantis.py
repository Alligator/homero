from util import hook
from atlantipsum import atlantipsum


@hook.command
def gate(inp):
    ".gate <character> <wordcount>. Characters include: McKay."
    characters = ['mckay']
    if inp.lower().split(' ')[0] in characters:
        count = None
        for x in inp.split():
            try:
                count = int(x)
            except ValueError:
                character = x.lower()
        r = atlantipsum.generate_sentence(character=character, word_count=count)
        return r
