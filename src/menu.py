from bst import *

def help_message():
    print("Help Show this menu",
    "Print      Print the tree using In-order, Pre-order, Post-order",
    "Remove     Remove elements from the tree",
    "Delete     Delete whole tree",
    "Export     Export the tree to a file", # Maybe I will do it I dunno
    "Rebalance  Rebalance the tree",
    "Exit       Exits the program (same as CTRL+D)", sep='\n')

def menu():
    state = ""
    arr = []

    print(f"nodes> {len(arr)}")
    print(f"insert> {arr}")

    while True and state != "exit":
        state = input("action> ")

        if state.lower() == "help":
            help_message()
        elif state.lower() == "print":
            pass
        elif state.lower() == "remove":
            pass
        elif state.lower() == "export":
            pass
        elif state.lower() == "rebalance":
            pass
        elif state.lower() == "exit":
            state = "exit"
