import tkinter as tk

window = tk.Tk()

from scorecard import Scorecard
from die import Die

window.geometry("400x385")

scorecard = Scorecard()

turn_counter = None
score_label = None
score_buttons = []

def roll_dice(dice:list[Die]):
    global turn_counter, score_label, score_buttons
    #if Die.turn == 3:
    #    turn_counter = tk.Label(window, text = f"{0 - Die.turn} Turns Left... Reseting Turns.")
    #    turn_counter.grid(column=2, row = 0)
    #    Die.turn = 0
    #    turn_counter = tk.Label(window, text = f"{0 - Die.turn} Turns Left...")

    # Clean up previous widgets if they exist
    
    if turn_counter:
        turn_counter.destroy()
    if score_label:
        score_label.destroy()
    for button in score_buttons:
        button.destroy()
    score_buttons = [] # Reset the list

    if Die.turn < 3:
        for die in dice:
            if not die.holding.get():
                die.roll()
        Die.turn += 1
        print(f"Rolls remaining: {3 - Die.turn}")
    else:
        print("No more rolls left.")

    turn_counter = tk.Label(window, text = f"{3 - Die.turn} Turns Left.").grid(column=2, row = 0)
    
    score_label = tk.Label(window, text = f"Score: {scorecard.score}").grid(column=4, row=0)

    ones = scorecard.score_turn(dice, 1)
    twos = scorecard.score_turn(dice, 2)
    threes = scorecard.score_turn(dice, 3)
    fours = scorecard.score_turn(dice, 4)
    fives = scorecard.score_turn(dice, 5)
    sixes = scorecard.score_turn(dice, 6)

    scores = [ones, twos, threes, fours, fives, sixes]
    names = ["ones", "twos", "threes", "fours", "fives", "sixes"]

    for i, score_value in enumerate(scores):
        button = tk.Button(window, text=f"{names[i]}: {score_value}")
        button.grid(column=1, row=i+4)
        score_buttons.append(button)

    full_house = scorecard.score_full_house(dice)
    full_house_button = tk.Button(window, text=f"Full House: {full_house}").grid(column=3, row=4)


header = tk.Label(window, text = "YAHTZEE!")
header.grid(column=0, row = 0)


dice = []
dice_labels = []
for i in range(5):
    label = tk.Label(window)
    label.grid(column=i, row=2)
    dice.append(Die(window, i, label))


button1 = tk.Button(
    window,
    text = "Roll",
    command=lambda: roll_dice(dice)
)

button1.grid(column=0, row=1)


window.mainloop()
