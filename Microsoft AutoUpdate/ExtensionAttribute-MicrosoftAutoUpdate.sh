#!/bin/sh
ExtensionVersion=""
if [ -f /Library/Application\ Support/Microsoft/MAU2.0/Microsoft\ AutoUpdate.app/Contents/Info.plist ]; then
	ExtensionVersion=$(defaults read /Library/Application\ Support/Microsoft/MAU2.0/Microsoft\ AutoUpdate.app/Contents/Info.plist CFBundleVersion)
fi

echo "<result>$ExtensionVersion</result>"

exit 0
