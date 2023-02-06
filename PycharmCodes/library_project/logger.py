#log to log.txt file any loans
#class?
#just methods?

import json

def load_library_log():
    with open('/library_project/', 'w') as log:
        json.load("log.json")

#need to figre out how to get the return date of a certain book through the loan function
# maybe dict where key is book id and the date is one of the values in the ictonary that makes the value of the book id