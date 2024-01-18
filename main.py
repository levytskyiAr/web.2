from Bot import *

if __name__ == "__main__":
    choice = {
        'add': AddBot(),
        'search': SearchBot(),
        'view': ViewBot(),
        'edit': EditBot(),
        'load': LoadBot(),
        'congratulate': CongratulateBot(),
        'delete': RemoveBot(),
        'exit': ExitBot(),
        'save': SaveBot(),
        'help': Help()
    }


    print('Hello. I am your contact-assistant. What should I do with your contacts? <type "help" to see commands> ')

    while True:
        action = input('Enter your command: ')
        if action in choice:
            choice[action].handle()
        else:
            print("Incorrect command!")
            