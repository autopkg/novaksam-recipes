#!/bin/sh
ExtensionVersion=""
if [ -f /Library/Frameworks/R.framework/Versions/Current/Resources/Info.plist ]; then
	ExtensionVersion=$(defaults read  /Library/Frameworks/R.framework/Versions/Current/Resources/Info.plist  CFBundleVersion)
fi

echo "<result>$ExtensionVersion</result>"

exit 0
