import datetime
import json


CustomerCom = {}
time = datetime.datetime.now()
selectCom = ""

def Customer():
    
    if CustomerCom:
        complain = input("Enter a complain: ")
            
        if complain in CustomerCom.values():
            print("Complain already exist")
        else:
            for record in CustomerCom.values():
                if complain in CustomerCom.values():
                    print("Complain already exist")
                else:
                    CustomerCom[complain] = {"Complain":complain}
                    print("+++++++++++++++++++")
                    print("Complain: ", CustomerCom)
                    print("Was submitted on the ",time)
                    print("+++++++++++++++++++")
                    break
    else:
        complain = input("Enter a complain: ")
        CustomerCom[complain] = {"Complain":complain}
        print("Complain: ", CustomerCom)
        print("Was submitted on the ",time)
         

def view():
    for x in CustomerCom.values():
        print(x)


def select(selectCom):
    #selectCom =  CustomerCom.get("complain")
    #selectCom
    pick = int(input("Enter a value or number of complain you want to translate"))
    selectCom = list(CustomerCom.values())[pick]
    print(selectCom)
    return selectCom

def language():
    import requests
    
    languageCom = input("Enter the language to translate:")
    src = input("Enter the language to translate from")
    
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = "q=select(selectCom)&target=languageCom&source=src"
    headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "9ebc9e11bcmsh74dfdeaa35afdacp16d31ajsn4974d9ffee15",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    #print(response.detect(languageCom))

def main():
    runtime = 1
    print("Welcome to complain day")
    while runtime:
        start = int(input("Press 0 to enter a complain, 1 to view complains,select a complain and to translate a complain.Press 2 to quit: "))
        
        if start == 0:
            Customer()
        elif start == 1:
            view()
            select(selectCom)
            language()
        elif start == 2:
            break
        else:
            print('Invalid value, try again')
main()
