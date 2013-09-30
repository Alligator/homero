from util import hook
from treksum import treksum


@hook.command
def trek(inp):
    ".trek <character> <wordcount>. Characters include: Picard, Riker, Data, Worf, Geordi, Barclay, Q, Pulaski, Computer, Guinan, Troi, Beverly and Wesley. "
    characters = ['picard', 'riker', 'data', 'worf', 'geordi', 'barclay', 'q', 'pulaski', 'computer', 'guinan', 'troi', 'beverly', 'wesley']
    if inp.lower().split(' ')[0] in characters:
        count = None
        for x in inp.split():
            try:
                count = int(x)
            except ValueError:
                character = x
        r = treksum.generate_sentence(word_count=count, character=character)
        return r
