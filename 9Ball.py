# Import random module using the import keyword
import random
# Create a function say codeMagic_8ball() (Which is used to Implement the main logic of the magic 8 ball program)
def codeMagic_8ball():
    # Give the response you want as user input using the input() function and 
    # store it in a variable
    User_response = input("Enter any key for answer and 'quit' to exit:")
    # Give the list of all eight ball answers and store it in another variable
    Magic_8ball_answers = [
        "BtechGeeks platform for all type of articles",
        "Python Programs for in depth articles about Python Language",
        "SheetTips for Articles about excel and google sheets",
        "PythonArray",
        "Hello Good Morning",
        "This is BtechGeeks",
        "This is PythonPrograms",
        "Refer Excel Articles on SheetTips"
        ]
    # Check if the obtained/input response is "quit" using the if conditional statement
    if User_response == "quit":
        # If it is true then print Some Random Acknowledgement indicating the Game is over.
        print("The Game is Ended <!!>")
    else:
        # Else print some random answer from the above given list of answers using the 
        # choice() function of the random module by Passing the about Eight answers list to choice Function
        # Here \n is used a separator to Print the new line
        print(random.choice(Magic_8ball_answers), "\n")
        # Call the above created codeMagic_8ball() function Recursively to Play the Game Again.
        codeMagic_8ball()
# Call the above created codeMagic_8ball() function to start the game.
codeMagic_8ball()
