# Imports
import var

# Function for M1 button click
def get_coords(event):
    var.px, var.py = event.x, event.y

# Function for M1 button movement
def draw_line(event):
    # Drawing line
    curr = var.canvas.create_line((var.px, var.py, event.x, event.y), fill='red', width=2)
    var.px, var.py = event.x, event.y

    # Adding line to list of lines
    if (len(var.lines) == 0):
        var.lines.append([curr, var.canvas.coords(curr)])
    elif (var.line_ind == len(var.lines)-1):
        var.line_ind += 1
        var.lines.append([curr, var.canvas.coords(curr)])
    else:
        var.line_ind += 1
        var.lines = var.lines[:var.line_ind]
        var.lines.append([curr, var.canvas.coords(curr)])

# Function for Ctrl-Z
def undo_line(event):
    # Undoing 3 lines
    for _ in range(3):
        # Casework for undoing lines
        if (var.line_ind > 0):
            var.canvas.delete(var.lines[var.line_ind][0])
            var.line_ind -= 1
        else:
            var.canvas.delete(var.lines[var.line_ind][0])

# Function for Ctrl-Y
def redo_line(event):
    # Redoing 3 lines
    for _ in range(3):
        # Casework for redoing lines
        if (var.line_ind < len(var.lines)-1):
            var.line_ind += 1
            crds = var.lines[var.line_ind][1]
            var.canvas.delete(var.lines[var.line_ind][0])
            curr = var.canvas.create_line(crds, fill='red', width=2)
            var.lines[var.line_ind][0] = curr
        else:
            crds = var.lines[var.line_ind][1]
            var.canvas.delete(var.lines[var.line_ind][0])
            curr = var.canvas.create_line(crds, fill='red', width=2)
            var.lines[var.line_ind][0] = curr
