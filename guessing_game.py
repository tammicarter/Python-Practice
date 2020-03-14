''' Andy reference 
'''

secret_number = 3
guess_count = 0
guess_limit = 3
# conditions set
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
# the : lets you know that a condition is happening if true do this 
    if guess == secret_number:
# do this 
     print("You Won")
# this causes the parsing to stop the loop     
     break
else: 
    print ("Sorry, you only had 3 tries, but none were correct")