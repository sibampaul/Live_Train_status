#This Program will check the live train status of any trin using railway api
#for this you need to create your api account and api key for free in railwayapi.

import json, requests

def get_live_status():
    apikey= "arz6oaccpj"

    #"https://api.railwayapi.com/v2/live/train/12046/station/GKP/date/20-06-2017/apikey/myapikey/"

    railway_api_link="https://api.railwayapi.com/v2/live/train/"

    train_no =input("\nEnter your train Number : ")
#    train_no="12246"
    station= input("Enter your Destination station code : ")
#    station = "HWH"
    date=input("Enter your date in dd-mm-yyyy format : ")
#    date="29-05-2019"
    final_link = railway_api_link + train_no +"/station/"+ station + "/date/"+ date + "/apikey/" + apikey + "/"

    api_response = requests.get(final_link)

    response_json=api_response.json()

    if response_json["response_code"] == 200:
        train_name= response_json["train"]["name"]
        sch_date =response_json["status"]["scharr_date"]
        sch_time=response_json["status"]["scharr"]

        destination_station =response_json["station"]["name"]

        position = response_json["position"]

        print("\n----------------------------------\n Name of the train : " + str(train_name) + "\n Destination station : "+ str(destination_station)
            +"\n Scheduled arrival time : " + str(sch_date) + " "+ str(sch_time) + "\n Current status : " + str(position) )
    else:
        print("\n Recorde not found :( \n")
    continue_or_not()

def continue_or_not():
    take_input =input("\n If you want to try again Press Y/y or Press any key and Enter to exit : ")

    if take_input == 'y' or take_input=="Y":
        get_live_status()
    else:
        return 0
get_live_status()
