# Exercise 3: Integrating Web Ontologies and Inductive Reasoning

Running the different programs for each task is quite straightforward:
```
python3 task2.py
python3 task4.py
python3 task5.py
```

When executing the script for task 5, you will be asked to enter the path to an image. As test, you can enter test.png.
For the illumination goal you can simply enter "darker" and the program will look for actionable steps to make the room darker. Alternatively you can enter "brighter" (or anything else really) and the program will look for steps to make the room brighter.

Example input/output:
```
python3 task5.py
Path to image file: test.png
Illumination goal (darker/brighter): darker
```
```
Following Elements were detected:
{'BlindStateUp': 0, 'BlindStateDown': 5, 'LampStateOn': 2, 'LampStateOff': 0}
Executing insert statement
Looking for actionable steps to reach goal...
To fulfill the Illumination Goal, the user needs to switch the states of the following elements:
lamp
https://was-course.interactions.ics.unisg.ch/#Lamp-67289980-f0f8-4d76-bd0b-4c3ca3761c8d
https://was-course.interactions.ics.unisg.ch/#Lamp-bbbc0ded-c287-4b59-8473-13702aadb33a

blind

```