# standard packages
from copy import deepcopy


def convert_to_yolo(annotations: dict) -> dict:
    """
    Convert bounding boxes to YOLO format.

    Returns a copy of the original annotations object. For details about YOLO format, see
    https://docs.ultralytics.com/yolov5/tutorials/train_custom_data/#12-create-labels_1
    """
    annotations = deepcopy(annotations)
    image_id_dict = {image['id']: image for image in annotations['images']}
    for index, annotation in enumerate(annotations['annotations']):
        image = image_id_dict[annotation['image_id']]
        x, y, w, h = annotation['bbox']
        x = (x + w / 2) / image['width']
        y = (y + h / 2) / image['height']
        w = w / image['width']
        h = h / image['height']
        bbox = [x, y, w, h]
        annotations['annotations'][index]['bbox'] = bbox
    return annotations
