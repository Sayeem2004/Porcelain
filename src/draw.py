# Imports
import var

# Function for M1 button click
def get_coords(event):
    var.px, var.py = event.x, event.y

# Function for M1 button movement
def draw_line(event):
    var.canvas.create_line((var.px, var.py, event.x, event.y), fill='red', width=2)
    var.px, var.py = event.x, event.y
