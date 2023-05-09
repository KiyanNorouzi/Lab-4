#####
##### Ф.И: Ноурузи Мехди
##### ИСУ: 317306
##### группа: R3135
#####Номер варианта: 6
#####


import tkinter as tk
import random
import pygame

root = tk.Tk()
root.title("Prince of Persia Key Cracker")
root.geometry("600x600")
root.resizable(False, False)

pygame.mixer.init()
pygame.mixer.music.load("8bit.mp3")
pygame.mixer.music.play(-1)

weights = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
           'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26,
           '0': 27, '1': 28, '2': 29, '3': 30, '4': 31, '5': 32, '6': 33, '7': 34, '8': 35, '9': 36}

canvas = tk.Canvas(root, width=500, height=100)
canvas.pack()
 

def animate():
    canvas.move("ball", 5, 0)
    root.after(50, animate)

ball = canvas.create_oval(50, 50, 100, 100, fill="red", tags="ball")

animate()


def generate_key():

    key = ""
    for i in range(12):
        symbol = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        key += symbol

    blocks = [key[i:i+4] for i in range(0, len(key), 4)]
    

    averages = []
    for block in blocks:
        block_sum = sum(weights[symbol] for symbol in block)
        block_average = block_sum / len(block)
        averages.append(block_average)
    
 
    for average in averages: # Check that the average value of the sum of symbols in each block falls into the interval [12, 24]
        if average < 12 or average > 24:
            return generate_key()
    formatted_key = "-".join(blocks)
    key_label.config(text=formatted_key)


game_image = tk.PhotoImage(file="pop.png")
game_label = tk.Label(root, image=game_image)
game_label.pack()


key_label = tk.Label(root, text="XXXXX-XXXX-XXXX", font=("Arial", 20))
key_label.pack()


generate_button = tk.Button(root, text="Generate key", command=generate_key)
generate_button.pack()

root.mainloop()