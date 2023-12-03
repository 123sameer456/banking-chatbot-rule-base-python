bank = {
    "Menu": {
        "1": {
            "Account Overview": {
                "Ballance Inquiry": "Dear Customer, your account balance is 10,000",
                "Account Statement": {
                    "1 week": "your request is being processed. Kindly wait.",
                    "1 month": "your request is being processed. Kindly wait.",
                    "3 months": "your request is being processed. Kindly wait.",
                    "6 months": "your request is being processed. Kindly wait."
                },
                "IBAN Generator": "Dear Customer, your IBAN number is 43534534",
                "Tax Certificates": {
                    "Advance Tax Certificate": "your request is being processed. Kindly wait.",
                    "Tax deduction on profit payment": "your request is being processed. Kindly wait.",
                    "Tax deduction on cash withdrawal": "your request is being processed. Kindly wait."
                }
            }
        }
    }
}

# print(bank["Menu"]["1"]["Account Overview"]["Tax Certificates"][ "Advance Tax Certificate"])
print("\n\n")
print("WELCOME TO THE TEST BANK. PLEASE type  1")

while True:
    user = input("""User: """)
    if user == '1':
        
        print("""==== Menu ===
              1 - Your Account Overview
              2 - Meezan Product Offerings
              3 - Complaints
              4 - More About Islamic Banking""")
        menu_list = input("User: ")
        if menu_list == '1':
            print("\n\t=========  MENU > Overview =========")
            print("\t1- Ballance Inquiry")
            print("\t2- Account Statement")
            print("\t3- IBAN Generator")
            print("\t4- Tax Certificates ")
            submenu = input("Please enter the corresponding number for your selection: ")
            if submenu == "1":
                print(bank["Menu"]["1"]["Account Overview"]["Ballance Inquiry"])
                break
            elif submenu == "2":
                timeframe = input("Enter Time Frame (1 week/1 month/3 months/6 months): ")
                if timeframe == "1" :
                    print(bank["Menu"]["1"]["Account Overview"]["Account Statement"]['1 week'])
                    break
                elif timeframe =="2":
                    print(bank["Menu"]["1"]["Account Overview"]["Account Statement"]['1 month'])
                    break
                elif timeframe == "3" :
                    print(bank["Menu"]["1"]["Account Overview"]["Account Statement"]['3 months'])
                    break
                elif timeframe == "4" : 
                    print(bank["Menu"]["1"]["Account Overview"]["Account Statement"]['6 months'])
                    break
            elif submenu == "3":
                print(bank["Menu"]["1"]["Account Overview"]["IBAN Generator"])
                break
            elif submenu == "4":
                print("MENU > Overview > Certificates")
                print("""\t\tselect any one
                                         1 - Advance Tax deduction
                                         2 - Tax deduction on Profit Payment
                                         3 - Tax deduction on Cash Withdrawal """)
                tax_certificates = input("User: ")
                if tax_certificates == "1":
                    print(bank["Menu"]["1"]["Account Overview"]["Tax Certificates"]["Advance Tax Certificate"])
                elif tax_certificates == "2" :
                    print(bank["Menu"]["1"]["Account Overview"]["Tax Certificates"]["Tax deduction on profit payment"])
                elif tax_certificates == "3" : 
                    print(bank["Menu"]["1"]["Account Overview"]["Tax Certificates"]["Tax deduction on cash withdrawal"])
                else:
                    print("invalid number")
                    break
        elif menu_list == "2":
            print("\n\t=========  MENU > Offerings ==========")
            print("please type an option number of your desired service: ")
            print("""\t\t1 - premium Easy Home
                         2 - premium Car Ijarah
                         3 - premium Product Offerings
                         4 - RDA Financing Products
                         5 - RDA Investments Products
                         6 - RDA Debit Cards and Cheque Book Information
                         7 - RDA Internet Banking Guidlines """)
            offerings = input("User: ")
            if offerings == "1":
                print("premium Easy Home.pdf")
                break
            elif offerings == "2":
                print("premium Car Ijarah.pdf")
                break
            elif offerings == "3":
                print("premium Product Offerings")
                break
            elif offerings == "4":
                print("RDA Financing Products")
                break
            elif offerings == "5":
                print("RDA Investments Products")
                break
            elif offerings == "6":
                print("RDA Debit Cards and Cheque Book Information")
                break
            elif offerings == "7":
                print("RDA Internet Banking Guidelines")
                break
            else:
                print("invalid number")
                break



    else:
        print("invalid number")
        break
           
            
             

