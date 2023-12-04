#chat gpt genius real
import tkinter as tk
from tkinter import ttk
import threading
import time
import requests

# Global variables
counter = 0
click_value = 1
rebirths = 0
rebirth_cost = 50
auto_clicker_cost = 100
auto_clicker_speed = 1

# Functions for game actions
def increase_counter():
    global counter
    counter += click_value
    update_counter()

def update_counter():
    counter_label.config(text=f"Click Count: {counter}")
    progress_bar['value'] = counter
    progress_bar['maximum'] = rebirth_cost

def rebirth():
    global counter, click_value, rebirths, rebirth_cost
    if counter >= rebirth_cost:
        counter -= rebirth_cost
        rebirths += 1
        click_value += 1
        rebirth_label.config(text=f"Rebirths: {rebirths}")
        update_counter()
        rebirth_cost += 50
        rebirth_button.config(text=f"Rebirth ({rebirth_cost} Clicks)")

def buy_auto_clicker():
    global counter, auto_clicker_speed, auto_clicker_cost
    if counter >= auto_clicker_cost:
        counter -= auto_clicker_cost
        auto_clicker_speed += 1
        auto_clicker_cost *= 2
        auto_clicker_label.config(text=f"Auto Clicker Speed: {auto_clicker_speed}")
        auto_clicker_button.config(text=f"Buy Auto Clicker ({auto_clicker_cost} Clicks)")

def auto_click():
    global counter
    while True:
        counter += auto_clicker_speed
        update_counter()
        time.sleep(1)

def reset_game():
    global counter, click_value, rebirths, rebirth_cost, auto_clicker_speed, auto_clicker_cost
    counter = 0
    click_value = 1
    rebirths = 0
    rebirth_cost = 50
    auto_clicker_speed = 1
    auto_clicker_cost = 100
    update_counter()
    rebirth_label.config(text="Rebirths: 0")
    auto_clicker_label.config(text="Auto Clicker Speed: 1")
    rebirth_button.config(text=f"Rebirth ({rebirth_cost} Clicks)")
    auto_clicker_button.config(text=f"Buy Auto Clicker ({auto_clicker_cost} Clicks)")

def submit_score():
    global counter
    webhook_url = ''  # "Not giving you the server webhook" -the owner of the server, 2023
    
    payload = {
        'content': f'Click count: {counter}'
    }
    
    # Sending POST request to Discord webhook
    requests.post(webhook_url, json=payload)

# Tkinter setup
root = tk.Tk()
root.title("Ultimate Clicker Game")
root.configure(bg="#2E3440")

counters_frame = tk.Frame(root, bg="#2E3440")
counters_frame.pack()

counter_label = tk.Label(counters_frame, text="Click Count: 0", fg="#FFFFFF", font=("Arial", 18), bg="#2E3440")
counter_label.pack()

rebirth_label = tk.Label(counters_frame, text="Rebirths: 0", fg="#FFFFFF", font=("Arial", 14), bg="#2E3440")
rebirth_label.pack()

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", maximum=rebirth_cost)
progress_bar.pack(pady=10)

buttons_frame = tk.Frame(root, bg="#2E3440")
buttons_frame.pack()

click_button = ttk.Button(buttons_frame, text="Click Me!", command=increase_counter)
click_button.pack(side=tk.LEFT, padx=10)

rebirth_button = ttk.Button(buttons_frame, text=f"Rebirth ({rebirth_cost} Clicks)", command=rebirth)
rebirth_button.pack(side=tk.LEFT, padx=10)

auto_clicker_button = ttk.Button(root, text=f"Buy Auto Clicker ({auto_clicker_cost} Clicks)", command=buy_auto_clicker)
auto_clicker_button.pack(pady=10)

reset_button = ttk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=20)

auto_clicker_label = tk.Label(root, text="Auto Clicker Speed: 1", fg="#FFFFFF", bg="#2E3440")
auto_clicker_label.pack()

submit_score_button = ttk.Button(root, text="Submit Score", command=submit_score)
submit_score_button.pack(pady=10)

# Start auto-clicking in a separate thread
auto_clicker_thread = threading.Thread(target=auto_click)
auto_clicker_thread.daemon = True
auto_clicker_thread.start()

root.mainloop()