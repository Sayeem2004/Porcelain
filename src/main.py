# Imports
import tkinter
import draw
import util
import var

# Function that binds keystrokes to commands
def bind_keystrokes():
    # Basic control
    var.canvas.bind("<Button-1>", draw.get_coords)
    var.canvas.bind("<B1-Motion>", draw.draw_line)
    var.app.bind("<Control-c>", util.exit_app)

    # Changing window size
    var.app.bind("<Shift-Right>", util.increase_width)
    var.app.bind("<Shift-Left>", util.decrease_width)
    var.app.bind("<Shift-Down>", util.increase_height)
    var.app.bind("<Shift-Up>", util.decrease_height)

    # Shifting window
    var.app.bind("<Right>", util.shift_right)
    var.app.bind("<Left>", util.shift_left)
    var.app.bind("<Down>", util.shift_down)
    var.app.bind("<Up>", util.shift_up)

    # Undoing and redoing
    var.app.bind("<Control-z>", draw.undo_line)
    var.app.bind("<Control-y>", draw.redo_line)

# Main function
def main():
    # Creating app screen
    var.app = tkinter.Tk()
    var.app.geometry("".join([str(var.x_dim) + "x" + str(var.y_dim)]))

    # Creating canvas
    var.canvas = tkinter.Canvas(var.app, bg=var.back_color)
    var.canvas.pack(anchor='nw', fill='both', expand=1)

    # Binding Keystrokes
    bind_keystrokes()

    # Looping
    var.app.mainloop()

main()
