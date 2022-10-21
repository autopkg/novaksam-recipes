#!/bin/sh
ExtensionVersion=""
if [ -f /Applications/Skype.app/Contents/Info.plist ]; then
	ExtensionVersion=$(defaults read /Applications/Skype.app/Contents/Info.plist CFBundleVersion)
fi

echo "<result>$ExtensionVersion</result>"

exit 0
