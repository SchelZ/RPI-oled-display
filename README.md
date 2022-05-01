# RPI-oled-display
```
Display IPs connected to the linux machine (RPI) by printing the "user": "ip"
This was done on Adafruit 0.96" I2C oled display
```

## Installation
- sudo pip install adafruit-circuitpython-ssd1306

## Or
- sudo pip3 install adafruit-circuitpython-ssd1306

## AND
- sudo apt-get install python3-pil


## Setup 
1. Type this command "sudo raspi-config" and enable under "Interface Options" --> I2C or SPI.
2. Install python modules from above
3. Clone this git into the raspberry 
4. Type in terminal "sudo crontab -e", go to the buttom and write "* * * * * /usr/bin/python /your_path_to_code/get_ips.py" or "* * * * * /usr/bin/python3 /your_path_to_code/get_ips.py"
5. Reboot the system and enjoy (crontab should run your python code every minute)
