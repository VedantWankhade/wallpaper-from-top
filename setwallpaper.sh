#!/bin/bash

# TODO:
# 1. Separate generating top output into different script
# 2. Generate top output and wallapaper each time
# 3. Setting wallpaper automatically from Gnome DE

########################### this doesn't seem to work yet ##########################
# create new top output
#echo 'Fetching process information..'
#top -b -n 1 > top.out
#
## generate new wallpaper
#echo 'Creating new wallpaper'
#
#sleep 10
#python ./generate_word_cloud.py
####################################################################################

echo 'Setting up wallpaper'
echo 'Please wait...'

# reference to setting kde plasma wallpaper from terminal: https://superuser.com/questions/488232/how-to-set-kde-desktop-wallpaper-from-command-line

# hardcoded path to wallpaper
qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = "org.kde.image";d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");d.writeConfig("Image", "/home/vedant/projects/wallpaper-from-top/wc_wall.png")}'
echo 'Wallpaper set successfully'