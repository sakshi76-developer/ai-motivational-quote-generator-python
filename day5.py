import tkinter as tk
import random
quotes = {
    "Motivation":[
           "Push yourself, because no one else is going to do it for you.",
        "Dream big and dare to fail.",
        "Success starts with self-discipline."
    ],

    "Study": [
        "Study now, shine later.",
        "Small progress is still progress.",
        "Focus on your goals."
    ],

    "Life": [
        "Life is short, make it meaningful.",
        "Happiness depends on your mindset.",
        "Every day is a fresh start."
    ]
}
def generate_quotes():
    category = category_var.get()
    quote = random.choice(quotes[category])
    quotes_label.config(text=quote)    

root= tk.Tk()
root.title("Ai Motivation Quotes Generator")
root.geometry("900x1000")
root.config(bg="#f2f2f2")

title = tk.Label(
    root,
    text="Motivation Quotes Generator",
    font=("Arial",35,"bold"),
    bg="#f2f2f2",
    fg="black" 
)
title.pack(pady=20)
category_var = tk.StringVar(value="Motivation")
dropdown = tk.OptionMenu(root,category_var, *quotes.keys())
dropdown.config(font=("Arial",18),width=15,bg="white",fg="black")
dropdown.pack(pady=30)

quotes_label= tk.Label(
    root,
    text="Click The Button To Generate Code",
    font=("Arial",35,"bold"),
    bg="#f2f2f2",
    fg="blue"
)
quotes_label.pack(pady=30)
generate_btn = tk.Button(
    root,
    text="Generate Quotes",
    command=generate_quotes,
    font=("Arial",18,"bold"),
    bg="blue",
    fg="white"
    )
generate_btn.pack(pady=30)

root.mainloop()
