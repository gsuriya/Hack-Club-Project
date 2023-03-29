import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()

# Set window size and position
window_width = 414 # width of iPhone 12 screen
window_height = 896 # height of iPhone 12 screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Set background color and font
root.configure(bg='#ADD8E6')  # light blue
button_font = ('Arial', 16)
title_font = ('Times New Roman', 24)

# Create title label
title_label = tk.Label(root, text="Ergon", font=title_font, fg='#000000', bg='#ADD8E6', pady=40)
title_label.pack()

# Create a frame to hold the buttons and chart
frame = tk.Frame(root, bg='#ADD8E6')
frame.pack(pady=20)

# Create Diagnosis button
diagnosis_button = tk.Button(frame, text="Diagnosis", font=button_font, bg='#FFFFFF', padx=20, pady=10)
diagnosis_button.pack(side=tk.LEFT)

# Create Statistics button
statistics_button = tk.Button(frame, text="Statistics", font=button_font, bg='#FFFFFF', padx=20, pady=10)
statistics_button.pack(side=tk.LEFT, padx=20)

# Create a figure object
fig = Figure(figsize=(4, 3), dpi=100)

# Add a subplot to the figure
ax = fig.add_subplot(111)

# Define the data for the bar chart
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
pain_levels = [3, 4, 2, 5, 1, 6, 2]

# Create the bar chart
ax.bar(days, pain_levels)

# Add labels to the chart
ax.set_title('Daily Pain Level', fontsize=16)
ax.set_xticks([]) # remove x-axis ticks
ax.set_ylabel('Pain Level', fontsize=12)

# Create a canvas to display the figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# Add the canvas to the window
canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()