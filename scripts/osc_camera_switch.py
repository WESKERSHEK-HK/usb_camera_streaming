#!/usr/bin/env python3

import argparse
from pythonosc import dispatcher
from pythonosc import osc_server
import rospy
from std_srvs.srv import Empty

def switch_cameras_handler(unused_addr, args):
    cam1, cam2 = args
    rospy.wait_for_service('/{}/switch_cameras'.format(cam1))
    rospy.wait_for_service('/{}/switch_cameras'.format(cam2))
    try:
        switch_cam1 = rospy.ServiceProxy('/{}/switch_cameras'.format(cam1), Empty)
        switch_cam2 = rospy.ServiceProxy('/{}/switch_cameras'.format(cam2), Empty)
        switch_cam1()
        switch_cam2()
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="192.168.1.131", help="The IP to listen on")
    parser.add_argument("--port", type=int, default=20000, help="The port to listen on")
    parser.add_argument("--cam1", default="usb_cam1", help="The first camera node name")
    parser.add_argument("--cam2", default="usb_cam2", help="The second camera node name")
    args = parser.parse_args()

    rospy.init_node('osc_camera_switch')

    disp = dispatcher.Dispatcher()
    disp.map("/switch_cameras", switch_cameras_handler, args.cam1, args.cam2)

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), disp)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
