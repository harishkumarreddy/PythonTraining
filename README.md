# PythonTraining
Python training code base

### List of Classes and Topics
1.  [Demo](/Python%20for%20Data%20bricks%20(2).pdf)
2.  [Python Intro](/Python%20for%20Data%20bricks-demo.pdf)
3.  [Data Types](/DataTypes)  
4.  [Operators](/Operators)
5.  [Conditions](/Conditions)
6.  [Loops](/Loops)
7.  [Functions](/Functions)
8.  [Algorithms](/Algorithms)
9.  [RegEx](/#regex)



## RegEx:
```
Character	Description
\A	        Returns a match if the specified characters are at the beginning of the string	"\AThe"
\b	        Returns a match where the specified characters are at the beginning or at the end of a word
            (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain" r"ain\b"
\B	        Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
            (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain" r"ain\B"
\d	        Returns a match where the string contains digits (numbers from 0-9)	"\d"
\D	        Returns a match where the string DOES NOT contain digits	"\D"
\s	        Returns a match where the string contains a white space character	"\s"
\S	        Returns a match where the string DOES NOT contain a white space character	"\S"
\w	        Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
\W	        Returns a match where the string DOES NOT contain any word characters	"\W"
\Z	        Returns a match if the specified characters are at the end of the string	"Spain\Z"

```

```
Set	        Description
[arn]	    Returns a match where one of the specified characters (a, r, or n) are present
[a-n]	    Returns a match for any lower case character, alphabetically between a and n
[^arn]	    Returns a match for any character EXCEPT a, r, and n
[0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present
[0-9]	    Returns a match for any digit between 0 and 9
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case

[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

```

```
Function	Description
search	      Returns a Match object if there is a match anywhere in the string
findall	      Returns a list containing all matches
split	      Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
```



---
Author : [Harishkumar Reddy](harishkumerreddy.cherla@gmail.com)
