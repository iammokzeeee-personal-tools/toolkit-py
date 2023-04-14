# IAMMOKZEEEE's Personal Tool Kit (IPTK) - PY

A series of modules IAMMOKZEEEE regularly uses in his own Python code.

## Dependencies

Info on dependencies here.

## iptk_data.py

This repo holds a collection of modules for data cleaning, manipulation and normalization used frequently in IAMMOKZEEEE's code.

### **class** Normalize
---

A class for normalising data, to allow for consistency and accuracy in data processing, manipulation and output.

The desire is for this class to hold at least three functions for typical functioning:

1. Normalize.string(*string*)
2. Normalize.num(*num*)
3. Normalize.flt(*flt*)

#### **def:** Normalize.string(*string*)

This function is to normalise string inputs. It does this by carrying out 3 actions on the input:
1. Putting all characters in the string into lower case. This allows py can accurately draw out comparisons between strings.
2. Removing all white space from the string input. This ensures strings are accurate and truly representative of the information they should hold.
3. Uni-decoding the string, to ensure the characters are all ASCII. This increases compatability, reduces file size and increases readability.

```
function here
```

#### **def:** Normalize.num(*num*)

*Note: this code is currently in production.*


This function is to normalise numbers.

```
function here
```

#### **def:** Normalize.flt(*flt*)

*Note: this code is currently in production.*

This function is to normalise floats.

```
function here
```

### **class** Present
---

Present is a class used to format output data, ready for reading. This allows for increased legibility, and more accurate and easy use beyond the applications.

*Note: Present is based on IAMMOKZEEEE's preferences **only**. As such, your preferences may vary and you may need to adjust your code accordingly.*

#### **def:** Present.title(*string*)

This function is an expands pythons built-in .title() function to increase readability and to ensure for a more grammatically-correct output. To do this, it performs several different actions:

1. It does not transform articles, conjunctions and prepositions into title case.
2. It checks the title for any mispellings.
3. It changes 'and' to '&' *only* if there is not an ampersand already in the title.

```
function here
```

#### **def:** Present.job_title(*string*)

*Note: this code is currently in production.*

This function is specifically designed to format an individuals job title. This achieves this through a variety of means:

- Unabbreviating commonly-used title abbreviations. *eg, turning 'CEO' into 'Chief Executive Officer'.*

- Abbreviating commonly-used title abbreviations. *eg, turning 'Information Technology' into 'IT'.*

```
function here
```


#### **def:** Present.name(*string*)

*Note: this code is currently in production.*

This function is specifically designed to format an individuals names. This is achieved by:

```
function here
```

### **class** Clean

*Note: this code is currently in production.*

## iptk_files.py