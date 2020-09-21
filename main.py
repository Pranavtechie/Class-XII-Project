import os
import mysql.connector as m
from prettytable import PrettyTable

conn = m.connect(host='localhost',
                 user='root',
                 password='student',
                 database='medic')
cursor = conn.cursor()


def thanks():
    print(f"\n{chr(9055)}  Thank You for using our Program  {chr(9055)}")


def show_medicines():
    med_table = PrettyTable()
    med_table.field_names = ['Medicine Name','Usage / Indications', 'Quantity']

    cursor.execute("SELECT * FROM medicine")
    data = cursor.fetchall()

    for med, ind, qty in data:
        med_table.add_row([med, ind, qty])

    print(med_table)


cursor.execute("SELECT medicine_name FROM medicine")
med_list_raw = cursor.fetchall()
med_list = []
for name in med_list_raw:
    med_list += name

def probable_med_and_table(medi_name):

    prob_table = PrettyTable()
    prob_table.field_names = ['Medicine Name', 'Usage / Indication','Quantity']

    cursor.execute(f"SELECT * FROM medicine WHERE medicine_name LIKE '%{medi_name}%'")
    data = cursor.fetchall()

    cursor.execute(f"SELECT medicine_name FROM medicine WHERE medicine_name LIKE '%{medi_name}%'")
    medicines = cursor.fetchall()

    medicine_list = []

    for medicine, usage, qty in data:
        prob_table.add_row([medicine, usage, qty])

    for medi in medicines:
        medicine_list += medi


    if len(medicine_list) == 0:
        prob_table.add_row(['nothing found','nothing found','nothing found'])

    return medicine_list, prob_table


os.system('cls')
print("_________________________SAINIK SCHOOL KALIKIRI______________________\n"
      "____________________________SANJEEVANI BLOCK_________________________\n"
      "______________________MEDICINE DATABASE MANAGEMENT___________________\n")

