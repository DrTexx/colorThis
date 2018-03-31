"""
colorThis by Denver P.

Simplification for Colorama
"""

# attempt to import colorama, otherwise raise an exception
try: import colorama # library used for colouring
except: print("Can't import colorama. Maybe it isn't installed? Maybe you're running 64-bit instead of 32-bit?")

try: # try to fix the escape sequences so they work in windows 10 console
    import os # used to allow win32 console to recognize ANSI/VT100 escape sequences
    os.system('') # stops formatting from appearing as "[41m[33m" and the like
except: raise Exception("couldn't apply fix for ANSI/VT100 escape sequence recognition under Win32 console in Windows 10")

def ct(string,**kwargs): # define main function
    ''' EXAMPLE: ct("hello",Back="RED") '''

    if 'autoReset' in kwargs: autoReset = kwargs['autoReset']
    else: autoReset=True
    
    if 'debug' in kwargs: debug = kwargs['debug']
    else: debug=False
    
    try: # attempt to run function as intended
        if(debug): print("kwargs:",kwargs) # print all kwards if debugging

        tempString = []
        
        keywords = ['Back','Fore','Style'] # list of classes from colorama that are recognized by this function
        
        for keyword in keywords: # for each keyword, do this
            if(debug): print("matching for keyword:",keyword)
            if keyword in kwargs: # if kwarg matches current keyword from list
                if(debug): print('colorama.%s.%s' % (keyword,kwargs[keyword]))
                tempString.append(eval('colorama.%s.%s' % (keyword,kwargs[keyword])))
        if not (string == ""): tempString.append(str(string)) # append the inputed string to the output list
        tempString.append(colorama.Fore.RESET)
        if(autoReset): tempString.append(colorama.Style.RESET_ALL) # append a style reset character to the end of the list
        if(debug): print(tempString)
        output = "".join(tempString) # convert the output array into a string
        return(output)
    except: # if function did not run as intended, return the string without formatting
        if (debug): print("something went wrong while running colorThis.ct()...")
        if (debug): print("returning a normal string...")
        return(string)

print(ct("hello",Back="RED", debug=True))

"""
def ctn(*args,**kwargs): # WIP revised version
    
    for my_list in args: # for each list encountered
        
        if type(my_list) == type(['test','list']):
            
            print("it's a list!")
            
            for my_item in my_list:
                
                if type(my_item) == type('a string'):
                    
                    print(my_item,'is a string!')
                    
                elif type(my_item) == type(Back='RED'):
                    
                    print(my_item,'is a keyword!')
"""

