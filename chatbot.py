import google.generativeai as genai
import os
key = "AIzaSyDG7lQwPESbr9fU9wv-USHlSynblS75eYA"
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash")
while True:
    user = input("Enter your text here : ")
    if user.lower() == "exit":
        print("exiting bro .... ")
        break
    response = model.generate_content(user)
    print("Bot : " , response.text)
