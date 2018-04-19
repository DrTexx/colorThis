#import colorama
#colorama.init()
#print(colorama.Back.RED + "RED BACK!" + colorama.Style.RESET_ALL)

from colorThis.colorThis import ct

while(True):
    print()
    test_to_run = input("Which test would you like to run? [normal,autoReset,showErrors,speed,exit]: ")
    if(test_to_run=='normal'):
        print("normal text")
        print(ct("red back, yellow text! :)",Back="RED",Fore="YELLOW"))
        print("more normal text")
    
    # TESTING AUTORESET FUNCATIONALITY
    elif(test_to_run=='autoReset'):
        print(ct("YELLOW FROM HERE",Back='YELLOW',autoReset=False))
        print("a regular print")
        print("another regular print")
        print(ct("I DEMAND NO YELLOW!",Style='RESET_ALL',autoReset=False))
        print("another another regular print")
    
    # TESTING FOR ERRORS
    elif(test_to_run=='showErrors'):
        print(ct("DON'T SHOW ME ERRORS!",Back="YELLOW",Fore="RED",StrangerDanger="oh jeez",showErrors=False)) # Ignore errors, just return the string best you can
        print(ct("TELL ME IF SOMETHING IS WRONG! (DEFAULT)",Back="YELLOW",Fore="RED",StrangerDanger="oh jeez")) # Notify of errors (default behaviour)
    # TESTING FOR SPEED
    elif(test_to_run=='speed'):
        for i in range(100):
            print(ct("STRING #{}".format(i),Back='RED',Fore='WHITE'))
    # EXIT TESTING SUITE
    elif(test_to_run=='exit'):
        break
    else:
        print("that's not a valid test name")
    