#!/bin/sh
CFBundleVersion=""
PlistPath="/Applications/ZoomOutlookPlugin/PluginLauncher.app/Contents/Info.plist"
if [ -f "$PlistPath" ]; then
    CFBundleVersion=$(defaults read "$PlistPath" CFBundleShortVersionString | cut -d' ' -f1)
fi
echo "<result>$CFBundleVersion</result>"
exit 0
