import time
import random
from pydbus import SessionBus  # Session or System Bus
from gi.repository import GLib
from pydbus.generic import signal


bus = SessionBus()
BUS = "https://github.com/Harut23/SearchEngine2022"
loop = GLib.MainLoop()
INTERVAL = 2
message_count = 0



class DBusService_XML:
    """
    DBus Service XML definition
    type = "i" for integer, "S" string, "d" double, "as" list of string data
    """
    dbus = """
    <node>
        <interface name= "{}">
            <signal name="integer_signal">
                <arg type="i"/>
            <signal> 
        <interface>           
    </node>
    """.format(BUS)
    integer_signal = signal()


def timer():
    "emit a random integer each call"
    random_integer = random.randint(0, 100)
    print("random integer emitted: {}".format(random_integer))

    # emit signal
    emit.integer_signal(random_integer)
    return True



if __name__ == "__main__":
    emit = DBusService_XML()  # for signal example
    bus.publish(BUS, DBusService_XML())

    GLib.timeout_add_seconds(interval=INTERVAL, function = timer)
    loop.run()


