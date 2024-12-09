# MidJourney Automation Tool

The MidJourney Automation Tool automates the process of generating images on [MidJourney](https://www.midjourney.com/) using pre-defined prompts. It streamlines the task of submitting prompts in batches and monitors the progress of image generation.

## Features

- **Automated Prompt Submission**: Automatically submits prompts from a file to MidJourney.
- **Batch Processing**: Processes prompts in batches of 10 to manage workflow efficiently.
- **Image Generation Monitoring**: Monitors the status of image generation and waits for completion before proceeding.
- **Chrome Profile Support**: Uses a specific Chrome profile for login persistence and custom settings.
- **Undetected ChromeDriver**: Bypasses detection mechanisms using `undetected_chromedriver`.

## Requirements

- Python 3.7+
- Google Chrome (latest version)
- Required Python libraries:
  - `selenium`
  - `chromedriver_autoinstaller`
  - `undetected-chromedriver`

## Installation

1. **Install Dependencies**:

   ```bash
   pip install selenium chromedriver-autoinstaller undetected-chromedriver
   ```

2. **Set Up Chrome Profile**:

   - Create a Chrome profile named `WhatsappBot`.
   - Navigate to `~\AppData\Local\Google\Chrome\User Data` and ensure the profile exists.

3. **Prepare Prompt File**:

   - Create a text file with your prompts, one prompt per line.
   - Save the file and note its path.

## Usage

1. **Run the Script**:

   Execute the script by running:

   ```bash
   python midjourney_automation.py
   ```

2. **Provide Prompt File**:

   Enter the path to the prompt file when prompted:

   ```
   Enter Prompts File (or drag and drop the file here): /path/to/prompts.txt
   ```

3. **Login to MidJourney**:

   - The script will open the MidJourney website.
   - Login manually and press Enter to continue.

4. **Monitor Progress**:

   - The script will submit prompts in batches of 10.
   - Wait 35 seconds between batches to avoid overloading the system.
   - Image generation status is monitored to ensure completion.

5. **Completion**:

   Once all prompts are processed, the browser will close automatically.

## Sample Prompt File

```
Generate a serene sunset over mountains.
Create a futuristic cityscape.
Illustrate a dragon in a medieval setting.
A cozy cabin in the woods during winter.
```

## Notes

- Ensure the ChromeDriver version matches your installed Chrome version. The script auto-installs the correct version.
- Allow sufficient time for each batch to complete to avoid errors or delays.
- If an error occurs during image generation, it will be logged in the console.

## Limitations

- Manual login is required for accessing MidJourney.
- The script depends on MidJourney’s website layout and may break if the site changes.
- Network latency and server response times may impact performance.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributions

Contributions, suggestions, and feature requests are welcome! Please open an issue or submit a pull request on GitHub.

