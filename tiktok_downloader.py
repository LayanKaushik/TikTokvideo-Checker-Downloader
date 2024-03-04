# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import time
import requests
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen

def checkVideoExistence(url):
    """
    Checks if a given video URL is available.
    
    Parameters:
        url (str): The URL of the video to check.
        
    Returns:
        str: 'Video currently unavailable' if the video is unavailable, 'Available' otherwise.
    """
    
    # Cookies required to bypass the site's security checks
    cookies = {
        'cf_clearance': 'yRvOa2.5O4QnhOze9jMpzsFK6c6xIlz5HQ7eMaTrr.c-1707692221-1-AWHyZr4o5oJZDenx03Kshq2hASyWBKCa7vNnuyBrdgTCpQu8gBXa8BarIIAc2BrvcvmVXkr4KzCZLeWS4V/79Io=',
    }
    
    # Headers to simulate a request from a web browser
    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"121.0.6167.161"',
        'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.161", "Chromium";v="121.0.6167.161"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }
    
    # Parameters for the POST request
    params = {
        'url': 'dl',
    }
    
    # Data to be sent in the POST request
    data = {
        'id': url,
        'locale': 'en',
        'tt': 'eEx5VnE_',
    }

    # Generate a random sleep time, clipped to the range [10, 15], done to avoid locking out
    sleep_time = np.clip(np.random.normal(12.5, 5), 10, 15)
    time.sleep(sleep_time)
    
    # Make the POST request to check video availability
    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    
    # Parse the HTML response
    downloadSoup = BeautifulSoup(response.text, "html.parser")
    
    # Extract the text content from the parsed HTML
    html_content = downloadSoup.get_text()
    
    # Check if the error message is in the HTML content
    if 'Error code: Video currently unavailable' in html_content:
        return 'Video currently unavailable'
    else:
        return 'Available'

def downloadVideo(url, id, username, directory='tiktok_videos'):
    """
    Downloads a video from a given URL and saves it to a specified directory.
    
    Parameters:
        url (str): The URL of the video to download.
        id (str): The ID of the video.
        username (str): The username of the video's uploader.
        directory (str, optional): The directory where the video will be saved. Defaults to 'tiktok_videos'.
    """
    
    # Cookies required to bypass the site's security checks
    cookies = {
        'cf_clearance': 'yRvOa2.5O4QnhOze9jMpzsFK6c6xIlz5HQ7eMaTrr.c-1707692221-1-AWHyZr4o5oJZDenx03Kshq2hASyWBKCa7vNnuyBrdgTCpQu8gBXa8BarIIAc2BrvcvmVXkr4KzCZLeWS4V/79Io=',
    }
    
    # Headers to simulate a request from a web browser
    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"121.0.6167.161"',
        'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.161", "Chromium";v="121.0.6167.161"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }
    
    # Parameters for the POST request
    params = {
        'url': 'dl',
    }
    
    # Data to be sent in the POST request
    data = {
        'id': url,
        'locale': 'en',
        'tt': 'eEx5VnE_',
    }

    # Generate a random sleep time, clipped to the range [10, 15], done to avoid locking out
    sleep_time = np.clip(np.random.normal(12.5, 5), 10, 15)
    time.sleep(sleep_time)
    
    # Make the POST request to get the download link
    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    
    # Parse the HTML response
    downloadSoup = BeautifulSoup(response.text, "html.parser")
    
    # Extract the download link and video title
    downloadLink = downloadSoup.a["href"]
    videoTitle = downloadSoup.p.getText().strip()
    
    # Open the video URL for downloading
    mp4File = urlopen(downloadLink)
    
    # Save the video to the specified directory
    with open(f"{directory}/{id}_{username}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break
