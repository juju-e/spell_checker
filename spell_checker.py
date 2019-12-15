from spellchecker import SpellChecker
from termcolor import colored
import time


print(colored("  ___  ___  ____           ___             ","yellow"))
print(colored(" /    |   | |     |   |   |    |   |  | / ","yellow"))
print(colored("|___  |___| |__   |   |   |    |___|  |*  ","yellow"))
print(colored("____) |     |__   |__ |__ |__/ |   |  | \ ","yellow"))
time.sleep(0.8)

spell=SpellChecker()

words_to_spellcheck=input(colored("[*]enter the words you want to spell check------->","blue"))

words_to_spellcheck=words_to_spellcheck.split()

possibly_misspelled=spell.unknown(words_to_spellcheck)

for index,word in enumerate(possibly_misspelled):
    if word in spell:
        pass
    else:
        print(colored("[#]-----$ ","blue"))
        print(colored(word+" is misspelled ","red"))
        print(colored("processing...**"))
        time.sleep(0.98)
        print(colored("The best spelling is[*]------> "+spell.correction(word),"green"))
        print(colored("here are the other candidates[*]-----> "+str(spell.candidates(word)),"blue"))
        for a in range(len(words_to_spellcheck)):
            if words_to_spellcheck[a].lower()==word.lower():
               words_to_spellcheck[a]=spell.correction(word)

print(colored("Here is the entire corrected sentence","green"))
print(" ".join(words_to_spellcheck))


