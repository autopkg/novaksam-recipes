#!/bin/bash
ExtensionVersion=""
# Find all the JDKs
# Cut out the directory slashes from the find command
# Sort the results in reverse order
# Get the first result from the sort
# Cut that value to a "1.8.0_45" format
if [ -d /Library/Java/JavaVirtualMachines ]; then
	JDK_Dir=$(find /Library/Java/JavaVirtualMachines  -d 1 -name "*.jdk" | grep 'temurin' | grep 11 |cut -d '/' -f5 )
	if [ -d /Library/Java/JavaVirtualMachines/$JDK_Dir/Contents/ ]; then
        ExtensionVersion=$(defaults read "/Library/Java/JavaVirtualMachines/$JDK_Dir/Contents/Info.plist" CFBundleVersion)
    fi
fi

echo "<result>$ExtensionVersion</result>"
