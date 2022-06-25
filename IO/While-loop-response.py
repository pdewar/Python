# A user is asked to input Y or n in response to a question.
# Write a loop to repeatedly prompt the user input to supply 
# a valid response. The loop should end when the  user supplies
# a valid response.

response = input("What is your response? (y/n) ")
while not (response == "y" or response == "n"):
    response = input("Invalid! Please type 'y' or 'n': ")

if __name__ == "__main__":
    print("Your valid response is", response)