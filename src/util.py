# Imports
import var

# Function for increasing canvas width
def increase_width(event):
    var.xdim += var.chdim
    var.app.geometry("".join([str(var.xdim) + "x" + str(var.ydim)]))

# Function for decreasing canvas width
def decrease_width(event):
    var.xdim -= var.chdim
    var.app.geometry("".join([str(var.xdim) + "x" + str(var.ydim)]))

# Function for increasing canvas height
def increase_height(event):
    var.ydim += var.chdim
    var.app.geometry("".join([str(var.xdim) + "x" + str(var.ydim)]))

# Function for
def decrease_height(event):
    var.ydim -= var.chdim
    var.app.geometry("".join([str(var.xdim) + "x" + str(var.ydim)]))
