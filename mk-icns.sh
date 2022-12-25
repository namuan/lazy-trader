#!/bin/bash

# Set the list of dimensions
dimensions=(72x72 96x96 128x128 144x144 152x152 192x192 384x384 512x512)

# Loop through the dimensions
for dimension in "${dimensions[@]}"; do
  # Generate the output file name
  output_file="assets/icons/icon-$dimension.png"

  # Run the convert command
  convert docs/app-icon.png -resize $dimension $output_file
done
