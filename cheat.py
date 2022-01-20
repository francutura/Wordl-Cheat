import string
import argparse


def create_score_map(words):
    """Creates a score map for each word.
    Depending how common it's letters are
    the score is greater.

    Args:
        words (list): List of words

    Returns:
        list: Sorted list of possible words
    """
    frequency = {}
    scores = []
    for letter in string.ascii_lowercase:
        frequency[letter] = 0

    for word in words:
        for letter in word:
            frequency[letter] += 1

    for word in words:
        word_score = 0
        for letter in set([letter for letter in word]):
            word_score += frequency[letter]
        scores.append((word, word_score))

    return sorted(scores, key=lambda x: -x[1])


def load_words(path):
    """Load the wordlist.

    Args:
        path (str): path to wordlist

    Returns:
        list: list of loaded words
    """
    with open(path) as f:
        words = f.readlines()
    return [word.strip().lower() for word in words]


def find_optimal_word(scores, used_letters):
    """Find the optimal world to use next.
    The word is found having in mind the currently
    used letters as well as how common its letters
    are.

    Args:
        scores (Tuple): (str, int) word and word score tuple
        used_letters (set): set of letters used so far

    Returns:
        str: optimal word to try next
    """
    new_scores = []
    for entry in scores:
        word = entry[0]
        score = entry[1]
        letter_score = 0
        for letter in word:
            if letter in used_letters:
                letter_score += 1
        new_scores.append((word, score, letter_score))

    return sorted(new_scores, key=lambda x: (x[2], -x[1]))[0][0]


def letters_in_words(words):
    """Return set of letters found
    in a list of words

    Args:
        words (list): list of words

    Returns:
        set: set of letters
    """
    letters = set()

    for word in words:
        for letter in word:
            letters.add(letter)

    return letters


def run(hard=False):
    """Run main guesser.
    Two modes avaliable hard mode or normal.
    Represents the same modes as wordle modes.

    Args:
        hard (bool, optional): Is the game in hard mode?. Defaults to False.
    """
    words = load_words("./words.txt")
    working_words = words.copy()
    used_letters = set()
    ten_or_less = False

    while True:

        if not hard:
            avaliable_letters = letters_in_words(words)
            working_words = list(
                filter(
                    lambda x: set(letter for letter in x).union(avaliable_letters)
                    == avaliable_letters,
                    working_words,
                )
            )
            scores = create_score_map(working_words)
        else:
            scores = create_score_map(words)

        optimal_word = find_optimal_word(scores, used_letters)

        print(f"Use this word next: {optimal_word}")

        green = input("Which letters are green? (letters go from 0 to 4) ")
        yellow = input("Which letters are yellow? (letters go from 0 to 4) ")
        print()

        green = [
            int(num)
            for num in green
            if num in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        ]

        yellow = [
            int(num)
            for num in yellow
            if num in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        ]

        green_letters = set(optimal_word[index] for index in green)
        yellow_letters = set(optimal_word[index] for index in yellow)

        if optimal_word in words:
            words.remove(optimal_word)

        # leave words that have letters at the green positons
        for index in green:
            words = list(filter(lambda x: x[index] == optimal_word[index], words))

        # remove words that dont have gray letters
        # or have yellow letters at that position
        for index in range(len(words[0])):
            if index in green:
                continue
            if index in yellow:
                words = list(filter(lambda x: x[index] != optimal_word[index], words))
            else:
                if (
                    optimal_word[index] in green_letters
                    or optimal_word[index] in yellow_letters
                ):
                    continue
                words = list(filter(lambda x: optimal_word[index] not in x, words))

        # leave words that have yellow letters in them
        for index in yellow:
            words = list(filter(lambda x: optimal_word[index] in x, words))

        if len(words) == 1:
            print(f"DONE! the word is {words[0]}")
            exit(0)

        if len(words) == 0:
            print("Uh... something went wrong. I have no words left :(")
            exit(1)

        if len(words) <= 10 and not ten_or_less:
            print("We are down just to 10 or less words!")
            ten_or_less = True

        if ten_or_less:
            print(", ".join(words))

        for letter in optimal_word:
            used_letters.add(letter)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Wordle cheater - command line program to help you choose the next word for the game wordle"
    )
    parser.add_argument(
        "--hard", default=False, action="store_true", help="Enable hard mode play"
    )
    parsed = parser.parse_args()

    run(parsed.hard)
