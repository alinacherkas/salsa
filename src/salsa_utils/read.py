# standard packages
import json
import pkgutil



def read_annotations():
    data = pkgutil.get_data(__name__, "data/annotations.json")
    annotations = json.loads(data)
    return annotations
