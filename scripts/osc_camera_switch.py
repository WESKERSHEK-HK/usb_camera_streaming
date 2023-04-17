#!/usr/bin/env python3

import argparse
import subprocess
from pythonosc import dispatcher
from pythonosc import osc_server

def switch_cameras_handler(unused_addr, args):
    cam1, cam2 = args
    try:
        subprocess.check_call(['rosservice', 'call', '/{}/switch_cameras'.format(cam1)])
        subprocess.check_call(['rosservice', 'call', '/{}/switch_cameras'.format(cam2)])
    except subprocess.CalledProcessError as e:
        print("Service call failed: %s" % e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="192.168.1.131", help="The IP to listen on")
    parser.add_argument("--port", type=int, default=20000, help="The port to listen on")
    parser.add_argument("--cam1", default="usb_cam1", help="The first camera node name")
    parser.add_argument("--cam2", default="usb_cam2", help="The second camera node name")
    args = parser.parse_args()

    disp = dispatcher.Dispatcher()
    disp.map("/switch_cameras", switch_cameras_handler, args.cam1, args.cam2)

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), disp)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()