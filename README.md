# Images to GIF

A simple Python script to convert multiple images into a single animated GIF. Supports `.jpeg`, `.jpg`, and `.png` formats.

## Features

- Automatically sorts images by filename (numeric order if filenames are numbers)
- Supports JPEG, JPG, and PNG images
- Generates a looping animated GIF
- Custom frame duration via command line argument

## Usage

1. Place your images in the same folder as the script
2. Run the script:

```bash
python image_to_gif.py
```

## Optional Arguments

`--tempo` Sets frame duration in milliseconds. Default is 100.

```bash
python image_to_gif.py --tempo 200
```
