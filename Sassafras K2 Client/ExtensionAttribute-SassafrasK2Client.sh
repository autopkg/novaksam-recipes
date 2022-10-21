#!/bin/sh
ExtensionVersion=""
if [ -f /Library/KeyAccess/KeyAccess.app/Contents/Info.plist ]; then
	ExtensionVersion=$(defaults read /Library/KeyAccess/KeyAccess.app/Contents/Info.plist CFBundleShortVersionString)
fi

echo "<result>$ExtensionVersion</result>"

exit 0
