import tkinter as tk

window = tk.Tk()

from scorecard import Scorecard
from die import Die

window.geometry("400x385")

scorecard = Scorecard()

turn_counter = None
score_label = None
score_buttons = []

def select_score_category(dice: list[Die], category: int, score: int):
    global turn_counter, score_label, score_buttons
    
    # Check if category already used
    category_used = {
        1: scorecard.used_ones,
        2: scorecard.used_twos,
        3: scorecard.used_threes,
        4: scorecard.used_fours,
        5: scorecard.used_fives,
        6: scorecard.used_sixes
    }
    
    if category_used[category]:
        print(f"Category {category} already used!")
        return
    
    # Add score to total and mark category as used
    scorecard.score += score
    for die in dice:
        die.holding.set(False)  # Reset holding status for next turn
    
    if category == 1:
        scorecard.used_ones = True
    elif category == 2:
        scorecard.used_twos = True
    elif category == 3:
        scorecard.used_threes = True
    elif category == 4:
        scorecard.used_fours = True
    elif category == 5:
        scorecard.used_fives = True
    elif category == 6:
        scorecard.used_sixes = True
    
    # Reset turn counter for next turn
    Die.turn = 0
    
    # Clean up UI
    if turn_counter:
        turn_counter.destroy()
    if score_label:
        score_label.destroy()
    for button in score_buttons:
        button.destroy()
    score_buttons = []
    
    # Update the display immediately
    turn_counter = tk.Label(window, text=f"{3 - Die.turn} Turns Left.")
    turn_counter.grid(column=2, row=0)
    
    score_label = tk.Label(window, text=f"Score: {scorecard.score}")
    score_label.grid(column=4, row=0)

    # Properly clear the dice images and checkbuttons
    for die in dice:
        die.label.config(image="")  # Clear the image
        die.label.grid_remove()     # Remove from grid
        die.checkbutton.grid_remove()  # Remove checkbutton from grid
        die.value = None            # Reset die value
    
    print(f"Scored {score} points in category {category}. Total score: {scorecard.score}")

def select_right_score_category(dice: list[Die], category: str, score: int):
    global turn_counter, score_label, score_buttons
    
    # Check if category already used
    category_used = {
        "full_house": scorecard.used_full_house,
        "large_straight": scorecard.used_large_straight,
        "small_straight": scorecard.used_small_straight,
        "three_of_a_kind": scorecard.used_three_of_a_kind,
        "four_of_a_kind": scorecard.used_four_of_a_kind,
        "chance": scorecard.used_chance,
        "yahtzee": scorecard.used_yahtzee
    }
    
    if category_used.get(category, False):
        print(f"Category {category} already used!")
        return
    
    # Add score to total and mark category as used
    scorecard.score += score
    for die in dice:
        die.holding.set(False)  # Reset holding status for next turn
    
    # Mark the specific category as used
    if category == "full_house":
        scorecard.used_full_house = True
    elif category == "large_straight":
        scorecard.used_large_straight = True
    elif category == "small_straight":
        scorecard.used_small_straight = True
    elif category == "three_of_a_kind":
        scorecard.used_three_of_a_kind = True
    elif category == "four_of_a_kind":
        scorecard.used_four_of_a_kind = True
    elif category == "chance":
        scorecard.used_chance = True
    elif category == "yahtzee":
        scorecard.used_yahtzee = True
    
    # Reset turn counter for next turn
    Die.turn = 0
    
    # Clean up UI
    if turn_counter:
        turn_counter.destroy()
    if score_label:
        score_label.destroy()
    for button in score_buttons:
        button.destroy()
    score_buttons = []
    
    # Update the display immediately
    turn_counter = tk.Label(window, text=f"{3 - Die.turn} Turns Left.")
    turn_counter.grid(column=2, row=0)
    
    score_label = tk.Label(window, text=f"Score: {scorecard.score}")
    score_label.grid(column=4, row=0)

    # Properly clear the dice images and checkbuttons
    for die in dice:
        die.label.config(image="")  # Clear the image
        die.label.grid_remove()     # Remove from grid
        die.checkbutton.grid_remove()  # Remove checkbutton from grid
        die.value = None            # Reset die value
    
    print(f"Scored {score} points in category {category}. Total score: {scorecard.score}")

