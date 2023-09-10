# standard packages
import os
import random
from pathlib import Path


def write_splits(
        image_dir: str,
        output_dir: str,
        test_size: int = 300,
        val_size: int = 300,
        seed: int = None
):
    image_paths = sorted(Path(image_dir).glob('*.jpeg'))
    if seed is not None:
        random.seed(seed)
    random.shuffle(image_paths)
    print(f'Found {len(image_paths)} images')

    splits = [
        (0, test_size, 'test'),
        (test_size, test_size + val_size, 'val'),
        (test_size + val_size, len(image_paths), 'train')
    ]
    for start, end, split in splits:
        file_path = os.path.join(output_dir, f'image_paths_{split}.txt')
        with open(file_path, 'w') as file:
            for image_path in image_paths[start:end]:
                file.write(str(image_path) + '\n')
        print(f'Created {file_path} with {len(image_paths[start:end])} image paths')
    
    
def write_labels(annotations: dict, output_dir: str, exclude_category_ids: list[int] = None):
    if os.path.exists(output_dir):
        raise Exception('Directory already exists.')
    os.mkdir(output_dir)

    if exclude_category_ids is not None:
        exclude_category_ids = set(exclude_category_ids)
    
    image_id_dict = {image['id']: image for image in annotations['images']}
    for annotation in annotations['annotations']:
        category_id = annotation['category_id']
        if exclude_category_ids is not None and category_id in exclude_category_ids:
            continue

        image = image_id_dict[annotation['image_id']]
        file_name, _ = os.path.splitext(image['file_name'])
        file_path = os.path.join(output_dir, f'{file_name}.txt')

        with open(file_path, 'w') as file:
            x, y, w, h = annotation['bbox']
            file.write(f'{category_id} {x} {y} {w} {h}\n')
    return True
