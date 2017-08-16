
print('Hello Worl')

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

class MyApp(Gtk.Application):

    def do_activate(self):
        ''''''
        #create a gtk window belonging to the application itself
        janela = Gtk.Window(application=self)

        # set the title
        janela.set_title('Welcome to Gnome')

        # set default size of the window
        janela.set_default_size(300,200)

        #show the window
        janela.show_all()


#create and the run application, exit the value
app = MyApp()
exit_status = app.run(sys.argv)
sys.exit(exit_status)