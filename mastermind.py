import sys
import computer
import human


def main():

    #default parameters value : 
    code_length = 4;
    colors = 6
    tries = 10
    players = 2
    cpu_only = True #TODO : change to False by default
    guess_alg = "minmax"    

    """
    Command line arguments :
        -c *number* : number of colors in game

        -l *number* : length of the code

        -t *number* : number of tries

        -p *arg*    : where arg is one of the following:
                        - 1p : 1 player guesses a random code
                        - 2p : 2 players against each other, default mode
                        - c  : a computer guess a random code
        
        -ca *arg*   : only when -p c is specified previously. Choose
                      the guessing method that the computer is going to use.
                      arg must be one of the following :
                        - aaa : default
                        - jsp : another guessing method

    """
    args = sys.argv[1: ]

    while len(args) > 0:

        if(args[0] == "-c"):
            args.pop(0)
            colors = args.pop(0)

        elif(args[0] == "-l"):
            args.pop(0)
            code_length = args.pop(0)

        elif(args[0] == "-t"):
            args.pop(0)
            tries = args.pop(0)

        elif(args[0] == "-p"):
            args.pop(0)
            if(args[0] == "1p"):    
                args.pop(0)
                players = 1;
            elif(args[0] == "2p"):
                args.pop(0)
                players = 2;
            elif(args[0] == "c"):
                players = 0;
                cpu_only = True
                args.pop(0)
            else:
                args.pop(0)
        
        elif(args[0] == "-ca"):
            args.pop(0)
            guess_alg = args.pop(0)
        
        else: args.pop(0)
    
    if(cpu_only):
        print(computer.mastermind(code_length, colors, guess_alg));
    else:
        human.mastermind(code_length, colors, tries, players)

    return 0

if __name__ == "__main__":
    main()