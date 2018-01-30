#!/usr/bin/env python

import sys
import os

PHONEBOOK_ENTRIES = ".python_phonebook_entries"


def main():
    if len(sys.argv) < 2:
        exit(1)

    elif sys.argv[1] == "new":
        # YOUR CODE HERE #

    elif sys.argv[1] == "list":
        if not os.path.isfile(PHONEBOOK_ENTRIES) or os.path.getsize(
                PHONEBOOK_ENTRIES) == 0:
            print("phonebook is empty")
        else:
            # YOUR CODE HERE #

    elif sys.argv[1] == "remove":
        name = " ".join(sys.argv[2:4])
        # YOUR CODE HERE #

    elif sys.argv[1] == "clear":
        # YOUR CODE HERE #


if __name__ == "__main__":
    main()
