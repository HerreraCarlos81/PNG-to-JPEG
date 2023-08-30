# PNG to JPEG Converter

A simple and efficient utility to batch convert PNG images to JPEG format.

## Description

This script allows users to convert all PNG files from a specified directory (`./pngs` by default) to the JPEG format, saving them into another directory (`./jpegs` by default). After successful conversion, the original PNG files are deleted to save space.

## Features

- **Batch Conversion:** Convert multiple PNG files in one go.
- **Automatic Deletion:** Deletes PNG files after successful conversion.
- **Date Stamping:** Saves JPEG files with a date prefix for easy organization.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.x**: Ensure Python is installed. You can download it [here](https://www.python.org/downloads/).
- **Pillow**: This is the Python Imaging Library fork. Install it using pip:

`pip install pillow`

## Usage

1. Clone this repository:

`git clone HerreraCarlos81/PNG-to-JPEG`

2. Navigate to the directory:

`cd PNG-to-JPEG`

3. Place all the PNG files you want to convert in the `./pngs` directory.

4. Run the script:

`python main.py`

5. Check the `./jpegs` directory for the converted JPEG files.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
