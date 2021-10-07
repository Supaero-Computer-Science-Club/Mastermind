# Mastermind in Python

Mastermind implemented on Python.

Works on Python 3.9 +

Currently only the computer solver has been implemented.

Future version will had single and two player modes.

To run the solver, run mastermind.py:

```console
python mastermind.py
```

## Command line arguments

The script can take the following arguments:

```console
-l code_length -c number_colors -t number_tries -p gamemode -ca solving_algorithm
```

Where gamemode is one of :

* 1p : 1 player guesses a random code
* 2p : 2 players against each other, default mode
* c  : a computer guess a random code, default value

*solving_algorithm* is only avaible if gamemode is set to c, and must be one of:

* minmax : default algorithm

For example, this command:

```console
python mastermind.py -c 8 -l 6
```

Will solve a random code of 8 colors, of length 6.

By default, arguments are as follow:

```console
python mastermind.py -l 4 -c 6 -t 10 -p c -ca minmax
```
