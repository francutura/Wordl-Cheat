# wordle-cheat

Are you tired of being beat at the wordle game? Worry no more since now you can guess the words like a pro.

This python script tells you which words to guess next and it's always right.

Run it from the command line with python3 cheat.py. You have to have the wordlist named words.txt in the same directory as the python script.

## Usage

```
usage: cheat.py [-h] [--hard]

Wordle cheater - command line program to help you
choose the next word for the game wordle

optional arguments:
  -h, --help  show this help message and exit
  --hard      Enable hard mode play
```

Once you get a word from the script enter it into wordle. Next you enter the indexes of letters which were green or yellow. Indexes range from 0 to 4.
You can seperate the indexes with spaces commas, or you don't have to seperate them at all. Once you  get a new word enter it again untill you got it!


## How it works

Here are the number of occurences of each letter in all English 5 letter words

```
  "s": 3033,
  "e": 3009,
  "a": 2348,
  "o": 1914,
  "r": 1910,
  "i": 1592,
  "l": 1586,
  "t": 1585,
  "n": 1285,
  "d": 1181,
  "u": 1089,
  "c": 964,
  "p": 955,
  "y": 886,
  "m": 843,
  "h": 810,
  "b": 715,
  "g": 679,
  "k": 596,
  "f": 561,
  "w": 505,
  "v": 318,
  "x": 139,
  "z": 135,
  "j": 89,
  "q": 53
```

We use this and a simple heuristic tracking all the letters used so far to determine the word to use next.
The best first word to use is AROSE since it's a valid English word and its letters are the most common so you have the highest chance to guess some. The frequency table is rebuilt after every guess and subsequent optimal words are printed on the screen

## Example

This is from day 215

```
:$ python3 cheat.py
Use this word next: arose
Which letters are green? (letters go from 0 to 4)
Which letters are yellow? (letters go from 0 to 4) 1,2

Use this word next: yourn
Which letters are green? (letters go from 0 to 4) 1
Which letters are yellow? (letters go from 0 to 4) 3

Use this word next: torch
Which letters are green? (letters go from 0 to 4) 1
Which letters are yellow? (letters go from 0 to 4) 0 2

We are down just to 10 or less words!
motor, robot, rotor
Use this word next: motor
Which letters are green? (letters go from 0 to 4) 13
Which letters are yellow? (letters go from 0 to 4) 24

DONE! the word is robot
```

![Wordle example image](https://github.com/francutura/wordle-cheat/blob/main/day_215_img.png?raw=true)

Have fun!
