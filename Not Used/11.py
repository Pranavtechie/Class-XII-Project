#Dictionary Containing all Medicines
dic = {"Tab Pantop - D":("Reddy's Lab",200,"Gastric"),"Tab Vitamin - C ":("XYZ",1000,"Deficiency - Vitamin C"),
       "Tab Paracetimol 500 mg":("Crocin",1000,"Body Pains, Cold(Below 13)"),
       "Tab Paracetimol 650 mg":("Crocin",200,"Body Pains, Cold(Adults)"),
       "Tab Albendazole" : ("HI",1000,"Deworming"),"Tab Mulitivitamin" : ("HI",200,"Eye Problem"),
       "Tab Calcium" : ("HI",50,"Weak Bones"),"Budecort Respules" : ("HI",10,"Asthama"),"Omnigel Ointment" : ("HI",50,"Sprain"),
       "Omnigel Spray" : ("HI",50,"Sprain"),"Syp Paracetimol P125 mg" : ("Crocin",10,"Fever(For babies)"),
       "Syp Parecetimol P250mg" : ("Crocin",10,"Fever(For babies)")}
# The Heading of the Program

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
    
    # Input from the User
    inpt1 = eval(input("Enter the Required Number: "))
    # Viewing Of the table
    if inpt1 == 1:
        print("Medicine Name","\t\t\t\t","Company Name", "\t\t\t\t","Quantity", "\t\t\t\t","Usage")
        for i in dic:
            print(i,"\t\t\t\t",dic[i][0],"\t\t\t\t",dic[i][1],"\t\t\t\t",dic[i][2] )
        print("\n")
            
        einpt1 = input("Do you want to continue (Y or N):")
        if einpt1 =="Y":
            continue
        elif einpt1 == "y":
            continue
        else:
            print(chr(9055),"Thank You for using our Program",chr(9055))
            break
        
            

    # Editing Of the Table
    if inpt1 == 2:
        print(chr(9888),"NOTE: Please enter the actual name as in List" )
        inpt2 = input("Enter the Medicine name to Edit: ")
        if inpt2 not in dic:
            print("You have entered an Invalid Medicine Name")
            for j in dic:
                if inpt2[0:7] == j[0:7]:
                    print("You may be searching for",j)
                    inpt3   = input("Enter the Valid Medicine Name from the above Output: ")
                    inpt4_0 = input("Enter the Company Name: ")
                    inpt4_1 = int(input("Enter the Quantity: "))
                    inpt4_2 = input("Enter the Use of Medicine: ")
                    edi_tup1 = (inpt4_0,inpt4_1,inpt4_2)
                    dic[inpt3] = edi_tup1
                    print("You have successfully changed the Medicine Details")
                    print(inpt3,":",dic[inpt3])
                    break
                else:
                    print("Sorry ",chr(9785))
                    break
        else:
            inpt5_0 = input("Enter the Company Name: ")
            inpt5_1 = int(input("Enter the Quantity: "))
            inpt5_2 = input("Enter the Use of Medicine: ")
            edi_tup2 = (inpt5_0,inpt5_1,inpt5_2)
            dic[inpt2] = edi_tup2
            print("It is successfully edited :)",inpt2,":",edi_tup2)
        print("\n")
        einpt2 = input("Do you want to continue (Y or N):")
        if einpt2 =="Y":
            continue
        elif einpt2 == "y":
            continue
        else:
            print(chr(9055),"Thank You for using our Program",chr(9055))
            break
        
    # To Delete a Key and Value from a Dictionary
    if inpt1 == 3:
        inpt6 = input("Enter the medicine name to delete: ")
        if inpt6 not in dic:
            print("You have entered an Invalid Medicine Name")
            for k in dic:
                if inpt6[0:7] == k[0:7]:
                    print("You may be searching for",k)
                    inpt7  = input("Enter the Valid medicine name you wanted to delete: ")
                    dic.pop(inpt7)
                    print("You have successfully deleted the item ",inpt7,":)")
                    break
                else:
                    print("Sorry ",chr(9785))
                    break
            
        
        else:
            dic.pop(inpt6)
            print("You have succeessfully deleted",inpt6,":)")
        print("\n")
        einpt3 = input("Do you want to continue (Y or N):")
        if einpt3 =="Y":
            continue
        elif einpt3 == "y":
            continue
        else:
            print(chr(9055),"Thank You for using our Program",chr(9055))
            break

    # To add a Key and Value to a Dictionary
    if inpt1 == 4:
        inpt7 = input("Enter the Key to Add to the Dictionary: ")
        inpt8_0 = input("Enter the Company Name: ")
        inpt8_1 = int(input("Enter the Quantity: "))
        inpt8_2 = input("Enter the Use of Medicine: ")
        edi_tup3 = (inpt8_0,inpt8_1,inpt8_2)
        dic[inpt7] = edi_tup3
        print("Medicine Added Successfully : ",{inpt7 : edi_tup3})
        print("\n")
        einpt4 = input("Do you want to continue (Y or N):")
        if einpt4 =="Y":
            continue
        elif einpt4 == "y":
            continue
        else:
            print(chr(9055),"Thank You for using our Program",chr(9055))
            break
 
 
    symdic = {"Fever":("Tab Pantop - D","Cap Amoxilline 500 mg"),}
    # To find the Usage of the Medicine
    if inpt1 == 5:
        inpt9 = input("Please enter the Symptom you are facing: ")     
        for z in symdic.keys():
            if inpt9 != z:
                print("The entered Symptom does not exist in our database")
                if inpt9[0:3] == z[0:3]:
                    print("You may be searching for",z)
                    inpt10 = input("Enter the valid symptom from the above output: ")
                    print("The medicines you can use are",symdic[inpt10])
                else:
                    print("Sorry ",chr(9785))
                    break
            else:
                print("The medicines you can use are",symdic[inpt9])
        print("\n")
        einpt5 = input("Do you want to continue (Y or N):")
        if einpt5 =="Y":
            continue
        elif einpt5 == "y":
            continue
        else:
            print(chr(9055),"Thank You for using our Program",chr(9055))
            break
            
    # To checkout a Medicine From Database
    if inpt1 == 6:
        inpt11 = input("Please enter the medicine for checkout: ")
        
        
        if inpt11 not in dic:
            print("The entered Medicine does not exist in our database",chr(9785))
            for x in dic:
                if inpt11[0:7] == x[0:7]:
                    print("You may be searching for",x)
            inpt12 = input("Enter the valid medicine: ")
            if inpt12 not in  dic:
                print(chr(9888),"Medicine does not exist",chr(9785))
                break
            print("Available quantity in MI room is",dic[inpt12][1])
            inpt13 = int(input("Please enter the Quantity for Checkout: "))
            if inpt13>dic[inpt12][1]:
                print(chr(9888),"Available quantity in MI room is",dic[inpt12][1],"Cannot Proceed:(")
                
            else:
                tup1 = (dic[inpt12][1] - inpt13,)
                tup2 = (dic[inpt12][0],)
                tup3 = (dic[inpt12][2],)
                tup4 = tup2 + tup1 + tup3
                dic[inpt12] = tup4
                print ("Tablet's Data Changed:) \n",inpt12,":",dic[inpt12])
        else:
            print("Quantity available in MI room:",dic[inpt11][1])
            inpt14 = int(input("Please enter the Quantity for Checkout: "))
            
            if inpt14>dic[inpt11][1]:
                print("The quantity available in MI room is:",dic[inpt11][1],"...Not possible")
                print("")
                inpt15 = int(input("Please re-enter the Quantity for Checkout: "))
                etup1 = (dic[inpt11][1] - inpt15,)
                etup2 = (dic[inpt11][0],)
                etup3 = (dic[inpt11][2],)
                etup4 = etup2 + etup1 + etup3
                dic[inpt11]=etup4
                print ("Tablet's Data Changed:) \n",inpt11,":",dic[inpt11])
                
            else:
                tup5 = (dic[inpt11][1] - inpt14,)
                tup6 = (dic[inpt11][0],)
                tup7 = (dic[inpt11][2],)
                tup8 = tup6 + tup5 + tup7
                dic[inpt11] = tup8
                print ("Tablet's Data Changed:) \n",inpt11,":",dic[inpt11])
        print("")
        einpt6 = input("Do you want to continue (Y or N):")
        if einpt6 =="Y":
            continue
        elif einpt6 == "y":
            continue
        else:
            print(chr(9055),"Thank You for using our Program",chr(9055))
            break
    else:
        a="abc"
        if type(inpt1)==type(a):
            print("Enter a valid number")
        else:
         print(chr(9888),"Enter a correct number",chr(9785))
        print()
        einpt7 = input("Do you want to continue (Y or N):")
        if einpt7 =="Y":
            continue
        elif einpt7 == "y":
            continue
        else:
            
            print(chr(9055),"Thank You for using our Program",chr(9055))
            break
        
    
        
                 
            
                
    
            
                
            
        
            
    
    
    




    



