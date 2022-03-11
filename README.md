# Exercise 3: Integrating Web Ontologies and Inductive Reasoning

This repository contains everything required for Exercise 3 of the Web-based Autonomous Systems course in Spring Semester 2022.

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
