import google.generativeai as genai
import os
key = "enter your api key"
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash")
while True:
    user = input("Enter your text here : ")
    if user.lower() == "exit":
        print("exiting bro .... ")
        break
    response = model.generate_content(user)
    print("Bot : " , response.text)

