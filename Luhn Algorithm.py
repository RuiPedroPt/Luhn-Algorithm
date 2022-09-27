# ---------------------------------- IMPORTANT ----------------------------------
# ---------------------------------- IMPORTANT ----------------------------------
# ---------------------------------- IMPORTANT ----------------------------------
# This was made By: Rui Pedro O. Paiva

# ---------------------------------- LICENSE ----------------------------------
# Because There is NO LICENSE this code is NOT ALLOWED FOR COMMERCIAL USE.
# This is ONLY FOR EDUCATIONAL PURPOSES for the Community, if you want to improve/optimize the code and update it you can, just ask for a repo update.


# ---------------------------------- Code ----------------------------------
CC_number = "5354 5614 0000 5278".replace(" ", "")

print("Card Number         |Valid / Invalid\n-------------------------------------")
space = (20- len(CC_number)) * " "

if len(CC_number) != 16:    # If lenght isn't 16 print Invalid Card
    print(str(CC_number) + space + "|Invalid❌")


elif len(CC_number) == 16:   # If lenght is correct (16) do the Luhn Algorithm
    # Get How many numbers are in the CC
    How_many_nums_in_CC = 0
    for numbers in CC_number:
        How_many_nums_in_CC += 1

    # ---------------------------- Even Numbers ----------------------------
    # Run through all the even numbers in the CC and append them to an array
    evenNumbers_array = []
    index = 0
    while index < How_many_nums_in_CC:
        even_num = CC_number[index]
        evenNumbers_array.append(int(even_num))
        index += 2

    # ---------------------------- Odd Numbers ----------------------------
    # Run through all the odd numbers in the CC and append them to an array
    OddNumbers_array = []
    odd_index = 1
    while odd_index < How_many_nums_in_CC:
        odd_number = CC_number[odd_index]
        OddNumbers_array.append(int(odd_number))
        odd_index += 2

    # ---------------------------- Step 2 ----------------------------
    Step2 = []
    for even_nums in evenNumbers_array:
        double = str(even_nums*2)

        if len(str(double)) == 2:
            ifLen2 = []
            ifLen2.append(int(double[0]))
            ifLen2.append(int(double[1]))

            double = sum(ifLen2)

        elif len(str(double)) == 1:
            pass

        else:   # There's an error
            print("There's an error!")

        Step2.append(int(double))

    # ---------------------------- Step 3 ----------------------------
    # Sum all Numbers
    Step3 = str(sum(Step2 + OddNumbers_array))

    # ---------------------------- Step 4 ----------------------------
    # If it Ends with a "0" it is a valid C ard

    if Step3[1] == "0" :    # Valid
        print(str(CC_number) + space + "|Valid✅")

    else:   # Invalid
        print(str(CC_number) + space + "|Invalid❌")
