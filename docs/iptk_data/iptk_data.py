from unidecode import unidecode
import re
from spellchecker import SpellChecker
import datetime

#Init spell checker
spell = SpellChecker()

class Normalize:
    def __init__(self):
        pass

    def normalize(self, data, encoding_type=None):
        
        data = self.encode(data, encoding_type)

        # Check data type
        data_type = self.find_data_type(data)

        # Decide action based on data type
        if data_type == 'str' or 'url':
            data = self.string(data, data_type)
        
        elif data_type == 'date':
            data = self.date(data)

        elif data_type == 'int':
            data = self.num(data)

        return data
    
    def encode(self, data, encoding_type):
        
        if not encoding_type:
            #Unidecode string
            data = unidecode(data)
        
        else:
            data = data.encode(encoding_type)

        return data

    def string(self, string, data_type):
        
        #Put all letters to lower case
        string = string.lower()
        
        #Remove Whitespace
        string = string.strip()

        #Remove punctuation if data_type is string
        if data_type == 'str':
            
            string = Clean.punctuation(string)

        return string
    
    def find_data_type(self, data):

        '''
        Uses regex and builtin .__class__ 
        to find and return type.
        '''
        #Check for URL
        regex = re.compile(r'https?://[^\s]+')
        match = re.match(regex, data)
        print(match)
        if match:
            data_type = 'url'
            return data_type

        # Check for data
        regex1 = re.compile(r'\d{4}-\d{1,2}-\d{1,2}')
        match1 = re.match(regex1, data)
        
        regex2 = re.compile(r'\d{8}')
        match2 = re.match(regex2, data)
        print(match1, match2)
        if match1 or match2:
            data_type = 'date'
            return data_type
        
        # Check for all other data types
        data_type = data.__class__.__name__
        return data_type
    
    def date(self, date):
        # Check if the date string is empty.
        if not date:
            return None
        
        # Remove punctuation
        date = Clean.punctuation(date)
        
        # Check if the date string is in the correct format.
        if len(date) != 8:
            return None

        # Convert the date string to a datetime object.
        date = datetime.datetime(
            year=int(date[:4]),
            month=int(date[4:6]),
            day=int(date[6:]))

        # Return the normalized date string.
        return date.strftime("%Y/%m/%d")
    
    def num(num):
        #CUSTOM NUMBER NORMALISATION FUNCTION HERE
        return num

    def flt(flt):
        #CUSTOM FLOAT NUMBER NORMALISATION FUNCTION HERE
        return flt
    
# PRESENT: A sub-class for data to be formatted in a consistent, publicly presentable format.

class Present(Normalize):
    
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
        title = self.string(title)

        #Split words to list
        words = title.split()
        
        '''
        #Spell check
        misspelled = spell.unknown(words)

        #Assume closest spelling is correct
        for word in misspelled:
            i = words.index(str(word))
            words[i] = spell.correction(word)
        '''

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

# CLEAN: A class for data to be cleaned  

class Clean:

    def punctuation(string):

        '''
        REMOVES PUNCTUATION FROM STRINGS

        ARGS: STRING TO BE CLEANED

        RETURNS: STRING WITH PUNTUCATION REMOVED
        '''

        string = re.sub(r"[^\w\s]", "", string)

        return string

