#!/bin/sh
ExtensionVersion=""
if [ -f /usr/local/bin/RemoteUpdateManager  ]; then
    chmod +x /usr/local/bin/RemoteUpdateManager
    S_VERSION=$(/usr/local/bin/RemoteUpdateManager -h | grep version | cut -d ':' -f2 | cut -d ' ' -f2 2>/dev/null )
    ExtensionVersion="${S_VERSION}"
elif [ -a /usr/sbin/RemoteUpdateManager ]; then
    S_VERSION="Pre 2015.5 Release"
    ExtensionVersion="${S_VERSION}"
fi
echo "<result>$ExtensionVersion</result>"
