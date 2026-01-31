# 1-import the random module
import random
#2 create a subject list 
subjects = ["The cat", "A scientist", "The president", "An alien", "The teacher"]
action=["discovers", "invents", "announces", "explores", "teaches"]
objects=["a new planet", "a groundbreaking", "a secret", "a new technology", "a mystery"]
#3 stat the  headline generatino loop
while True:
    subjects_choice = random.choice(subjects)
    action_choice = random.choice(action)
    objects_choice = random.choice(objects)
    headline = f" breaking news:{subjects_choice} {action_choice} {objects_choice}"
    print("\n"+headline)
    user_input = input("\nGenerate another headline? (y/n): ").strip().lower()
    if user_input == "no":
        break 
    print("\nThank you for using the fake headline generator!")
