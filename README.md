# wordle-cheat

Are you tired of being beat at the wordle game? Worry no more since now you can guess the words like a pro.

This python script tells you which words to guess next and it's always right.

Run it from the command line with python3 cheat.py. You have to have the wordlist named words.txt in the same directory as the python script.

## Usage

Once you get a word from the script enter it into wordle. Next you enter the indexes of letters which were green or yellow. Indexes range from 0 to 4.
You can seperate the indexes with spaces commas, or you don't have to seperate them at all. Once you  get a new word enter it again untill you got it!

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
