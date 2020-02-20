#!/usr/bin/python
"""
ANDROID2468
script for post arch install written in python!!!

"""

import os

# installing yay
print("Installing yay")
os.system('git clone https://aur.archlinux.org/yay.git')
os.system('cd yay && makepkg -si')
os.system('cd ..')
os.system('yay -Sy')

# X window system
print("choose an x window system: ")
print("   1. Xwayland")
print("   2. Xorg")
print("   3. none")
xWindow=int(input("?: "))
if xWindow == 1:
    print("Installing Xwayland...")
elif xWindow == 2:
    print("Installing Xorg")
elif xWindow == 3:
    print("X window system not installed, continuing...")
else:
    print("invalid input, continuing...")

# DE install
print("choose a desktop environment: ")
print("Please enter one of the following options: ")
print("   1. gnome")
print("   2. kde")
print("   3. none")

dE=int(input("?: "))

# other app installs
os.system('yay -S waterfox-classic-bin pycharm-community-edition minecraft-launcher xournal')

# touch fix
touch = input("Do you have a touchscreen that stops working after exiting sleep mode? [y/N]: ")
if touch == "y" or touch == "Y":
    print("Installing touch fix...")
    os.system('sudo cp wake_hack.service /etc/systemd/system/')
    os.system('sudo systemctl enable wake_hack.service')
    print("")
else:
    print("")

print("Done!")
