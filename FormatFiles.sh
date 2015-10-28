#!/bin/bash
find ./ -name "*.recipe" -exec plutil -convert xml1 {} \;
find ./ -name "*.xml" -exec plutil -convert xml1 {} \;
