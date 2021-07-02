#!/bin/bash

echo 'Setting up wallpaper\nPlease wait...'

# reference to set kde wallpaper from terminal: https://superuser.com/questions/488232/how-to-set-kde-desktop-wallpaper-from-command-line

qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = "org.kde.image";d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");d.writeConfig("Image", "/home/vedant/projects/wallpaper-from-top/wc_wall.png")}'
echo 'Wallpaper set successfully'