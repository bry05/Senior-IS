import requests
from bs4 import BeautifulSoup
import pandas as pd



def get_response(user_input):


    if "cross country" in user_input.lower():
        cross_country = CrossCountryScheduleList()
        if cross_country:
            schedule = CrossCountryScheduleList()
            return {schedule}

def CrossCountryScheduleList(): #  Brings out the list of Meets(Names) to the User  def CrossCountryScheduleList(sport) <--- ???
    url = f"https://www.woosterathletics.com/sports/xc/2023-24/schedule"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    
    XCmeet1_info = soup.find_all('span', class_= "e_teamname e_opponent_name")
    
    
    content1 = []
    
    for content1 in XCmeet1_info:
        soup.get_text['innerText']
    
    
    #Meet1 = element1

    XCmeet2_info = soup.find_all('span', class_= "e_teamname e_opponent_name e_home")
    
    content2 = []
    
    for content2 in XCmeet2_info:
        soup.get_text['innerText']
        
    #Meet2 = element2


   # element2 = [element.get_text['innerText'] for element in XCmeet2_info]
     
    
    #.get_attribute('outerHTML')
    
    #Meet2 = text2
        
    meet = content1 + content2




    XC_schedule = f"Here are the List of Meets for 23-24 Season of College of Wooster Cross Country Team: {meet}"

    #PD_XCsport_info = pd.DataFrame(XCsport_info)

    return XC_schedule





def main():
    
    print("Welcome to the College of Wooster Athletics Chatbot! How can I help you?")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        response = get_response(user_input)
        print("Bot:", response)
        
      

if __name__ == "__main__":
    main()