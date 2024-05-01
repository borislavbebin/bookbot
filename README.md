# BookBot

BookBot is a simple Python script designed to analyze text files, specifically books, to provide insights into the usage of words and character frequencies. It reads a book from a text file and reports the total number of words and the frequency of each unique character.

## Features

- Count the total number of words in a text file.
- Analyze and count the frequency of each unique character in the text.
- Generate a report that lists these statistics for easy review.

## Installation

No installation is necessary other than having Python installed on your system. BookBot runs as a standalone Python script. Ensure you have Python version 3.x installed on your system.

## Usage

To use BookBot, follow these simple steps:

1. ure your book text file is in a subdirectory named books/ from where you run the script. For example, your directory should look something like this:
    ```bash
    /path/to/your/script/books/frankenstein.txt
    ```

2. Run the script using Python from the command line:
    ```bash
    python bookbot.py
    ```

3. View the output directly in your command line interface.

## Example Output
```bash
--- Begin report of books/frankenstein.txt ---
4316 words found in the document
The 'e' character was found 1152 times
The 't' character was found 792 times
...
--- End report ---
```

## License
This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

## Acknowledgements
- This project was build while working on the BACK-END DEVELOPER in boot.dev