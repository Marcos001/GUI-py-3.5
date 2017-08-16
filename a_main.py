
print('init the application')

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys
import os

class MyWindow(Gtk.ApplicationWindow):
    ''''''
    #contructor: the title is "Welcome to Gnome " and the window belong to the application app
    def __init__(self, app):
        Gtk.Window.__init__(self, title='Welcome to Gnome', application=app)
        # set the title
        self.set_title('Welcome to Gnome')

        # set default size of the window
        self.set_default_size(300,300)

        #set the center
        self.set_position(Gtk.WindowPosition.MOUSE) #Gtk.WindowPosition.CENTER., Gtk.WindowPosition.CENTER_ALWAYS, Gtk.WindowPosition.CENTER_ON_PARENT



# a class to create an image
class MyImage(Gtk.Image):
    ''''''
    def __init__(self):
        Gtk.Image.__init__(self)
        self.set_from_file(os.getcwd()+'/asserts/ideia.png')


class MyLabel(Gtk.Label):
    def __init__(self):
        Gtk.Label.__init__(self)
        self.set_text('Marcos Vinícius')


class MyApp(Gtk.Application):

    def do_activate(self):
        ''''''

        def __init__(self):
            Gtk.Application.__init__(self)

        # create a gtk window belonging to the application itself
        janela = MyWindow(self)

        # a grid
        grid = Gtk.Grid()
        grid.set_column_spacing(20)

        # in the grid:
        # attach the first label in the top left corner
        grid.attach(MyImage(), 0,0,1,1)
        # attach second label

        grid.attach(MyLabel(), 1,0,1,1)

        # create an instance of MyImage() and the add it to the window
        #janela.add(MyImage())

        # create an instance of MyImage() and the add it to the window
        #janela.add(MyLabel())

        janela.add(grid)

        # show the window
        janela.show_all()

    # start up the application
    # Note that the function in C startup becomes do_startup() in python
    def do_startup(self):
        Gtk.Application.do_startup(self)


if __name__ == '__main__':
    #create and the run application, exit the value
    app = MyApp()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)