from random import randint

"""

    Main function, called by main.py that generates the code, 
    and calls the solving method of choice.

"""

def mastermind(code_length, colors, guess_alg):

    #generates a random code
    code = [randint(0, colors-1) for i in range(0, code_length)]

    if(guess_alg == "default"):
        nb_tries = brute_force(code, colors)
    
    return nb_tries

def test_guess(guess, good_code, colors):
    l = len(good_code)
    result = [0, 0]
    #teste les occurences de couleurs
    colors_good  = [0 for i in range(colors)]
    colors_guess = [0 for i in range(colors)]
    for i in range(l):
        if guess[i] == good_code[i]:
            result[1] += 1
        else:
            colors_good[good_code[i]] += 1
            colors_guess[guess[i]]    += 1
    
    for i in range(colors):
        if colors_good[i] <= colors_guess[i]:
            result[0] += colors_good[i]
        else:
            result[0] += colors_guess[i]

    return result


"""

    Default method proceeeds as follow : 
        - Produce all possibles codes, S
        - test 1 code (1122)
        - Remove from S any code that would not give the same result if
        it was the secret code
        - For each unused guess (not limiting to S), 

"""


def brute_force(code, colors):

    nb_tries = 0
    winning_result = [1 for i in range(colors)]
    #generates all possible codes

    all_codes = generate_all_codes(len(code), colors)
    code_test = []; #choix arbitraire
    result = test_guess(code, code_test)
    nb_tries += 1
    if result == generate_all_codes:
         return 1;
    return nb_tries

def generate_all_codes(code_length, colors):
    L = []
    for i in range(pow(colors, code_length)):
        L.append(index2code(i, colors, code_length))
    return L

def code2index(code, colors):
    b = len(code)
    exp = 1
    s = 0
    for i in range(b):
        s += code[b - i - 1]*exp
        exp *= colors

    return s

def index2code(index, code_length, colors):
    a = index
    L = [None for i in range(code_length)]
    for i in range(code_length):
        (a, b) = divmod(a, colors)
        L[code_length - i - 1] = b
    return L


