from unidecode import unidecode
from spellchecker import SpellChecker

#Init spell checker
spell = SpellChecker()

class Normalize:

    def string(string):
        #Put all letters to lower case
        string = string.lower()
        
        #Remove Whitespace
        string = string.strip()
        
        #Unidecode string
        string = unidecode(string)
        
        return string
    
    def num(num):
        #CUSTOM NUMBER NORMALISATION FUNCTION HERE
        return num

    def flt(flt):
        #CUSTOM FLOAT NUMBER NORMALISATION FUNCTION HERE
        return flt
    


class Present:
    
    def __init__(self):

        #List of articles, conjunctions and prepositions 
        #not to be put into title case:
        self.title_exceptions = ['of', 
                    'and', 
                    'but', 
                    'or', 
                    'for', 
                    'yet', 
                    'so', 
                    'a', 
                    'an', 
                    'the']
        
    def title(self, title):

        #Normalize title
        title = Normalize.string(title)

        #Split words to list
        words = title.split()

        #Spell check
        misspelled = spell.unknown(words)

        #Assume closest spelling is correct
        for word in misspelled:
            i = words.index(str(word))
            words[i] = spell.correction(word)

        #Turn non-exception words in title case
        for word in words:

            #Find corresponding index of word in words list
            i = words.index(str(word))

            #If the word is 'and' and there are no ampersands in the words list, 
            #change the word to ampersand

            if word == 'and' and '&' not in words:
                words[i] = '&'

            #If the word is an exception, leave as lower case.
            if word in self.title_exceptions:
                continue

            #Otherwise, change to title case.
            else:
                words[i] = word.title()

        title = ' '.join(words)
        return title
    
    def job_title(self, job_title):
        return job_title

    def name(self, name):
        return name
    

class Present:
    
    def __init__(self):

        #List of articles, conjunctions and prepositions 
        #not to be put into title case:
        self.title_exceptions = ['of', 
                    'and', 
                    'but', 
                    'or', 
                    'for', 
                    'yet', 
                    'so', 
                    'a', 
                    'an', 
                    'the']
        
    def title(self, title):

        #Normalize title
        title = Normalize.string(title)

        #Split words to list
        words = title.split()

        #Spell check
        misspelled = spell.unknown(words)

        #Assume closest spelling is correct
        for word in misspelled:
            i = words.index(str(word))
            words[i] = spell.correction(word)

        #Turn non-exception words in title case
        for word in words:

            #Find corresponding index of word in words list
            i = words.index(str(word))

            #If the word is 'and' and there are no ampersands in the words list, 
            #change the word to ampersand

            if word == 'and' and '&' not in words:
                words[i] = '&'

            #If the word is an exception, leave as lower case.
            if word in self.title_exceptions:
                continue

            #Otherwise, change to title case.
            else:
                words[i] = word.title()

        title = ' '.join(words)
        return title
    
    def job_title(self, job_title):
        return job_title

    def name(self, name):
        return name