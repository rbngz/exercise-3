# Exercise 3: Integrating Web Ontologies and Inductive Reasoning

This repository contains everything required for Exercise 3 of the Web-based Autonomous Systems course in Spring Semester 2022.

Here are several notes:

- We have removed the training and validation files as well as the trained weights from this repository because of a github LFS quota problem. They are available here:
  * Training Pictures: https://drive.google.com/file/d/1pG1IQjC7Fi9CTAhQUHmDZqjMeiSjKyhI/view
  * Test Pictures: https://drive.google.com/file/d/1hjBNFfMhI_Bi3Moq4bUuovI0kcbl2YCY/view
  * Yolov4 Weights: https://drive.google.com/file/d/1D20UOBNwUiO_o3mriQTYe4je9vGfREkt/view

- Note that running Darknet on your machine does _neither_ require a GPU _nor_ OpenCV to be installed, i.e. it is perfectly possible for you to clone darknet, set its parameters to GPU=0, OPENCV=0, CUDNN=0, CUDNN_HALF=0 and build it (see the Task 3 tutorial for more information). The only difference in this case is that Darknet will not open a window that visualizes its predictions, but simply give you the predictions on the command line. We still recommend that you set up OpenCV as it is generally useful.



### Project structure
```bash
├── graphDBstarter # kick-off code for Task 2
├── customYOLOv4 # everything needed for Tasks 3 and 4
│   ├── FS22-WAS-Tutorial-Custom-Yolo.ipynb # Tutorial for training your own custom YOLOv4 detector, Task 3
│   ├── obj.data # Configuration of training, Task 3
│   ├── obj.names # Names of detected classes, Tasks 3 and 4
│   ├── yolov4-four-obj.cfg # Configuration of YOLOv4 network for four classes, Task 3
│   ├── obj.zip # Labelled training dataset from the Interactions Laboratory, Task 3
│   ├── test.zip # Labelled validation dataset from the Interactions Laboratory, Task 3
│   ├── generate_train.py # Helper that puts names of training images into a textfile, Task 3
│   ├── generate_test.py # Helper that puts names of test images into a textfile, Task 3
│   └── yolov4-obj_final.weights # Trained YOLOv4 weights for our laboratory environment
└── README.md # this README.md
```
