#!/bin/sh

ExtensionVersion=""

if [ -f /usr/local/bin/appleloops ]; then
	ExtensionVersion=$(/usr/local/bin/appleloops -v | cut -d' ' -f2)
	if [ -f /usr/local/bin/appleLoops.py ]; then
		# Removing the old python based one
		rm -f /usr/local/bin/appleLoops.py
	fi
fi

if [ -f /usr/local/bin/appleLoops.py ]; then
	ExtensionVersion=$(python /usr/local/bin/appleLoops.py --version | cut -d' ' -f3)
fi

echo "<result>$ExtensionVersion</result>"

exit 0