def roll_dice(dice:list[Die]):
    global turn_counter, score_label, score_buttons
    
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

    dice_values = [die.value for die in dice]
    
    # Left scorecard (existing code)
    ones = scorecard.score_turn(dice_values, 1)
    twos = scorecard.score_turn(dice_values, 2)
    threes = scorecard.score_turn(dice_values, 3)
    fours = scorecard.score_turn(dice_values, 4)
    fives = scorecard.score_turn(dice_values, 5)
    sixes = scorecard.score_turn(dice_values, 6)

    scores = [ones, twos, threes, fours, fives, sixes]
    names = ["ones", "twos", "threes", "fours", "fives", "sixes"]
    used_categories = [scorecard.used_ones, scorecard.used_twos, scorecard.used_threes, 
                      scorecard.used_fours, scorecard.used_fives, scorecard.used_sixes]

    for i, score_value in enumerate(scores):
        if used_categories[i]:
            button_text = f"{names[i]}: X"
            button = tk.Button(
                window, 
                text=button_text,
                state="disabled"
            )
        else:
            button_text = f"{names[i]}: {score_value}"
            button = tk.Button(
                window, 
                text=button_text,
                command=lambda num=i+1, score=score_value: select_score_category(dice, num, score)
            )
        button.grid(column=1, row=i+4)
        score_buttons.append(button)

    # Right scorecard - Add these new buttons
    full_house_score = scorecard.score_full_house(dice_values)
    large_straight_score = scorecard.score_large_straight(dice_values)
    small_straight_score = scorecard.score_small_straight(dice_values)
    three_kind_score = scorecard.score_three_of_a_kind(dice_values)
    four_kind_score = scorecard.score_four_of_a_kind(dice_values)
    chance_score = scorecard.score_chance(dice_values)
    yahtzee_score = scorecard.score_yahtzee(dice_values)

    # Full House button
    if scorecard.used_full_house:
        full_house_button = tk.Button(window, text="Full House: X", state="disabled")
    else:
        full_house_button = tk.Button(
            window, 
            text=f"Full House: {full_house_score}",
            command=lambda: select_right_score_category(dice, "full_house", full_house_score)
        )
    full_house_button.grid(column=3, row=4)
    score_buttons.append(full_house_button)

    # Large Straight button
    if scorecard.used_large_straight:
        large_straight_button = tk.Button(window, text="Large Straight: X", state="disabled")
    else:
        large_straight_button = tk.Button(
            window, 
            text=f"Large Straight: {large_straight_score}",
            command=lambda: select_right_score_category(dice, "large_straight", large_straight_score)
        )
    large_straight_button.grid(column=3, row=5)
    score_buttons.append(large_straight_button)

    # Small Straight button
    if scorecard.used_small_straight:
        small_straight_button = tk.Button(window, text="Small Straight: X", state="disabled")
    else:
        small_straight_button = tk.Button(
            window, 
            text=f"Small Straight: {small_straight_score}",
            command=lambda: select_right_score_category(dice, "small_straight", small_straight_score)
        )
    small_straight_button.grid(column=3, row=6)
    score_buttons.append(small_straight_button)

    # Three of a Kind button
    if scorecard.used_three_of_a_kind:
        three_kind_button = tk.Button(window, text="Three of a Kind: X", state="disabled")
    else:
        three_kind_button = tk.Button(
            window, 
            text=f"Three of a Kind: {three_kind_score}",
            command=lambda: select_right_score_category(dice, "three_of_a_kind", three_kind_score)
        )
    three_kind_button.grid(column=3, row=7)
    score_buttons.append(three_kind_button)

    # Four of a Kind button
    if scorecard.used_four_of_a_kind:
        four_kind_button = tk.Button(window, text="Four of a Kind: X", state="disabled")
    else:
        four_kind_button = tk.Button(
            window, 
            text=f"Four of a Kind: {four_kind_score}",
            command=lambda: select_right_score_category(dice, "four_of_a_kind", four_kind_score)
        )
    four_kind_button.grid(column=3, row=8)
    score_buttons.append(four_kind_button)

    # Chance button
    if scorecard.used_chance:
        chance_button = tk.Button(window, text="Chance: X", state="disabled")
    else:
        chance_button = tk.Button(
            window, 
            text=f"Chance: {chance_score}",
            command=lambda: select_right_score_category(dice, "chance", chance_score)
        )
    chance_button.grid(column=3, row=9)
    score_buttons.append(chance_button)

    # Yahtzee button
    if scorecard.used_yahtzee:
        yahtzee_button = tk.Button(window, text="Yahtzee: X", state="disabled")
    else:
        yahtzee_button = tk.Button(
            window, 
            text=f"Yahtzee: {yahtzee_score}",
            command=lambda: select_right_score_category(dice, "yahtzee", yahtzee_score)
        )
    yahtzee_button.grid(column=3, row=10)
    score_buttons.append(yahtzee_button)


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
