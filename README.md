Images to GIF
A simple Python script to convert multiple images into a single animated GIF. Supports .jpeg, .jpg, and .png formats.

Features
Automatically sorts images by filename numeric order if filenames are numbers.
Supports JPEG, JPG, and PNG images.
Generates a looping animated GIF.
Custom frame duration via command line argument.

Usage
Place your images in the same folder as the script.
Run the script:

python image_to_gif.py

Optional arguments
--tempo Sets frame duration in milliseconds. Default is 80.

Example:

python image_to_gif.py --tempo 200
