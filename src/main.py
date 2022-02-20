# Imports
import tkinter
import draw
import util
import var

# Main function
def main():
    # Creating app screen
    var.app = tkinter.Tk()
    var.app.geometry(str(var.xdim) + "x" + str(var.ydim))

    # Creating canvas
    var.canvas = tkinter.Canvas(var.app, bg="black")
    var.canvas.pack(anchor='nw', fill='both', expand=1)

    # Binding Keystrokes
    var.canvas.bind("<Button-1>", draw.get_coords)
    var.canvas.bind("<B1-Motion>", draw.draw_line)
    var.app.bind("<Right>", util.increase_width)
    var.app.bind("<Left>", util.decrease_width)
    var.app.bind("<Down>", util.increase_height)
    var.app.bind("<Up>", util.decrease_height)

    # Looping
    var.app.mainloop()

main()
