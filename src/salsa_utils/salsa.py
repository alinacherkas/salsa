# standard packages
import os

# salsa modules
from .read import read_annotations
from .download import download_images
from .transform import convert_to_yolo
from .write import write_labels, write_splits, write_yaml


def prepare_salsa(output_dir: str = 'datasets') -> bool:
    """
    Run all stages of data preparation to create the dataset in YOLO format.

    This is the main function that allows to create a version of the dataset
    suitable for object detection with YOLO. The function downloads images,
    formats labels and splits as well as create a config YAML file.
    """
    salsa_dir = os.path.join(output_dir, 'salsa')
    os.makedirs(salsa_dir)

    image_dir = os.path.join(salsa_dir, 'images')
    label_dir = os.path.join(salsa_dir, 'labels')

    print('Preparing...')
    annotations = read_annotations()
    print('Convering annotations to YOLO format...')
    annotations = convert_to_yolo(annotations=annotations)
    print('Downloading images...')
    download_images(annotations=annotations, output_dir=image_dir)
    print('Writing labels...')
    write_labels(annotations=annotations, output_dir=label_dir)
    print('Creating splits...')
    write_splits(image_dir=image_dir, output_dir=salsa_dir, seed=123)
    print('Creating dataset YAML...')
    write_yaml(annotations=annotations, output_dir=os.curdir)
    print('Done')
    return True
