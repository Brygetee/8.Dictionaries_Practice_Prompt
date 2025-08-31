"""8. Dictionaries
What you should know: Store key–value pairs for structured data.
 Practice Prompt: Build a dictionary of sewing supplies with quantities,
 e.g. {"pins": 100, "needles": 20}, and write code to check the amount and update it when you “buy more.”"""





supplies = {
    "pins": 100,
    "needles": 20,
    "cutting mat": 1,
}
supplies_list = list(supplies)

def supplies_checker(project_type):
    return supplies.get(project_type, None)

while True:
    status = input(f"Which item would you like to check the quantity of? {supplies_list}\n").lower()
    result = supplies_checker(status)
    if result:
        print(f"You have {result} {status}.")
        new_supplies_bought = input(f"Have you recently bought more supplies?\nIf so, which one? {supplies_list},If none type 'none'") #MAKE SURE IF THE USER WROTE IT WRONG THEN YOU KNOW HOW TO FIX IT, also if the user types no
        # if statement checking that the input is a key in the dictionary,
        if new_supplies_bought in supplies:
            new_supplies_amount_added = int(input(f"how many {new_supplies_bought} did you buy?\n"))
            #get dictionary value of existing amount to add to the new amount
            new_total_amount = supplies[new_supplies_bought] + new_supplies_amount_added
            #change the amount in the actual dictionary and print it.
            supplies[new_supplies_bought] = new_total_amount
            print(f"You now have {supplies[new_supplies_bought]} {new_supplies_bought}")
        elif new_supplies_bought == "none":
            #TODO: Add a print statement printing all the supplies and their values
            break
        else:
            print("Choose a valid response")

        #
        # print(new_supplies_amount)

        # and add this to the value the user has input
        #then return this value

        break
    else:
        print("Choose a valid response.")

