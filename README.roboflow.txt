
box sortation - v10 2025-02-01 8:29pm
==============================

This dataset was exported via roboflow.com on February 1, 2025 at 1:30 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 502 images.
Boxes are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* 50% probability of vertical flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise, upside-down
* Random rotation of between -45 and +45 degrees
* Random shear of between -37° to +37° horizontally and -45° to +45° vertically
* Random brigthness adjustment of between -37 and +37 percent
* Random exposure adjustment of between -14 and +14 percent
* Random Gaussian blur of between 0 and 6.3 pixels
* Salt and pepper noise was applied to 6.24 percent of pixels

The following transformations were applied to the bounding boxes of each image:
* 50% probability of horizontal flip
* 50% probability of vertical flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise, upside-down
* Random rotation of between -23 and +23 degrees
* Random shear of between -11° to +11° horizontally and -15° to +15° vertically
* Random brigthness adjustment of between -32 and +32 percent
* Random Gaussian blur of between 0 and 7.2 pixels
* Salt and pepper noise was applied to 2.63 percent of pixels


