"""
********************************************************************************
*                                                                              *
*                               Wikipedia Assistant                            *
*                                                                              *
********************************************************************************
"""

from colorama import Fore
from os import system, name
import wikipedia
import pyttsx3



# Function for the program to speak to the user
def speak(text):
    voice = pyttsx3.init()
    voice.setProperty("rate", 160)
    voice.say(text)
    voice.runAndWait()


# Function to clear the screen
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


clear()
# Welcome the user in blue text
print(Fore.BLUE + "Welcome to wikipedia assistant")
speak("Welcome to wikipedia assistant")

while True:
    # Clear Screen
    clear()
    try:
        # Get the topic the user wants to research
        print(Fore.BLUE + "What do you want to know about?")
        speak("What do you want to know about?")
        question = input(Fore.BLACK + '> ')

        clear()
        # Get the number of sentences for the summary
        print(Fore.BLUE + f"In how many sentences do you want {question} to be explained in?")
        speak(f"In how many sentences do you want {question} to be explained in? ")

        summary_length = input(Fore.BLACK + '> ')
        clear()
        print(Fore.YELLOW + "Getting info ...")
        speak("Getting Info")

        # Generate summary from wikipedia
        result = wikipedia.summary(f'what is {question}', sentences=int(summary_length))

        clear()
        # Print summary to screen in red text
        print(Fore.RED + f"{result}")
        speak(result)
    except:
        clear()
        print("Sorry, wikipedia does not have information about that topic. Please try again.")
        speak("Sorry, wikipedia does not have information about that topic. Please try again.")

    clear()
    print(Fore.YELLOW + "Do you want to know about something else? Type y or n: ")
    speak("Do you want to know about something else? ")
    response = input('> ')
    if response == 'n':
        clear()
        print(Fore.BLUE + "Thank you for using this software! Good bye!")
        speak("Thank you for using this software! Good bye!")
        break
    clear()
