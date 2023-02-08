#!/bin/bash

PHONEBOOK_ENTRIES="bash_phonebook_entries"


if [ "$#" -lt 1 ]; then
    exit 1

elif [ "$1" = "new" ]; then
    # YOUR CODE HERE #

elif [ "$1" = "list" ]; then
    if [ ! -e $PHONEBOOK_ENTRIES ] || [ ! -s $PHONEBOOK_ENTRIES ]; then
        echo "phonebook is empty"
    else
        # YOUR CODE HERE #
    fi

elif [ "$1" = "lookup" ]; then
    # YOUR CODE HERE #

elif [ "$1" = "remove" ]; then
    # YOUR CODE HERE #

elif [ "$1" = "clear" ]; then
    # YOUR CODE HERE #

else
     # YOUR CODE HERE #
fi
