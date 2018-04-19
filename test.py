#import colorama
#colorama.init()
#print(colorama.Back.RED + "RED BACK!" + colorama.Style.RESET_ALL)

from colorThis import colorThis

while(True):
    print()
    test_to_run = input("Which test would you like to run? [normal,autoReset,showErrors,speed,hex,rgb,exit]: ")
    
    # TESTING GENERAL FUNCTIONALITY
    if(test_to_run=='normal'):
        print("normal text")
        print(colorThis.ct("red back, yellow text! :)",Back="RED",Fore="YELLOW"))
        print("more normal text")
        
    # TESTING AUTORESET FUNCATIONALITY
    elif(test_to_run=='autoReset'):
        print(colorThis.ct("YELLOW FROM HERE",Back='YELLOW',autoReset=False))
        print("a regular print")
        print("another regular print")
        print(colorThis.ct("I DEMAND NO YELLOW!",Style='RESET_ALL',autoReset=False))
        print("another another regular print")
        
    # TESTING FOR ERRORS
    elif(test_to_run=='showErrors'):
        print(colorThis.ct("DON'T SHOW ME ERRORS!",Back="YELLOW",Fore="RED",StrangerDanger="oh jeez",showErrors=False)) # Ignore errors, just return the string best you can
        print(colorThis.ct("TELL ME IF SOMETHING IS WRONG! (DEFAULT)",Back="YELLOW",Fore="RED",StrangerDanger="oh jeez")) # Notify of errors (default behaviour)
        
    # TESTING FOR SPEED
    elif(test_to_run=='speed'):
        for i in range(100):
            print(colorThis.ct("STRING #{}".format(i),Back='RED',Fore='WHITE'))
            
    # EXIT TESTING SUITE
    elif(test_to_run=='exit'):
        break
        
    # HEX TEST
    elif(test_to_run=='hex'):
        my_hex = str(input('please enter a hexadecimal color (e.g. #f57c00): '))
        print(colorThis.ct_hex("HEXADECIMAL COLOURED TEXT!",my_hex))
        
    elif(test_to_run=='rgb'):
        inputInvalid = True
        while(inputInvalid):
            my_rgb = str(input('please enter 3 values between 0 and 255 for R,G and B respectively (e.g. 212, 154, 106): '))
            my_rgb_list = []
            try:
                [my_rgb_list.append(x.strip()) for x in my_rgb.split(',')]
                r = int(my_rgb_list[0])
                g = int(my_rgb_list[1])
                b = int(my_rgb_list[2])
                inputInvalid = False
                print('{}={};{}={};{}={}'.format('r',r,'g',g,'b',b))
                print(colorThis.ct_rgb("RGB COLOURED TEXT!",r,g,b))
            except:
                print("please enter 3 comma separated numbers between 0 - 255")
                
    else: # test to run matches none of the previous if/elif statements
        print("that's not a valid test name")
        