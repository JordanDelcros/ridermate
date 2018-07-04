# ridermate
Rider mate


## install

 - Burn raspbian lite image on SSD
 - add empty `ssh` file at SD root
 - add `wpa_supplicant.conf` file with:
```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
  ssid="WIFI_SSID"
  scan_ssid=1
  psk="WIFI_PASSWORD"
  key_mgmt=WPA-PSK
}
 ```
 
  - connect via `ssh pi@raspberrypi.local`
  - `sudo raspi-config`
  - into `Interfacing Options` enable the camera (Yes then finish)
  - test the camera with `vcgencmd get_camera` (output must be `supported=1 detected=1`)
  - `sudo apt-get update`
  - `sudo apt-get upgrade`
