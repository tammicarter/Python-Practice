
# Printing multiLine strings using ''' '''
email_response = ''' 
Hi, User 
Thank you for testing out one of my 1st Python3 programs. 

I hope to see you in the neaer future, as I progress as a software engineer 😉! 

Graciously.
Tammi Ross
'''
print(email_response)

# Indexing strings using [] square bracket syntax - num starts at the end
email_response = "MultiLine Strings"
print(email_response[-2])

# Extract multiple characters using : inbetween requested index
email_response = "MultiLine Strings"
print(email_response[0:5])

# The interpreter assumes that the start index is 0 and the end is the length
# Using [] Brackets to duplicate a string like so: 
email_response = "MultiLine Strings"
another = email_response[:]
print(another)