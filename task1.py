num = int(input("Enter any number: "))
if (num % 2 == 0):
    print ("the entered number is even")
else:
    print("the entered number is odd")






age = int(input("enter your age:"))
income = float(input("enter your monthly income"))
job = str(input("Do you have a valid job:(yes/no)")).strip().title()
loan = float(input("Enter the amount of loan you want: RS. "))

def loan_amount_calculator( age, income, job, loan):
    if age >= 21 and income >= 30000 and job == "Yes":
        if 30000 <= income <= 49999:
            max_loan = 300000
        elif 50000 <= income <= 79999:
            max_loan = 500000
        elif 80000 <= income <= 99999:
            max_loan = 800000
        else:
            max_loan = 1000000
          

        print(f"Maximum loan available: RS. {max_loan}")
        print(f"Requested loan amount: RS. {loan}")

        if loan <= max_loan:
            print("Loan status: Approved")
        else:
            print("Loan status: Not Approved")
            print("Reason: Requested loan amount exceeds the maximum limit.")
    else:
        print("Loan status: Not Approved")
        if age < 21:
            print("Reason: Age is below the minimum requirement of 21.")
        if income < 30000:
            print("Reason: Monthly income is below the minimum requirement of Rs. 30,000.")
        if job != "Yes":
            print("Reason: Valid job is required for loan eligibility.")

loan_amount_calculator(age, income, job, loan)







user_input = input("Enter a string with at least 8 characters: ")
if len(user_input) < 8: 
    print("Please enter a string with at least 8 characters.") 
    if len(user_input) >= 8:   
        
        ascii_values = [ord(char) for char in user_input]
        print("ASCII values of each character:", ascii_values)

        modified_string = ""
        for i, char in enumerate(user_input):
            if (i + 1) % 2 == 0:  # Capitalize characters at positions 2, 4, 6, 8, ...
                modified_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
                modified_string += modified_char
            else:
                modified_string += char

        print("Final modified string:", modified_string)




num = int(input("Enter a 3-digit positive integer: "))
print("Decimal:", num)
print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hexadecimal:", hex(num))
print("Last digit:", num % 10)
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")
