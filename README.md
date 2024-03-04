# TikTok Video Checker & Downloader

This tool enables users to verify the public availability of TikTok videos and download them using a specified URL. It performs web requests to TikTok's servers to retrieve video information and facilitates content downloading.

## Features

- **Check Video Availability:** Determines if a TikTok video is publicly available online.
- **Download Videos:** Downloads TikTok videos using their URL if they are available publicly.

## Prerequisites

Before you start using this tool, ensure you have Python installed on your system. This tool has been tested with Python 3.8 and above. Additionally, you will need to manually obtain cookies and headers as described in the "Getting Cookies and Headers" section below.

## Getting Cookies and Headers

To ensure this tool functions correctly, you must update the cookies and headers to reflect the current requirements of TikTok's web interface. Follow these steps:

1. Visit [ssstik.io](https://ssstik.io).
2. Open your browser's Developer Tools (F12 or right-click -> "Inspect").
3. Navigate to the "Network" tab.
4. Paste any TikTok video link in the input box on ssstik.io and click the download button.
5. Look for a network request named `abc?url=dl` in the Developer Tools.
6. Right-click on the request and choose "Copy as cURL (bash)".
7. Visit [curlconverter.com](https://curlconverter.com/) and paste the copied cURL command.
8. Convert the command to Python code to update the `cookies` and `headers` variables in your script accordingly.

## Installation

Clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/<your-username>/TikTok-Video-Downloader.git
cd TikTok-Video-Downloader
pip install -r requirements.txt
```

Just replace `<your-username>` with your actual GitHub username.

## How to Use

1. **Check Video Existence:** Provide a TikTok video URL to the script to check its availability.
2. **Download Video:** If the video is available, use the script to download it. Refer to `playground.ipynb` for example code, or create your own script based on the provided functionality.

## Contribution

Contributions are welcome! If you have improvements or bug fixes, please fork the repository and submit a pull request with your changes. Follow the existing code style and document any new functions or changes you make.

## Disclaimer

This tool is intended for educational and research purposes only and is not an official TikTok downloader. It uses third-party websites to check and download TikTok videos. Ensure you are compliant with TikTok's terms of service and copyright laws in your jurisdiction and ensure you have the right to download content from TikTok and use this tool responsibly and ethically. The developer is not responsible for any misuse of this tool or legal repercussions that come from downloading copyrighted content without permission.
