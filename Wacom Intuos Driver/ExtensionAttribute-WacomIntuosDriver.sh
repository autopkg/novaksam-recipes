#!/bin/bash

ExtensionVersion=""
if [ -f /Applications/Wacom\ Tablet/.Tablet/WacomTabletDriver.app/Contents/Info.plist ]; then
	ExtensionVersion=$(defaults read /Applications/Wacom\ Tablet/.Tablet/WacomTabletDriver.app/Contents/Info.plist CFBundleVersion)
fi

echo "<result>$ExtensionVersion</result>"

exit 0
