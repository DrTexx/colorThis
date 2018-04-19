"""
colorThis by Denver P.

Adapted implementation of Colorama
"""

import os # used to allow win32 console to recognize ANSI/VT100 escape sequences
os.system('') # stops formatting from appearing as "[41m[33m" and the like
#except: raise Exception("couldn't apply fix for ANSI/VT100 escape sequence recognition under Win32 console in Windows 10")
    
# attempt to import colorama
coloramaImported = False
try:
    import colorama # library used for colouring
    coloramaImported = True
except:
    pass

def ct(my_string,**kwargs): # define main function
    ''' EXAMPLE: ct("hello",Back="RED") '''
    func_kws = {'debug': False,'autoReset': True,'showErrors': True} # List of keywords that change how this function executes
    styleKWs = ['Back','Fore','Style'] # list of classes from colorama that are compatible with this function
    
    # If the debug keyword is found in kwargs, set it accordingly
    for func_kw in func_kws: # for each keyword we can process
        if(func_kw in kwargs): # check if it's in the kwargs parsed and
            func_kws[func_kw] = kwargs[func_kw] # change the local keyword value if a parsed keyword value is found

    debug=func_kws['debug'];autoReset=func_kws['autoReset'];showErrors=func_kws['showErrors']
    
    if(debug): print("{:-<12}: {}".format('all kwargs',kwargs)) # print all kwargs if debugging
    
    tempString = []
    
    def printTempString(): # Function to print the value of tempString in a formatted manner
        if(debug): print("{:-<12}: {}".format('tempString',tempString)) # Print what tempString looks like so far
    
    if (coloramaImported): # if colorama imported successfully
        if(debug): print("colorama was successfully imported!")
        
        for kwarg in kwargs: # for each kwarg parsed
            if(debug): print("{:-<16}: [{}] {}: [{}]".format('kwarg',kwarg,'value',kwargs[kwarg]))
            
            if kwarg in styleKWs: # if the kwarg is a styling keyword
                if(debug): print('{:-<20}: [colorama.{}.{}] compatible, will be added to string'.format('class',kwarg,kwargs[kwarg]))
                
                tempString.append(eval('colorama.%s.%s' % (kwarg,kwargs[kwarg]))) # append the colorama class to the list
            
            elif kwarg in func_kws: # otherwise if it's a function keyword, ignore it
                if(debug): print('{:-<20}: {} is known to be a function keyword, not a styling keyword. Ignoring...'.format('class',kwarg))
                
                pass
            
            else: # else raise an error and state the keyword is incompatible (only if showing errors)
                if(showErrors): raise Exception('{} is not a compatible keyword'.format(kwarg))
            
        if(debug): print("{:-<16}: [{}]".format('my_string',my_string))
        
        if not (my_string == ""): # If my_string isn't empty
            if(debug): print("{:-<16}: string isn't empty, appending it".format('my_string'))
            
            tempString.append(str(my_string)) # append the inputed string to the output list
        else:
            if(debug): print("{:-<16}: string is blank! nothing appended.".format("my_string"))
            
            pass
        
        if(debug): print("{:-<16}: {}".format('autoReset',autoReset))
        
        if(autoReset): # if autoReset is enabled
            if(debug): print("{:-<16}: {}".format('autoReset','appending reset character'))
            
            tempString.append(colorama.Style.RESET_ALL) # append a style reset character to the end of the list
        else:
            if(debug): print("{:-<16}: {}".format('autoReset','autoReset disabled. nothing appended.'))
            
            pass
        
        if(debug): print("{:-<16}: {}".format('my_string',"joining into a single colour-formatted string"))
        
        output = "".join(tempString) # convert the output array into a string
    
        if(debug): print("{:-<20}: {}".format('my_string',"returning final colour-formatted string"))
        
        return(output)
    
    else:
        if(showErrors): print("colorama could not be imported... maybe it isn't installed? Maybe you're running 64-bit instead of 32-bit?")
        if(showErrors): print("returning a normal string...")
        return(my_string)
    
def ct_hex(my_string,hex_color,**kwargs):
    if 'autoReset' in kwargs:
        autoReset = kwargs['autoReset'] # store value if found in kwargs
    else:
        autoReset=True # set default value if not found
    
    r, g, b = [int(hex_color[i:i+2], 16) for i in range(1, len(hex_color), 2)]
    out = "\x1b[38;2;{};{};{}m{}".format(r,g,b,my_string)
    if(autoReset): out = out + str(ct('',Style="RESET_ALL"))
    return(out)
    #hex_color = '#f57c00'
    # thanks to Ican for his answer on stackoverflow: https://stackoverflow.com/a/41063750/5619653

def ct_rgb(my_string,r,g,b):
    return("\x1b[38;2;{};{};{}m{}{}".format(r,g,b,my_string,ct('',Style="RESET_ALL")))

print(ct("defined colour",Fore="RED"))
print("normal text")
print(ct_hex("hex colour!",'#f57c00'))
print("normal text")
print(ct_rgb("rgb colors",255,0,0))
print("normal text")

import time
def ct_grad(char='.',duration=1,instances=16,time_div_dec_places=8):
    x = 1
    while(x < 255):
        time.sleep(round(duration/instances,time_div_dec_places))
        print(ct_rgb(char,0,x,0),end='',flush=True)
        x += int(255/instances)
    return('')
        
print(ct_grad('.',1,16))
print("HEHELLO")
print("HEHELLO")