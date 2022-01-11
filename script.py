from stack import Stack

stacks = []

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

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
        

#title
print("==============\n")
print("Tower of Hanoi\n")
print("==============\n")

number_disks = int(input("\nHow many disks do you want to play with in this game?\n"))

while number_disks < 3: 
    number_disks = int(input("Enter a number GREATER than or EQUAL to 3.\n"))

for num in range(number_disks, 0, -1):
    left_stack.push(num)

number_optimal_moves = 2 ** number_disks - 1
num_user_moves = 0

print("\nThe fastest you can solve this game is in {0} moves.".format(number_optimal_moves))

while right_stack.get_size() != number_disks:
    print("Current Stack: \n")
    for stack in stacks: 
        stack.print_items()

    while True: 
        print("From which stack do you want to move?\n")
        from_stack = get_input()
        print("From which stack do you want to move to?\n")
        to_stack = get_input()
        
        if from_stack.is_empty(): 
            print("Invalid Move. Try Again\n")
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else: 
            print("Invalid Move. Try Again\n")

print("You completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, number_optimal_moves))