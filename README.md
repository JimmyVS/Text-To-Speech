# Text To Speech

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/)
[![pyttsx3](https://img.shields.io/badge/pyttsx3-v2.90-blue)](https://pypi.org/project/pyttsx3/)

## Description

This Python script utilizes the `pyttsx3` library to create a simple Text-to-Speech (TTS) program. The program allows customization of speech output by providing parameters such as text, speech rate, volume, and voice gender.

## Features

- Text-to-Speech functionality
- Adjustable speech rate and volume
- Selection of voice gender

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/text-to-speech.git
    ```

2. Install required dependencies:

    ```bash
    pip install pyttsx3
    ```

3. Run the program:

    ```bash
    python text_to_speech.py
    ```

## Example

```python
# Example usage
SpeakText("Hello, world!", 1, 1, 0)
```

## Configuration

- command: The text to be converted to speech.
- Rate: Adjustment to the speech rate.
- Volume: Volume level of the speech.
- Gender: Voice gender index (0 for male, 1 for female).

## License

This project is licensed under the MIT License - see the LICENSE file for details.


I hope you find this helpful! Happy coding!
