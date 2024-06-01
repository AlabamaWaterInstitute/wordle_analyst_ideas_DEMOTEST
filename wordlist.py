"""
These words generated in a brainstorm session
as a list to test from.
"""
import random


def generate_words(num_words=10):
    """
    Generate a list of random words.
    """
    words = []
    for i in range(num_words):
        word = ""
        for j in range(5):
            word += random.choice("abcdefghijklmnopqrstuvwxyz")
        words.append(word)
    return words


wordlist = [
    "pizza",
    "write",
    "wards",
    "sword",
    "clean",
    "rides",
    "drive",
    "snort",
    "grunt",
    "spunk",
    "punks",
    "green",
    "trove",
    "zebra",
    "couch",
    "adieu",
    "sport",
    "bicep",
    "quick",
    "snoop",
    "quail",
    "queen",
    "quell",
    "pinto",
    "beans",
    "mouse",
    "speak",
    "table",
    "ebony",
    "bread",
    "other",
    "ranch",
    "calve",
    "water",
    "canoe",
    "kayak",
    "saint",
    "saved",
    "ladle",
    "lapel",
    "folly",
    "llama",
    "lucky",
    "truck",
    "their",
    "throw",
    "state",
    "stays",
    "march",
    "otter",
    "mourn",
    "rupee",
    "mates",
    "ruddy",
    "dates",
    "shame",
    "famed",
    "ollie",
    "stone",
    "bangs",
    "sings",
    "singe",
    "phone",
    "holly",
    "moldy",
    "dolly",
    "calls",
    "colic",
    "class",
    "smack",
    "dance",
    "fight",
    "light",
    "gaunt",
    "mauls",
    "malls",
    "trope",
    "guars",
    "glint",
    "ghost",
    "glass",
    "gloss",
    "goose",
    "gauze",
    "grime",
    "right",
    "wrong",
    "mines",
    "train",
    "trick",
    "trace",
    "guess",
]
wordlist += generate_words(100)

wordset = set(wordlist)
