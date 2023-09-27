from tkinter import *
import time
import random
from result import Result

# Function to start the timer
def start_timer():
    global time_left, timer_running
    time_left = time_var.get()
    timer_running = True
    sor_txt.delete("1.0", "end")  # Clear the text input field
    sor_txt.config(state=NORMAL)  # Enable the text input field
    countdown()


# Function to update the timer
def countdown():
    global time_left, timer_running
       
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time Left: {time_left} seconds")
        timer_label.after(1000, countdown)  # Call countdown again after 1 second
    else:
        timer_label.config(text="Time's up!")
        timer_running = False
        sor_txt.config(state=DISABLED)  # Disable the text input field
        
        calculate_speed()  # Disable the "Result" button

# Function to calculate the typing speed
def calculate_speed():
    typed_text = sor_txt.get("1.0", "end-1c")  # Get the typed text from the Text widget
    source_text = Ttext_txt.cget("text")  # Get the source text
    typed_words = typed_text.split()
    source_words = source_text.split()
    
    correct_words = 0
    
    for typed_word, source_word in zip(typed_words, source_words):
        if typed_word == source_word:
            correct_words += 1

    accuracy = (correct_words / len(source_words)) * 100
    wpm = (correct_words / time_var.get()) * 60  # Calculate words per minute (WPM) based on correct words
    Result(accuracy, wpm, time_var.get())

# Create the main window
root = Tk()
root.title("Typing Speed Tester")
root.geometry("500x700")

# Set background color
root.configure(bg="brown")


paragraph=['The sun rose over the horizon, casting\na warm glow across the tranquil sea.\nBirds chirped, welcoming the new day. The\nbeach was serene, with soft sand underfoot.\nPeople strolled, enjoying the peaceful morning. Waves\nlapped gently, soothing the soul. It was\na perfect start to a beautiful day.', "In the bustling city, cars honked and\npeople hurried. Skyscrapers reached for the sky,\ncasting shadows on the streets. Cafes bustled\nwith activity, the aroma of coffee filling\nthe air. Businesspeople in suits rushed to\nmeetings. Amid the chaos, the city's energy\nwas electrifying, a constant buzz.", "Deep in the forest, trees stood tall\nand ancient. Leaves rustled, and birds sang\ntheir melodies. A gentle stream meandered through\nthe woods, babbling softly. Deer grazed peacefully\nin the clearing. Nature's beauty was awe-inspiring,\na reminder of the world's wonders.", "High in the mountains, snow-covered peaks glistened\nin the sunlight. The air was crisp\nand pure. Hikers trudged through the snow,\nseeking adventure. The view from the summit\nwas breathtaking, a reward for their effort.\nNature's majesty was on full display, a\ntestament to its grandeur.", 'On a cozy evening, a fireplace crackled,\nwarming the room. Soft music played in\nthe background. Friends gathered, sharing stories and\nlaughter. The aroma of dinner filled the\nair. It was a night of camaraderie,\na reminder of the importance of friendship\nand connection.']

RendomTextOFSource=random.choice(paragraph)


lab_txt = Label(root, text="Welcome to Typing Speed Tester", font=("Times New Roman", 20, "bold"), bg="brown")
lab_txt.place(x=15, y=10, height=90, width=450)

sor_txt = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), bg="brown")
sor_txt.place(x=100, y=100, height=22, width=300)

Ttext_txt = Label(root, text=RendomTextOFSource, font=("Times New Roman", 15), bg="brown")
Ttext_txt.place(x=10, y=140, height=160, width=500)

time_var = IntVar()
time_var.set(30)  # Default time set to 30 seconds

radio_30 = Radiobutton(root, text="30 seconds", variable=time_var, value=30, bg="brown")
radio_60 = Radiobutton(root, text="60 seconds", variable=time_var, value=60, bg="brown")

radio_30.place(x=100, y=320)
radio_60.place(x=250, y=320)

timer_label = Label(root, text="Time Left: 30 seconds", font=("Times New Roman", 16), bg="brown")
timer_label.place(x=50, y=360)

start_button = Button(text="Start Timer", relief=RAISED,bg="brown", command=start_timer)
start_button.place(x=320, y=360, height=40, width=100)

sor_txt = Text(root, font=("Times New Roman", 20, "bold"),bg="brown")
sor_txt.place(x=10, y=420, height=150, width=480)


# Initialize the timer_running variable
timer_running = False
sor_txt.config(state=DISABLED)
root.mainloop()
