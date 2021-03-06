# Imports
import tkinter
import signal
import style
import draw
import util
import var

# Function that handles signals
def signal_handler(sig, frame):
    if (sig == signal.SIGINT):
        var.app.destroy()
        exit(0)

# Function that binds keystrokes to commands
def bind_keystrokes():
    # Basic control
    var.canvas.bind("<Button-1>", draw.get_coords)
    var.canvas.bind("<B1-Motion>", draw.draw_line)
    var.app.bind("<Control-w>", util.exit_app)
    var.app.bind("<Command-w>", util.exit_app)
    var.app.bind("<Control-s>", util.save_image)
    var.app.bind("<Command-s>", util.save_image)
    var.app.bind("<Control-p>", util.export_lines)
    var.app.bind("<Command-p>", util.export_lines)

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
    var.app.bind("<Command-z>", draw.undo_line)
    var.app.bind("<Control-y>", draw.redo_line)
    var.app.bind("<Command-y>", draw.redo_line)

    # Changing colors
    var.app.bind("<Control-d>", style.change_background_color)
    var.app.bind("<Command-d>", style.change_background_color)
    var.app.bind("<Control-l>", style.change_background_color)
    var.app.bind("<Command-l>", style.change_background_color)
    var.app.bind("<r>", style.change_line_color)
    var.app.bind("<g>", style.change_line_color)
    var.app.bind("<b>", style.change_line_color)
    var.app.bind("<d>", style.change_line_color)
    var.app.bind("<w>", style.change_line_color)

    # Transparency
    var.app.bind("<[>", util.decrease_transparency)
    var.app.bind("<]>", util.increase_transparency)

    # Line size
    var.app.bind("<=>", style.increase_line_size)
    var.app.bind("<minus>", style.decrease_line_size)

# Main function
def main():
    # Signal handling
    signal.signal(signal.SIGINT, signal_handler)

    # Creating app screen
    var.app = tkinter.Tk()
    var.app.geometry("".join([str(var.x_dim) + "x" + str(var.y_dim)]))

    # Creating canvas
    var.canvas = tkinter.Canvas(var.app, bg=var.back_color, width=var.x_dim, height=var.y_dim)
    var.canvas.pack(anchor='nw', fill='both', expand=1)

    # Binding Keystrokes
    bind_keystrokes()

    # Looping
    var.app.mainloop()

main()
