#!/bin/bash

# get process information
echo "Fetching process information"
sh ./generate_top_output.sh
echo "done"

# generate new wallpaper
echo 'Creating new wallpaper'
python ./generate_wallpaper.py
echo "done"
echo 'Setting up wallpaper'

# gwenview ./wc_wall.png



echo "Select your desktop environment:"
echo "  1. KDE Plasma"
echo "  2. Gnome"

read de

if [ $de -eq 1 ]; then

# reference to setting kde plasma wallpaper from terminal: https://superuser.com/questions/488232/how-to-set-kde-desktop-wallpaper-from-command-line

########################### doesn't work correctly yet ##########################
# only sets the wallpaper if the current wallpaper is not set by the command below
# in other words this script works only once

qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript "var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = 'org.kde.image';d.currentConfigGroup = Array('Wallpaper', 'org.kde.image', 'General');d.writeConfig('Image', '$(pwd)/wc_wall.png')}"
echo 'Wallpaper set successfully'
#################################################################################
fi

if [ $de -eq 2 ]; then
  echo "Sorry! This does not yet work for gnome. Set wc_wall.png as wallpaper manually."
fi