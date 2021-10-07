from random import randint

"""

    Main function, called by main.py that generates the code, 
    and calls the solving method of choice.

"""

def mastermind(code_length, colors, guess_alg):

    #generates a random code
    code = [randint(0, colors-1) for i in range(0, code_length)]
    
    if(guess_alg == "minmax"):
        #generates a random first guess
        first_code = [randint(0, colors-1) for i in range(0, code_length)]
        nb_tries, code_found = minmax(code, code_length, colors, first_code)
        #sanity check
        if code_found != code:
            raise Exception("Ton code marche pas gros débile")
    
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

    Minmax method proceeeds as follow : 
        1) Produce all possibles codes, and let S* be the set of all possible codes,
           and S the set of possible winning codes, such as at step 1, S = S*
        2) Start with a code from S (1122 for original Mastermind )
        3) Play the guess to get a score : (right color, right color & position)
        4) If it is the right code, the game is won and the algorithm ends.
        5) Otherwise, remove from S* any code that would not give the same result if
           it was the secret code.
        6) Apply minmax technique to get the next guess, as follow :
            - For each unused guess in S, count how many elements of S*
              would lead to a certain score (x, y), for all possible scores.
            - Create a set which contains the guesses that lead to the minimum
              maximum number of elements left in S*
            - Take one of them (first one for determinism), and repeat from step 3.

"""


def minmax(code, code_length = 4, colors = 6, first_code = [0, 0, 1, 1]):

    nb_tries = 0

    #gestion des exceptions
    if len(code) != code_length:
        raise Exception("Secret code length does not match code length")
    if len(first_code) != code_length:
        raise Exception("First code length does not match code length")
    for i in range(len(code)):
        if code[i] > colors - 1:
            raise Exception("Secret code has too many colors")
        if first_code[i] > colors - 1:
            raise Exception("First code has too many colors")
    #generates all possible codes for this number of colors and length of code
    all_codes = generate_all_codes(code_length, colors)
    #S* set of possible winning codes
    winning_codes = list(all_codes)
    #list of tried codes
    failed_guesses = []
    #code to try
    code2try = first_code
    
    is_won = False;
    while(not is_won):
        result = test_guess(code2try, code, colors)
        nb_tries += 1
        if result[1] == code_length:
            is_won = True
        else:
            failed_guesses.append(code2try)
            #delete elements from S* that don't produce the same score
            i = 0
            while i < len(winning_codes):
                code_result = test_guess(code2try, winning_codes[i], colors)
                if code_result != result:
                    winning_codes.pop(i)
                else:
                    i += 1
            
            #TODO : commentary
            # find the next code to try
            minmax_value = -1
            minmax_set = []
            for guess in all_codes:
                already_tried = False
                for tried_code in failed_guesses:
                    if guess == tried_code:
                        already_tried = True
                        break
                
                if(not already_tried):
                    hit_count = \
                    [0 for i in range(int((code_length+1)*(code_length+2)/2))]
                    for g2 in winning_codes:
                        code_result = test_guess(guess, g2, colors)
                        index = code_result[1]*code_length \
                                - int(code_result[1]*(code_result[1]-1)/2) \
                                + code_result[1] + code_result[0]
                        hit_count[index] += 1
                        max_hit = len(winning_codes) - max(hit_count)
                        if max_hit > minmax_value:
                            minmax_value = max_hit
                            minmax_set = [guess]
                        elif max_hit == minmax_value:
                            minmax_set.append(guess)
            winning_in_minmax = find_common_elements(winning_codes, minmax_set)
            if len(winning_in_minmax) != 0:
                code2try = min(winning_in_minmax)
            else:
                code2try = min(minmax_set)

    return nb_tries, code2try

"""

    Generates all possible codes in a single list, where a code is represented as a list of
    digit between 0 and colors-1, and where the index of the code in the list also happens to 
    be the base 10 representation of the code

"""

def generate_all_codes(code_length, colors):
    L = []
    for i in range(pow(colors, code_length)):
        L.append(index2code(i, code_length, colors))
    return L

"""

    Two functions: 
        - code2index takes a code, aka a list of number between 0 and colors-1,
          and converts it to a base10 number, taking code[0] as the highest weight digit.

        - index2code realise the inverse operation.

"""

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

"""

    Tools

"""


def find_common_elements(list1, list2):
    L = []
    for x in list1:
        for y in list2:
            if x == y:
                L.append(x)
    return L
