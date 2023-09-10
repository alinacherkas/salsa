# standard packages
import os
from urllib.request import urlretrieve

# utils
from tqdm import tqdm


def download_images(annotations: dict, output_dir: str) -> bool:
    if os.path.exists(output_dir):
        raise Exception('Directory already exists.')
    os.mkdir(output_dir)
    for image in tqdm(annotations['images']):
        _, file_name = os.path.split(image['flickr_url'])
        file_path = os.path.join(output_dir, file_name)
        urlretrieve(url=image['flickr_url'], filename=file_path)
    return True
