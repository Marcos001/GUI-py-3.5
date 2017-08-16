
print('Hello Worl')

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    ''''''
    #contructor: the title is "Welcome to Gnome " and the window belong to the application app
    def __init__(self, app):
        Gtk.Window.__init__(self, title='Welcome to Gnome', application=app)


class MyApp(Gtk.Application):

    def do_activate(self):
        ''''''

        def __init__(self):
            Gtk.Application.__init__(self)


        #create a gtk window belonging to the application itself
        janela = MyWindow(self)

        # set the title
        janela.set_title('Welcome to Gnome')

        # set default size of the window
        janela.set_default_size(300,200)

        #set the center
        janela.set_position(Gtk.WindowPosition.MOUSE) #Gtk.WindowPosition.CENTER., Gtk.WindowPosition.CENTER_ALWAYS, Gtk.WindowPosition.CENTER_ON_PARENT

        #show the window
        janela.show_all()

    # start up the application
    # Note that the function in C startup becomes do_startup() in python
    def do_startup(self):
        Gtk.Application.do_startup(self)



#create and the run application, exit the value
app = MyApp()
exit_status = app.run(sys.argv)
sys.exit(exit_status)