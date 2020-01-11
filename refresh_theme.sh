#!/bin/bash

FLEX_LIB_PATH="$HOME/first_static/lib/python3.5/site-packages/pelican/themes/Flex"
FLEX_THEME_PATH="$HOME/first_static/second_Site/themes/Flex"
echo "Deleting Theme"
rm -rf "$FLEX_LIB_PATH"
sleep 2

echo "Installing Theme"
pelican-themes -i "$FLEX_THEME_PATH"

make devserver