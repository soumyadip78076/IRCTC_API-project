import requests
from datetime import datetime 

class Irctc:
    def __init__(self):
        while True:
            user_input = input(""" 
                            1. Live Train Status 
                            2. PNR Check 
                            3. Train Schedule 
                            4. Train Info
                            5. EXIT
                            what you want to do ? : """)
            if user_input == "1":
                self.live_train()
            elif user_input == "2":
                self.pnr_status()
            elif user_input == "3":
                self.train_schedule()
            elif user_input=="4":
                self.train_info()
            elif user_input=="5":
                break
            else:
                print("Invalid Option! Please try again.")
    def live_train(self):
        train_no = input("Enter the Train Number: ")
        date=input("Enter the Date in DD-MM-YYYY Format : ")
        actual_date_format=datetime.strptime(date, "%d-%m-%Y")
        formatted_date = actual_date_format.strftime("%Y%m%d")
        self.fetch_data(train_no=train_no,request_type="train_live_update")
    def train_schedule(self):
        train_no = input("Enter the Train Number: ")
        self.fetch_data(train_no=train_no,request_type="schedule")
    def pnr_status(self):
        pnr_no=input("Enter Your pnr no : ")
        self.fetch_data(pnr_no=pnr_no ,request_type="pnr")
    def train_info(self):
        train_no = input("Enter the Train Number: ")
        self.fetch_data(train_no=train_no ,request_type="info")
    def fetch_data(self, train_no=None,pnr_no=None,request_type=None,formatted_date=None):
        if request_type=="schedule" and train_no:
            url = f"http://indianrailapi.com/api/v2/TrainSchedule/apikey/ab6c29bd26c3315624698c51c1eb7938/TrainNumber/{train_no}/"
        elif request_type=="pnr"and pnr_no:
            url=  f"https://indianrailapi.com/api/v2/PNRCheck/apikey/ab6c29bd26c3315624698c51c1eb7938/PNRNumber/{pnr_no}/"
        elif request_type=="info" and train_no:
            url=  f"http://indianrailapi.com/api/v2/TrainInformation/apikey/ab6c29bd26c3315624698c51c1eb7938/TrainNumber/{train_no}/"
        elif request_type=="train_live_update" and train_no:
            url=  f"http://indianrailapi.com/api/v2/livetrainstatus/apikey/ab6c29bd26c3315624698c51c1eb7938/trainnumber/{train_no}/date/{formatted_date}/"
        else:
            print("Invalid request")
        try:
            response = requests.get(url, verify=False)
            if response.status_code == 200:
                data = response.json()
                #print(data["Route"])
                if request_type=="schedule":
                    print("Train Schedule for: ",train_no,"NO Train")
                    for i in data["Route"]:
                        print(i["StationName"],"|",i["ArrivalTime"],"|",i["DepartureTime"])
                elif request_type=="pnr":
                    print(data)
                elif request_type=="info":
                    print(data)
                elif request_type=="train_live_update":
                    print(data)
            else:
                print(f"Error: Unable to fetch data. HTTP Status Code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
kalka = Irctc()
