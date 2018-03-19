#import colorama
#colorama.init()
#print(colorama.Back.RED + "RED BACK!" + colorama.Style.RESET_ALL)
#input()
from colorThis import ct

print("normal text")
print(ct("red background, yellow text",Back="RED",Fore="YELLOW"))
print("more normal text")
print("ONLY IN THE DEV BRANCH!")