# Imports
import tkinter
import draw
import util
import var

# Function that binds keystrokes to commands
def bind_keystrokes():
    # Basic drawing
    var.canvas.bind("<Button-1>", draw.get_coords)
    var.canvas.bind("<B1-Motion>", draw.draw_line)

    # Changing window size
    var.app.bind("<Right>", util.increase_width)
    var.app.bind("<Left>", util.decrease_width)
    var.app.bind("<Down>", util.increase_height)
    var.app.bind("<Up>", util.decrease_height)

    # Undoing and redoing
    var.app.bind("<Control-z>", draw.undo_line)
    var.app.bind("<Control-y>", draw.redo_line)

# Main function
def main():
    # Creating app screen
    var.app = tkinter.Tk()
    var.app.geometry("".join([str(var.xdim) + "x" + str(var.ydim)]))

    # Creating canvas
    var.canvas = tkinter.Canvas(var.app, bg="black")
    var.canvas.pack(anchor='nw', fill='both', expand=1)

    # Binding Keystrokes
    bind_keystrokes()

    # Looping
    var.app.mainloop()

main()
