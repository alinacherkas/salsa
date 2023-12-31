# SALSA
Selection of Adjusted Litter Scene Annotations (SALSA) is a new image dataset for object detection that focuses on litter. This dataset is currently under active development.

## Overview

SALSA is designed to further research in the area of computer vision for litter detection. The dataset is a mix of selected and adjusted annotations of images from [TACO](http://tacodataset.org) and new annotations of images from [OpenLitterMap](https://openlittermap.com). SALSA contains 2569 images with 8356 annotations for objects across 10 categories. Images represent a diverse set of litter objects in the wild, i.e., outdoor images of litter in various natural environments. The annotations are provided in [COCO format](https://cocodataset.org/#format-data) in [annotations.json](./src/salsa_utils/data/annotations.json). Images are distributed via Azure Blob Storage (in West Europe Region). SALSA dataset, i.e., `annotations.json`, is made available under the [Open Database License](http://opendatacommons.org/licenses/odbl/1.0/). `salsa-utils` package is distributed under Apache License.

> [!IMPORTANT]  
>  I do not own the copyright of the images distributed via the Blob Storage. Use of the images must abide by respective image licenses specified for each image in [annotations.json](./src/salsa_utils/data/annotations.json). The users of the images accept full responsibility for the use of the dataset, including but not limited to the use of any copies of copyrighted images that they may create from the dataset.

## Getting Started

`salsa-utils` is a Python package designed to facilite work with SALSA dataset. You can install the package from GitHub using

```bash
pip install git+https://github.com/alinacherkas/salsa.git
```

You can either use Python or CLI interface to download the complete dataset in YOLO format with just a couple of lines of code.

```python
import salsa_utils as salsa

# transform annotations, download images, write labels and dataset config file all in one go
salsa.prepare_salsa()
```

Alternatively, you can run the below code from the command line to achieve the same result:

```bash
python -m salsa_utils
```

By default, data is saved to `./datasets` while `salsa.yaml` is written to the current working directory.

## Descriptive Statistics

Out of 2569 images in the dataset, about 48% come directly from TACO while the rest are new images obtained from OpenLitterMap. For all TACO images, bounding boxes were checked and adjusted if needed, while categories were manually recoded and validated according to the new label scheme with 10 categories. About 59% of annotations appear in newly annotated images from OpenLitterMap. The distribution of objects across the 10 classes is shown below.


![Figure 1. Distribution of Annountations Across Categories](https://github.com/alinacherkas/salsa/assets/51997505/a586a1d2-912c-4b84-956e-dd5cea3334ef)

Litter objects in images appear in different positions and various sizes. The distribution of bounding box areas across by object category is displayed in the figure below.

![Figure 2. Normalised Distribution of Bounding Box Areas by Category](https://github.com/alinacherkas/salsa/assets/51997505/9ddd259f-7208-4563-8b47-0d1705dd57d6)


### Comparison with TACO

| Criterion | TACO  | SALSA |
| - | ------------- | ------------- |
|Year| 2020  | 2023  |
|Number of Images| 1500 (official version)  | 2569 (1325 taken from TACO and 1244 collected from OpenLitterMap)  |
|Number of Annotations|4784|8356 (3396 adjusted from/added to TACO and 4960 annotated from OpenLitterMap)|
|Number of Categories|60|10|
|Number of Supercategories|28|1|
|Bounding Boxes|Yes|Yes|
|Instance Segmentation|Yes|Not yet|
|Source of Annotations|Crowdsourced|Manually Curated|


### Examples

![Figure 3. Examples of Annotated Images](https://github.com/alinacherkas/salsa/assets/51997505/22f1ac55-e430-4265-b4c8-785bcfbce08a)
