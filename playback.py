"""
In a file called playback.py, implement a program in Python that prompts
the user for input and then outputs that same input,
replacing each space with ... (i.e., three periods).
"""
def playback(prompt):
#remember to strip the prompt not the replace.
    prompt = prompt.strip().replace(" ", "...")
    return (prompt)
    
def main():
    play = input("$ ")
    print(playback(play))

main()