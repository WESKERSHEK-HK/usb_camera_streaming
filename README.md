<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->




<!-- PROJECT LOGO -->

<div align="center">

<h1 align="center">USB Camera Streaming</h3>
<br />
</div>



<!-- ABOUT THE PROJECT -->
## About The Project

  #ROS-Melodic
  This project aims to use rosbridge, websocket and web_video_server to streaming mulitple device camera in the same network.

### Requirments

* ROS Library
  ```sh
  sudo apt-get install ros-melodic-usb-cam ros-melodic-rosbridge-server ros-melodic-web-video-server
  ```

### Installation

1. Clone the repo to your workspace:
   ```sh
   git clone https://github.com/WESKERSHEK-HK/usb_camera_streaming.git
   ```
2. Set ROS Master URI:
   ```sh
   export ROS_MASTER_URI=http://<~~~~>:11311/
   ```
3. Launch rosbridge and web_video_server at ROS MASTER:
   ```sh
   roslaunch rosbridge_server rosbridge_websocket.launch
   rosrun web_video_server web_video_server
   ```
4. Launch usb_cam in different device to publish video topic (make sure use different topic name!!):
   ```sh
   roslaunch usb_cam usb_cam-test.launch
   ```
5. Configure index.html ip, port and topics

6. Run index.html

7. Send OSC command to websocket osc server with address "/switch" to switch videos.


