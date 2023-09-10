# standard packages
import os
from urllib.request import urlretrieve

# utils
from tqdm import tqdm

# salsa
from .read import read_annotations


def download_images(output_dir: str) -> bool:
    if os.path.exists(output_dir):
        raise Exception('Directory already exists.')
    os.mkdir(output_dir)
    annotations = read_annotations()
    for image in tqdm(annotations['images']):
        _, file_name = os.path.split(image['flickr_url'])
        file_path = os.path.join(output_dir, file_name)
        urlretrieve(url=image['flickr_url'], filename=file_path)
    return True
