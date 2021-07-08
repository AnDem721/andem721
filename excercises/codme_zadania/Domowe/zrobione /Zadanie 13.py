wires = """
Kid, don't lose your cool
It's still too soon
To have to choose
A brighter doom
It's hard to believe, but I can see
How there could be
So little left to lose
(Cracking open skulls like cans of beans on Christmas Eve)

Mama's not okay
She lights a candle for every day
That you're away
Today could be the one
She burns the motherfucker down
Her final act of grace
In a pointless, endless race

Kid, you're under fire
Your life is coming down to the wire
Maybe you'll take the Captain's hand
Carry his ship through burning sands
Cradle your rifle like a man

Mama she says, "No way"
She's lost it all, so, you've got to stay
To make her pay
She knows the fiend upon the throne's
A goddamn sucker for the stone
Until the day he dies alone

Succumb... 
"""

clutch = """
First thing that I did, was buy a pack of smokes,
check in to a motel and consult my horoscope.
Sitting on the bed, with a briefcase in my hands,
patiently awaiting any word from my command

Telekinetic, dynamite
Psychic warfare is real
You better believe me brother
X-ray vision
Telekinetic prophetic dynamite
Psychic warfare is real
I know what you're thinking sister
X-ray vision

Next thing that I did, was tap out Morse code,
with a wooden nickel on the receiver on the phone.
Before I could complete it, I was quickly overtaken
by the angry spirits of Ronald and Nancy Reagan

Telekinetic, dynamite
Psychic warfare is real
You better believe me brother
X-ray vision
Telekinetic, prophetic dynamite
Psychic warfare is real
I know what you're thinking sister
X-ray vision

And on the drums, Gemini
On bass guitar, presenting, Pieces
On lead guitar, we have Aries
and on the microphone, Scorpio
Go

Last thing I remember, I was covered by the ruins,
I don't know who's to blame for that, but I know who didn't do it.
With every day that passes, it keeps on getting stranger,
but that really doesn't bother me, cause I get off on the danger.

Telekinetic, dynamite
Psychic warfare is real
You better believe me brother
X-ray vision
Telekinetic, prophetic dynamite
Psychic warfare is real
I know what you're thinking sister
X-ray vision

Telekinetic, dynamite
Psychic warfare is real
You better believe me brother
X-ray vision
telekinetic, prophetic dynamite
Psychic warfare is real
I know what you're thinking...
X-ray vision
"""
def to_set(title):
    wyjatki = ['"', "'s", "'ll", "(", ")"]
    przestanki = ["\n", ".","  ", ","]
    for wyjatek in wyjatki:
        title = title.replace(wyjatek, "")
    for znak in przestanki:
        title = title.lower().strip().replace(znak, " ")
    title = set(title.split(" "))
    title.remove("")
    return title

wires = to_set(wires)
clutch = to_set(clutch)

print(wires.intersection(clutch))
print(clutch.difference(wires))  # słowa jedynie w secie clutch
print(wires.difference(clutch)) # słowa jedynie w setcie wires

# print(wires)
# print(clutch)

