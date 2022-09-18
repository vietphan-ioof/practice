import re

#Case INsensitive Matching

# This says how if you dont care about lower case and uppercase in the

robocop = re.compile(r'robocop', re.I) # re.I also means re.IGNORECASE
print(robocop.search('Robocop is part man, part machin, all cop').group)



#Subbing strings with the sub() method


namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')


# If you only want to censor the names of the secret agents

















#Managing Complex Regexes

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)