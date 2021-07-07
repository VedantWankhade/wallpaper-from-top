#!/bin/bash

# TODO:
# 1. Separate generating top output into different script ####### Done #############
# 2. Generate top output and wallpaper each time
# 3. Setting wallpaper automatically from Gnome DE

# get process information
echo "Fetching process information"
sh ./generate_top_output.sh
echo "done"

# generate new wallpaper
echo 'Creating new wallpaper'
python ./generate_word_cloud.py
echo "done"
echo 'Setting up wallpaper'

# gwenview ./wc_wall.png

# reference to setting kde plasma wallpaper from terminal: https://superuser.com/questions/488232/how-to-set-kde-desktop-wallpaper-from-command-line

########################### doesn't work correctly yet ##########################
# only sets the wallpaper if the current wallpaper is not set by the command below
# in other words this script works only once

# hardcoded path to wallpaper
qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript "var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = 'org.kde.image';d.currentConfigGroup = Array('Wallpaper', 'org.kde.image', 'General');d.writeConfig('Image', '$(pwd)/wc_wall.png')}"
#################################################################################

echo 'Wallpaper set successfully'
