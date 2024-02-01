import pandas as pd


spam = pd.read_csv("C:\\Users\\bryso\\OneDrive\\Documents\\COwSports.csv")
 
spam = spam[["Sport", "Game", "Date"]]





def get_response(user_input):
    if "Men's Soccer" "Football"  "Swimming"  "Men's Golf"  "Women's Golf" "Men's Basketball" "Volleyball" "Cross Country" in user_input.lower():
           schedule = get_rows_by_name()
           return {schedule}
    
    
    
def get_rows_by_name(user_input):
    
    spam = pd.read_csv("C:\\Users\\bryso\\OneDrive\\Documents\\COwSports.csv")
 
    spam = spam[["Sport", "Game", "Date"]]
    
    
    rows =[]

    for row in spam['Sport']:
            for user_input.lower in row:
                if row['Sport'] == user_input.lower:
                    rows.append(row)
                    
    return rows









def main():
    
    print("Welcome to the College of Wooster Athletics Chatbot! Type in the sport that you are interested in:  Cross Country, Men's Soccer, Football,  Swimming, Men's Golf, Women's Golf, Men's Basketball, Volleyball")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        response = get_response(user_input)
        print("Bot:", response)
        
      

if __name__ == "__main__":
    main()