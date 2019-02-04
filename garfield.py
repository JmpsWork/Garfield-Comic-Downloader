"""
Actually I lied this just downloads all of the garfield comics
"""

import requests
import os
from bs4 import BeautifulSoup


def download_comics(url: str, year: int, month: int):
    """Downloads all the images from a website."""
    header = {'User-Agent': 'Script'}
    content = requests.get(url, headers=header)
    print(content.url)
    soup = BeautifulSoup(content.content, 'html.parser')
    images = soup.find_all('img')
    for count, image in enumerate(images):
        image_src = image['src']
        if 'http' not in image_src:
            return
        try:
            print(f'Downloading "{image_src}"...')
            with requests.get(f'{image_src}', headers=header, timeout=10) as img:
                try:
                    path = f'garfield/{year}/{month}'
                    os.makedirs(path)
                except OSError:
                    pass
                with open(f'{path}/comic{year}-{month}-{count}.gif', 'wb') as f:
                    f.write(img.content)
        except Exception as e:
            print(f'Error download {image_src}! {e}')


for year in [year for year in range(1978, 2019)]:
    for month in [month for month in range(1, 13)]:
        download_comics(f'http://pt.jikos.cz/garfield/{year}/{month}', year, month)
