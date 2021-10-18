# RPI-oled-display
```
Display ips connected to the linux machine (RPI) by printing the "user": "ip"
This was done on Adafruit 0.96" I2C oled display
```

## Installation
- pip install Pillow
- pip install 
- pip install RPi.GPIO
- pip install Adafruit_BBIO

## Or
- pip3 install Pillow
- pip3 install 
- pip3 install RPi.GPIO
- pip3 install Adafruit_BBIO

## Setup 
1. Type this command "sudo raspi-config" and enable under "Interface Options" I2C.
2. Install python modules from above
3. Clone this git into the raspberry 
4. Type in terminal "crontab -e", go to the buttom and write "* * * * * /usr/bin/python /your_path_to_code/*.py" or "* * * * * /usr/bin/python3 /your_path_to_code/*.py"
5. Reboot the system and enjoy (crontab should run your python code every minute)
