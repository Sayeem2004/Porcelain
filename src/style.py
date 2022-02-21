# Imports
import var

# Function for changing the background of the canvas
def change_background_color(event):
    if (event.keysym == "d"):
        var.back_color = "black"
        var.canvas.configure(bg=var.back_color)
        return
    if (event.keysym == "w"):
        var.back_color = "white"
        var.canvas.configure(bg=var.back_color)
        return

# Function for changing the line color
def change_line_color(event):
    if (event.keysym == "r"):
        var.line_color = "red"
        return
    if (event.keysym == "g"):
        var.line_color = "green"
        return
    if (event.keysym == "b"):
        var.line_color = "blue"
        return
    if (event.keysym == "d"):
        var.line_color = "black"
        return
    if (event.keysym == "w"):
        var.line_color = "white"
        return
