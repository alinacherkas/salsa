# standard packages
import json
import pkgutil


def read_annotations() -> dict:
    """
    Read SALSA annotations in distributed in COCO format.
    """
    data = pkgutil.get_data(__name__, "data/annotations.json")
    annotations = json.loads(data)
    return annotations
