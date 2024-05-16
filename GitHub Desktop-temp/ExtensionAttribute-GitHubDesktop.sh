#!/bin/sh
ExtensionVersion=""
if [ -f /Applications/GitHub\ Desktop.app/Contents/Info.plist ]; then
	ExtensionVersion=$(defaults read /Applications/GitHub\ Desktop.app/Contents/Info.plist CFBundleVersion)
fi
echo "<result>$ExtensionVersion</result>"

exit 0
