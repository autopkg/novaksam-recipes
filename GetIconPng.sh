#!/bin/bash
ICON="$1"
PNG="$2" 
sips -s format png "$ICON" -z 128 128 --out "$PNG"
