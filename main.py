import os
import mysql.connector as m
from prettytable import PrettyTable

conn = m.connect(host = 'localhost', user = 'root', password = 'student', database = 'medic')
cursor = conn.cursor()

def show_medicines():
    med_table = PrettyTable()
    med_table.field_names = ['Medicine Name','Usage / Indications','Quantity']

    cursor.execute("SELECT * FROM medicine")
    data = cursor.fetchall()

    for med,ind,qty in data:
        med_table.add_row([med,ind, qty])

    print(med_table)

os.system('cls')
print("_________________________SAINIK SCHOOL KALIKIRI______________________\n"
      "____________________________SANJEEVANI BLOCK_________________________\n"
      "______________________MEDICINE DATABASE MANAGEMENT___________________" )
print("\n")
while 1:
    print("\n")
    # Features of the Program
    print(chr(9899),"Press (1) to view the Medicine Dictionary")
    print(chr(9899),"Press (2) to edit the Dictionary")
    print(chr(9899),"Press (3) to delete a medicine from the Dictionary")
    print(chr(9899),"Press (4) to add a medicine to the Dictionary")
    print(chr(9899),"Press (5) to find the remedy for your disease")
    print(chr(9899),"Press (6) to checkout a medicine")
    print(chr(9888),"NOTE: If you check out a medicine it's quantity will be Decreased.")
    print("\n")

    #Input from the user to go to specific column
    main_input = input("Enter the Required Number: ")

    if main_input == '1':
        show_medicines()


    elif main_input == '2':
        print(chr(9888), "NOTE: Please enter the actual name as in List")
        med_name = input("Enter the Medicine name to Edit: ")

        cursor.execute("SELECT medicine_name FROM medicine")
        med_list_raw = cursor.fetchall()
        med_list = []
        for name in med_list_raw:
            med_list += name

        print(med_list)

        if med_name not in med_list:
            print("You have entered an Invalid Medicine Name")
            for j in med_list:
                if med_name[0:7].lower() == j[0:7].lower():
                    print("You may be searching for", j)
                    edit_med_name = input("Enter the Valid Medicine Name from the above Output: ")
                    edit_quantity = int(input("Enter the Quantity: "))
                    edit_use = input("Enter the Use of Medicine: ")

                    print("You have successfully changed the Medicine Details")
                    cursor.execute(f"SELECT * FROM medic WHERE medicine_name = {edit_med_name}")
                    med_data = cursor.fetchone()

                    if edit_med_name in med_list:
                        med_table = PrettyTable()
                        med_table.field_names = ["Medicine Name", "Usage / Indications","Quantity"]
                        med_table.add_row([med_data[0],med_data[1],med_data[2]])
                        med_table.add_row(['Changed to','Changed to','Changed to'])

                        cursor.execute(f"UPDATE medicine set usage_or_indications = '{edit_use}', quantity = {edit_quantity} where medicine name = {edit_med_name}")
                        print(med_table)

                    else:
                        pass


                    break
                else:
                    print("Sorry ", chr(9785))
                    break
        else:
            inpt5_0 = input("Enter the Company Name: ")
            inpt5_1 = int(input("Enter the Quantity: "))
            inpt5_2 = input("Enter the Use of Medicine: ")
            edi_tup2 = (inpt5_0, inpt5_1, inpt5_2)
            dic[inpt2] = edi_tup2
            print("It is successfully edited :)", inpt2, ":", edi_tup2)
        print("\n")
        einpt2 = input("Do you want to continue (Y or N):")
        if einpt2 == "Y":
            continue
        elif einpt2 == "y":
            continue
        else:
            print(chr(9055), "Thank You for using our Program", chr(9055))
            break

    elif main_input == '3':
        pass

    elif main_input == '4':
        pass

    elif main_input == '5':
        pass

    elif main_input == '6':
        pass

    else:
        print("The entered input is not compatible with given options")
        false_input = input("Do you want to continue (Y or N): ")
        if false_input == 'y' or false_input == 'Y':
            continue
        else:
            print(chr(9055), "Thank You for using our Program", chr(9055))
            break