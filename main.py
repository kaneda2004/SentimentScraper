#a python program that displays a gui with a url input box, a submit button, and an exit button. Also the GUI will display a text box that can be filled with text scraped from the aforementioned URL once the submit button is clicked, and another text box that displays the sentiment of the text in the previous text box. The program should scrape the URL for text once the submit button is clicked, then perform sentiment analysis on the scraped text using NLTK, and then finally display the resulting sentiment in the sentiment text box.

#import necessary libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#create the GUI
root = tk.Tk()
root.title("Sentiment Analysis")

#create the URL input box
url_label = ttk.Label(root, text = "Enter URL:")
url_label.grid(row = 0, column = 0, sticky = "w")
url_entry = ttk.Entry(root, width = 70)
url_entry.grid(row = 0, column = 1, sticky = "w")

#create the submit button
submit_button = ttk.Button(root, text = "Submit")
submit_button.grid(row = 0, column = 2, sticky = "w")

#create the exit button
exit_button = ttk.Button(root, text = "Exit")
exit_button.grid(row = 0, column = 3, sticky = "w")

#create the text box that will display the sentiment of the scraped text
sentiment_label = ttk.Label(root, text = "Sentiment:")
sentiment_label.grid(row = 1, column = 0, sticky = "w")
sentiment_entry = ttk.Entry(root, width = 70)
sentiment_entry.grid(row = 1, column = 1, sticky = "w")

#create the text box that will display the scraped text
scraped_text_label = ttk.Label(root, text = "Scraped Text:")
scraped_text_label.grid(row = 2, column = 0, sticky = "w")
scraped_text_entry = ttk.Entry(root, width = 70)
scraped_text_entry.grid(row = 2, column = 1, rowspan = 3, columnspan=2)

#create the function that will scrape the URL for text
def scrape_url():
    #get the URL from the URL input box
    url = url_entry.get()
    #get the text from the URL
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.get_text()
    #clear the scraped text box
    scraped_text_entry.delete(0, END)
    #display the text in the scraped text box
    scraped_text_entry.insert(0, text)
    #perform sentiment analysis on the text
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(text)
    #clear the sentiment text box
    sentiment_entry.delete(0, END)
    #display the sentiment in the sentiment text box
    sentiment_entry.insert(0, ss)

#create the function that will exit the program
def exit_program():
    root.destroy()

#create the function that will clear the text boxes
def clear_text():
    scraped_text_entry.delete(0, END)
    sentiment_entry.delete(0, END)

#create the function that will display a message box
def display_message():
    messagebox.showinfo("Sentiment Analysis", "This program will scrape a URL for text, perform sentiment analysis on the scraped text, and display the resulting sentiment.")

#create the menu bar
menu_bar = Menu(root)
root.config(menu = menu_bar)

#create the file menu
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "Exit", command = exit_program)

#create the help menu
help_menu = Menu(menu_bar)
menu_bar.add_cascade(label = "Help", menu = help_menu)
help_menu.add_command(label = "About", command = display_message)

#create the buttons
submit_button.config(command = scrape_url)
exit_button.config(command = exit_program)

#run the GUI
root.mainloop()