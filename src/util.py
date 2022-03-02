# Imports
from datetime import datetime
from PIL import Image
import var
import os

# Function for increasing canvas width
def increase_width(event):
    var.x_dim += var.ch_dim
    var.app.geometry("".join([str(var.x_dim) + "x" + str(var.y_dim)]))

# Function for decreasing canvas width
def decrease_width(event):
    var.x_dim -= var.ch_dim
    var.x_dim = max(var.x_dim, 0)
    var.app.geometry("".join([str(var.x_dim) + "x" + str(var.y_dim)]))

# Function for increasing canvas height
def increase_height(event):
    var.y_dim += var.ch_dim
    var.app.geometry("".join([str(var.x_dim) + "x" + str(var.y_dim)]))

# Function for decreasing canvas height
def decrease_height(event):
    var.y_dim -= var.ch_dim
    var.y_dim = max(var.y_dim, 0)
    var.app.geometry("".join([str(var.x_dim) + "x" + str(var.y_dim)]))

# Function for shifting view to the right
def shift_right(event):
    for line in var.lines:
        var.canvas.move(line[0], var.ch_dim, 0)
        line[1][0] += var.ch_dim
        line[1][2] += var.ch_dim

# Function for shifting view to the left
def shift_left(event):
    for line in var.lines:
        var.canvas.move(line[0], -var.ch_dim, 0)
        line[1][0] -= var.ch_dim
        line[1][2] -= var.ch_dim

# Function for shifting view to the top
def shift_up(event):
    for line in var.lines:
        var.canvas.move(line[0], 0, -var.ch_dim)
        line[1][1] -= var.ch_dim
        line[1][3] -= var.ch_dim

# Function for shifting view to the bottom
def shift_down(event):
    for line in var.lines:
        var.canvas.move(line[0], 0, var.ch_dim)
        line[1][1] += var.ch_dim
        line[1][3] += var.ch_dim

# Function that exits the app
def exit_app(event):
    var.app.destroy()
    exit(0)

# Saving a screenshot of the board
def save_image(event):
    # Parsing file name from time
    file = datetime.now().strftime("%d%m%Y%H%M%S")

    # Saving as postscript
    if (not os.path.exists(var.img_dir)):
        os.makedirs(var.img_dir)
    file = "".join([var.img_dir, file, ".eps"])
    var.canvas.postscript(file=file)

    # Converting to png
    img = Image.open(file)
    img.save(file, 'png')
    os.remove(file)
    file = file[:-3] + "png"

    # Done message
    print("Lines exported into img folder, filename: " + file)

# Exporting lines into a csv file
def export_lines(event):
    # Parsing file name from time
    file = datetime.now().strftime("%d%m%Y%H%M%S")

    # Saving as postscript
    if (not os.path.exists(var.csv_dir)):
        os.makedirs(var.csv_dir)
    file = "".join([var.csv_dir, file, ".csv"])
    var.canvas.postscript(file=file)

    fout = open(file, "w")
    for line in var.lines:
        fout.write(str(line[1]))
        fout.write("\n")

    # Done message
    print("Lines exported into csv folder, filename: " + file)

# Increasing transparency of the screen
def increase_transparency(event):
    var.trans = min(1, var.trans+0.05)
    var.app.attributes("-alpha", var.trans)

# Decreasing transparency of the screen
def decrease_transparency(event):
    var.trans = max(0, var.trans-0.05)
    var.app.attributes("-alpha", var.trans)
