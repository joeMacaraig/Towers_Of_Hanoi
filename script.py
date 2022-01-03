from stack import Stack

stacks = []

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#title
print("\n")
print("\n")
print("\n")

number_disks = int(input("\nHow many disks do you want to play with in this game?\n"))

while number_disks < 3: 
    number_disks = int(input("Enter a number GREATER than or EQUAL to 3.\n"))

for num in range(number_disks, 0, -1):
    num.push("Left")

number_optimal_moves = 2 ** number_disks - 1
num_user_moves = 0

print("\nThe fastest you can solve this game is in {0} moves.".format(number_optimal_moves))




















def get_input(): 
    choices = [stack.get_name()[0] for stack in stacks]

    while True: 

        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {0} for {1}".format(letter, name))

        user_input = input("")

        if user_input in choices: 
        
            for i in range(len(stacks)):

                if user_input == choices[i]: 
                    return stacks[i]
        
