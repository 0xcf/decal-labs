## Scripting Lab Assignment

You'll be completing a classic first shell scripting assignment: make a phonebook.

Write a shell script `phonebook` which has the following behavior:

* `./phonebook new name number` adds an entry to the phonebook.
and
* `./phonebook name` displays the name and phone number associated with that name.

* `./phonebook list` displays every entry in the phonebook (in no particular order). If the phonebook has no entries, display `phonebook is empty`

* `./phonebook remove name` deletes the entry associated with that name.

* `./phonebook clear` deletes the entire phonebook.

For example,
```
$ ./phonebook new Linus Torvalds 101-110-0111
$ ./phonebook Linus Torvalds
Linus Torvalds 101-110-1010
$ ./phonebook new Tux Penguin 555-666-7777
$ ./phonebook list
Linus Torvalds 101-110-1010
Tux Penguin 555-666-7777
$ ./phonebook remove Linus Torvalds
$ ./phonebook list
Tux Penguin 555-666-7777
$ ./phonebook clear
$ ./phonebook list
phonebook is empty
```

Here's the kicker: **You have to implement this same functionality in both `bash` and `python`.** This is to help illuminate the strengths and weaknesses
of each language in the context of writing a simple CLI application.

Some tips to make things easier:
* `bash` has an append operator `>>` which, as you might guess, appends its second operand to the file passed in as the first operand.
```bash
$ cat foobar.txt
foobar
$ echo "hello, reader" >> foobar.txt
$ cat foobar.txt
foobar
hello, reader
```
* Remember that you can simply write to and read from a file to persist data
* Recall that `bash` exposes its command line arguments through the `$<integer>` positional parameters

```bash
#!/bin/bash
# contents of argscript.sh

echo "$1"
echo "$2"
```
```bash
./argscript.sh foo bar
foo
bar

```

* In `bash`, single quotes `''` preserve the literal value of the characters
they enclose. Double quotes `""` preserve the literal value of all characters
except for `$`, backticks \`\`, and the backslash `\\`.

* In `python`, you can interact with command-line arguments through the `sys.argv` list
```python
#!/usr/bin/python
# contents of argscript.py

import sys
print(sys.argv[1])
print(sys.argv[2])
```
```bash
$ ./argscript.py foo bar
foo
bar

```

* `python` lets you manipulate files with the `open` function, commonly used with the `with` control structure
```python
#!/usr/bin/python
# contents of fileman.py

with open('./newfile.txt', 'w') as f:
    f.write("hello from python\n")
    
```

```bash
$ python fileman.py
$ cat newfile.txt
hello from python

```

[13]: https://www.gnu.org/software/bash/manual/html_node/Redirections.html
[14]: https://github.com/0xcf/decal-utils/blob/master/checkoff
* [Here][13] you can read more about `bash` redirections
* [Here][14] you can see `python` used in a system administration context to implement the checkoff script used for this class
