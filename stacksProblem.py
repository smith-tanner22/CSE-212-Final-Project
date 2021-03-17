backwards_sentence = [".", "sentence", "backwards", "a", "is", "This"] #our backwards sentence
forward_sentence = [] #our empty forward_sentence

print()
print("Here we have a backwards sentence that sounds almost like gibberish:")
print(backwards_sentence)
print()
print("Your goal is to make the sentence in the correct way and then type 's' to submit")
print()

command = None

while command != "q":
    print("Press q to quit, m to move the words, and s to submit.")
    command = input("What would you like to do? ")
    if command == "m": #moving from backwards_sentence to forward_sentence
        
        # Start coding here: *Hint might be helpful to use print statements.
        pass
    elif command == "s":
        if len(forward_sentence) == 6:
            print("Nice you did it!")
            quit()
        else:
            print("Nope that's not quite it! Try again!")
            quit()
quit()