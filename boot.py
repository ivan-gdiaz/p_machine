# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import network
import gc
#import webrepl
#webrepl.start()
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

gc.collect()