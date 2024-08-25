def line(katz_deli):
    if not katz_deli:  # If the list is empty
        print("The line is currently empty.")
    else:
        # Create a list of people with their positions
        line_list = [f"{i + 1}. {name}" for i, name in enumerate(katz_deli)]
        print("The line is currently: " + " ".join(line_list))
def take_a_number(katz_deli, name):
    katz_deli.append(name)  # Add the customer to the end of the list
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")
def now_serving(katz_deli):
    if not katz_deli:  # If the list is empty
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli.pop(0)}.")  # Serve the first person and remove them from the list
