# Write you a skybot plugin #
Say you want to write yourself a skybot plugin or something. For no particular reason you want it to always remind people that someone called 'sponge' is an idiot. There are three ways to do this:

## Create a command ##
You could create a .sponge command that replies to whoever called it with 'sponge is an idiot'.

    from util import hook

    @hook.command
    def sponge(inp):
        return 'sponge is an idiot'

Easy isn't it? The function decorator `hook.command` takes either a function name, or the following function and turns it into a command. The follwing would be functionally equivalent to the previous example:
    
    @hook.command('sponge')
    def sponge_command(inp):
        return 'sponge is an idiot'

Both create a new command, called sponge.

Whatever string you return from your function will be the reply to the calling user, that is, if I called the command skybot would say something like 'alligator: sponge is an idiot'.

### Function arguments ###
Let's talk about function arguments. Command functions only need one argument, which passes the text sent with the command to the function. If I say '.sponge is a baby', the value of inp is 'is a baby'.

We can also specify optional default parameters to get useful things.

Say I wanted the calling channel and the calling user's nick in my plugin, I could do this:

    def sponge(inp, input=None):
        nick = input['nick']
        return 

So, what is this input parameter? Let's examine it.

### Input Objects ###

`input` is a dictionary containing lots of useful things, all of which are shown below.

#### bot ###
The current bot object.

#### chan ###
The current channel (i.e. the one the command was called from).

#### command ###
The IRC command (if you're using input within a command function this will probably be 'PRIVMSG').

#### conn ###
The current IRC connection object.

#### host ###
The calling user's hostname.

#### inp ###
The input to the command.

#### inp_unstripped ###
The input to the command without the whitespace stripped.
    
#### input ###
The input object (yes the one you're currently looking at).

#### lastparam ###
The actual message used to call the command (the .command isn't removed).

#### me ###
A function that takes a string and sends it to the current channel as an IRC action (like /me in most clients).

#### msg ###
I'm honestly not sure. It seems to be exactly the same as lastparam.

#### nick ###
The calling user's nick.

#### notice ###
Works like `me`, but sends the string as an IRC notice.

#### paraml ###
A list, usually of the form [nick, lastparam] or [chan, lastparam] depending on the context.

#### params ###
The same as the above, but formatted as a string 'user :lastparam'.

#### pm ###
Works like `me`, but sends the string as a private message to the user.

#### prefix ###
The user's whole nick (nick, prefix, realname and hostname) as a string.

#### raw ###
The raw IRC command..

#### reply ###
Works like `me`, except replies to the user with the string passed in the current channel.
    
#### say ###
Works like `me`, except simply says the passed string in the current channel.

#### server ###
The current IRC server.

#### set_nick ###
A function to change the bot's nick. Takes a string.

#### trigger ###
The thing that triggered the command. Usually the name of the command.

#### user ###
The user (prefix + realname) that called the commands.

**Important note**: All of the above properties in `input` can be used on their own, by specifying their name as the default paramter, for exmaple:

    def sponge(inp, nick=None):

Now let's look at that bot object in a little more depth.
    
#### Bot Objects ####
The bot object has tons o stuff in it and I rarely find a need for it, but here's a list of some cool stuff:

#### bot.commands ###
A dict of the current commands, where bot.commands['sponge'] would return the sponge function linked to that command.

#### bot.config ###
The current config, stored exactly as it looks in the config file.
    
#### bot.conns ###
A dict of the current IRC connection objects. There are their own thing that I'm not going into here.

#### bot.events ###
A dict of the currently hooked events.

#### bot.plugs ###
A dict of the currently loaded plugins.

So that's about it for commands. Let's move on to events.

## Hook an event ##

If we wanted the bot to remind everyone that sponge is an idiot every time the user named 'sponge' said anything, we could hook an event.

    from util import hook

    @hook.event('PRIVMSG')
    def sponge_event(paraml):
        return 'sponge is an idiot'

This will say 'sponge is an idiot' after every IRC message, in the channel that particular message came from. Probably not a good idea, so lets just make this happen in reply to sponge.

    @hook.event('PRIVMSG')
    def sponge_event(paraml, nick=None):
        if nick == 'sponge':
            return 'sponge is an idiot'

We can use all of the default parameters we could with hook.command, except unlike `hook.command` the only required argument gets the value of `paraml` instead of `inp`.

We can pass any IRC event to `hook.event`, including event numbers, such as those shown [here](http://www.mirc.net/raws/). We can also pass more that one event, using spaces to separate them.

In one of my own plugins I wanted to hook the topic changing and the TOPIC message received when joining a channel, so I used `@hook.event('TOPIC 332')`.

That's about it for events. Simple.

## Regex Hooks ##
The last way to hook is using a regular expression. This will search the message text (*just* the message text, we can't use regex to look for particular channels or nicks) for the given regex and fire the event whenever it matches.

    @hook.regex('sponge')
    def sponge_regex(match, input=None):
        return 'sponge is an idiot'

This function will get called any time the word 'sponge' is mentioned. Much like the other hooks, we have access to the input object but this time our required parameter. This is a python re match object, as documented [here](http://docs.python.org/library/re.html#match-objects).

The arguments to `hook.regex` are passed directly to the `re.search` function (docs [here](http://docs.python.org/library/re.html#re.search)), meaning we can pass flags like `re.I` for case insensitivity too.

Well that's about it. I'm gonna go eat a gat damn sandwhich now im hungry as shit what the heck.
