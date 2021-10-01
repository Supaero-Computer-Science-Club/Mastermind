import sys
from random import randint
from src import computer

def main():

    args = sys.argv[1: ]
    while len(args > 0):
        if(args[0] == "-c"):
            args.pop(0)
            colors = args.pop(0)

        elif(args[0] == "-l"):
            args.pop(0)
            code_length = args.pop(0)

        #number of starting codes to try
        elif(args[0] == "-t"):
            args.pop(0)
            n_start = args.pop(0)
        #number of codes per starting codes
        elif(args[0] == "-n"):
            args.pop(0)
            n_codes = args.pop(0)
        else:
            args.pop(0)

    #Creates n_start starting codes
    start_codes = [randint(0, colors-1) for i in range(code_length)]
    #Creates array to store results
    results = []
    for i in range(len(start_codes)):
        s_code = start_codes[i]
        results.append([])
        #Creates n_codes codes to crack
        secret_codes = [randint(0, colors-1) for i in range(code_length)]
        for code in secret_codes:
            (nbtries, code_found) = computer.minmax(code, code_length, colors, s_code)
            #sanity check
            if code_found != code:
                raise Exception("Fatal error, wrong code found")
            results[i].append([nbtries, code_found])
    
    return results




if __name__ == "__main__":
    main()