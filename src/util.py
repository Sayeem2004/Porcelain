# Imports
import var

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
