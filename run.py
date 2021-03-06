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
print("   1. wayland")
print("   2. Xorg")
print("   3. none")
xWindow=int(input("?: "))
if xWindow == 1:
    print("Installing wayland...")
    os.system('yay -S wayland wayland-protocols mesa')
elif xWindow == 2:
    print("Installing Xorg")
    os.system('yay -S xorg xorg-server mesa')
elif xWindow == 3:
    print("X window system not installed, continuing...")
else:
    print("Invalid input, continuing...")

# DE install
print("choose a desktop environment: ")
print("Please enter one of the following options: ")
print("   1. gnome")
print("   2. kde")
print("   3. cinnamon")
print("   4. deepin")
print("   5. none")
dE = int(input("?: "))
if dE == 1:
    print("installing gnome...")
    os.system('yay -S gnome gnome-extra gdm')
    os.system('sudo systemctl enable gdm.service')
elif dE == 2:
    print("Installing kde...")
    os.system('yay -S plasma sddm')
    os.system('sudo systemctl enable sddm.service')
elif dE == 3:
    print("Installing cinnamon...")
    os.system('yay -S cinnamon nemo-fileroller  yay -S lightdm')
    os.system('sudo systemctl enable lightdm.service')
elif dE == 4:
    print("Installing Deepin...")
    os.system('yay -S deepin deepin-extra lightdm')
    os.system('sudo systemctl enable lightdm.service')
elif dE == 5:
    print("No DE installed, continuing...")
else:
    print("Invalid input, continuing...")

# other app installs
os.system('yay -S waterfox-classic-bin pycharm-community-edition minecraft-launcher xournal discord gnome-disk-utility
 ')

# touch fix
touch = input("Do you have a touchscreen that stops working after exiting sleep mode? [y/N]: ")
if touch == "y" or touch == "Y":
    print("Installing touch fix...")
    os.system('sudo cp wake_hack.service /etc/systemd/system/')
    os.system('sudo systemctl enable wake_hack.service')
    print("")
else:
    print("")

# Update system
update = input("Do you want to update your system?[Y/n]: ")
if update == "n" or update == "N":
    print("")
else:
    os.system('yay -Syu')

print("Done!")
