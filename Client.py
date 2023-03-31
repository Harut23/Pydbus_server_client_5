import random
from pydbus import SessionBus
from gi.repository import GLib

bus = SessionBus()
BUS = "org.example.demo.test"
server_object = bus.get(BUS)
loop = GLib.MainLoop()


def cb_signal_emission(*args):
    "Callback on emitting signal, a random integer, from server"
    # Data is in args[4],  The first item in a tuple. i.e args[4]
    # print[args]
    random_number = args[4][0]
    print("Client received random number: {}".format(random_number))



if __name__ =="__main__":
    print("Starting Client Demo 4..")

    # Create the dbus filter
    dbus_filter = "/" + "/".join(BUS.split("."))
    print(dbus_filter)

    bus.subscribe(object = dbus_filter, signal_fired = cb_signal_emission)
    loop.run()