while True:
    print("\n")
    # Features of the Program
    print(chr(9899), "Press (1) to view the Medicine Table")
    print(chr(9899), "Press (2) to update the Medicine Table")
    print(chr(9899), "Press (3) to delete a Medicine")
    print(chr(9899), "Press (4) to add a Medicine to the Table")
    print(chr(9899), "Press (5) to find the remedy for your disease")
    print(chr(9899), "Press (6) to checkout a medicine")
    print(chr(9888), "NOTE: If you check out a medicine it's quantity will be Decreased.")
    print("\n")

    # Input from the user to go to specific column
    main_input = input("Enter the Required Number: ")

    #If user chose input as 1 then the medicine table will be listed
    if main_input == '1':
        show_medicines()

        con = input("\nDo you like to Continue using the Program (Y,N): ")

        if con in ['y', 'Y']:
            continue
        else:
            thanks()
            break

    elif main_input == '2':
        print(chr(9888), "NOTE: Please enter the actual name as in database but\n"
                         "If you cannot remember the name try entering first five letters\n\n")
        med_name = input("Enter the Medicine name to Edit: ")

        probable_list,probable_table = probable_med_and_table(med_name)

        if med_name in med_list:

            cursor.execute(
                f"SELECT * FROM medicine WHERE medicine_name = '{med_name}'")
            med_name, use, quantity = cursor.fetchone()

            correct_table = PrettyTable()
            correct_table.field_names = [
                'Medicine Name', 'Usage / Indications', 'Quantity']
            correct_table.add_row([med_name, use, quantity])

            print(correct_table)

            edited_table = PrettyTable()
            edited_table.field_names = ['Medicine Name', 'Usage / Indications', 'Quantity']
            edited_table.add_row([med_name, use, quantity])
            edited_table.add_row(['changed to', 'changed to', 'changed to'])

            new_med_name = input("Enter the new medicine Name: ")
            new_use = input("Enter the new Usage / Indication: ")
            new_qty = int(input("Enter the new quantity: "))

            cursor.execute(f"UPDATE medicine SET medicine_name = '{new_med_name}', usage_or_indications = '{new_use}', quantity = {new_qty} WHERE medicine_name = '{med_name}'")
            conn.commit()

            edited_table.add_row([new_med_name, new_use, new_qty])

            print("\nYou have successfully Updated the data of the Medicine\n", edited_table)

        else:
            print("\nYou have entered an Invalid Medicine Name")

            print("You may be searching for the medicine in the table\n")
            print(probable_table, '\n')
            print("Pro Tip: Try copy pasting the tablet that you want to edit\n")

            med_name = input("Enter the Medicine Name you want to update from the above table: ")

            if med_name in med_list:

                cursor.execute(
                    f"SELECT * FROM medicine WHERE medicine_name = '{med_name}'")
                med_name, use, quantity = cursor.fetchone()

                edited_table = PrettyTable()
                edited_table.field_names = [
                    'Medicine Name', 'Usage / Indications', 'Quantity']
                edited_table.add_row([med_name, use, quantity])
                edited_table.add_row(['changed to', 'changed to', 'changed to'])

                new_med_name = input("Enter the new medicine Name: ")
                new_use = input("Enter the new Usage / Indication: ")
                new_qty = int(input("Enter the new quantity: "))

                cursor.execute(
                    f"UPDATE medicine SET medicine_name = '{new_med_name}', usage_or_indications = '{new_use}', quantity = {new_qty} WHERE medicine_name = '{med_name}'")
                conn.commit()

                edited_table.add_row([new_med_name, new_use, new_qty])

                print("\nYou have successfully Updated the data of the medicine\n", edited_table)

            else:
                print(
                    "You have entered the Medicine Name wrong for two times, Try Again")
                con = input(
                    "\nWould you like to Continue using our Program (Y,N): ")

                if con in ['y', 'Y']:
                    continue
                else:
                    thanks()
                    break

    elif main_input == '3':

        print(chr(9888), "NOTE: Please enter the actual name as in database but\n"
                         "If you cannot remember the name try entering first five letters\n\n")

        med_name = input("Enter the Medicine name to Delete: ")

        del_probable_list, del_probable_table = probable_med_and_table(med_name)

        if med_name in med_list:

            print(f"The entered Medicine Name Exists")
            confirm_input = input("Are you sure you want to Delete the medicine (Y / N) : ")

            if confirm_input in ['y','Y']:

                delete_sql = f"DELETE FROM medicine WHERE medicine_name = '{med_name}'"
                cursor.execute(delete_sql)
                conn.commit()
                med_list.remove(med_name)

                print("You have successfully deleted the medicine from the database")

            else:
                print("You chose not to delete the medicine.")
                continue

        else:
            print("\nYou have entered an Invalid Medicine Name")

            print("You may be searching for the medicine in the table\n")
            print(del_probable_table, '\n')
            print("Pro Tip: Try copy pasting the tablet that you want to edit\n")

            med_name = input("Enter the Medicine name to Delete: ")

            if med_name in med_list:

                print(f"The entered Medicine Name Exists")
                confirm_input = input("Are you sure you want to Delete the medicine (Y / N) : ")

                if confirm_input in ['y', 'Y']:

                    delete_sql = f"DELETE FROM medicine WHERE medicine_name = '{med_name}'"
                    cursor.execute(delete_sql)
                    conn.commit()
                    med_list.remove(med_name)

                    print("You have successfully deleted the medicine from the database")

                else:
                    print("You chose not to delete the medicine.")
                    continue


    elif main_input == '4':
        print(chr(9888), "NOTE: Please enter the actual name as in List")

        med_name = input("Enter the Medicine name to Add: ")
        add_probable_list, add_probable_table = probable_med_and_table(med_name)

        condition = add_probable_list[0] in med_list

        if med_name in med_list:
            print("The medicine already exists in the database. Try to update the medicine")
            continue

        elif condition:
            print("\nThe medicine you wanted to enter does not exist but we have some probable list of medicines\n"
                  "matching in our database if you want to update those input Y below if you press N you can\n"
                  "enter the medicine as a new medicine.\n")

            print(add_probable_table)

            conf = input("Waiting for your input (Y / N) : ")
            if conf in ['y','Y']:
                print("You chose to update an existing medicine")
                continue

            else:
                current_med = input("\nEnter the new medicine name: ")
                current_use = input("Enter the Usage / Indication of the medicine: ")
                current_qty = int(input("Enter the quantity of the medicine: "))

                cursor.execute(f"INSERT INTO medicine values ('{current_med}', '{current_use}', {current_qty})")
                conn.commit()
                med_list += current_med

                print("You have successfully added a new medicine to the database.")

                continue_input = input("Would you like to continue: ")
                if continue_input in ['y', 'Y']:
                    continue

                else:
                    thanks()
                    break

        else:
            print("The medicine you entered does not exist in our database you can add the medicine\n")
            current_med = input("Enter the new medicine name: ")
            current_use = input("Enter the Usage / Indication of the medicine: ")
            current_qty = int(input("Enter the quantity of the medicine: "))

            cursor.execute(f"INSERT INTO medicine values ('{current_med}', '{current_use}', {current_qty})")
            conn.commit()
            med_list += current_med

            print("You have successfully added a new medicine to the database.")

            continue_input = input("Would you like to continue: ")
            if continue_input in ['y','Y']:
                continue

            else:
                thanks()
                break




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
            thanks()
            break
