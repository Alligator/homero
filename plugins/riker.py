from util import hook
from rikeripsum import rikeripsum

@hook.command
def riker(inp):
    r = rikeripsum.generate_sentence()
    if 'p' in inp:
        r = rikeripsum.generate_paragraph()  
    return r
