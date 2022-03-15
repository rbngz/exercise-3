import subprocess
import urllib
import requests
from task2 import readfile, query_map

DARKNET_PATH = "customYOLOv4/"
GRAPH_URL = "https://graphdb.interactions.ics.unisg.ch/repositories/was-assignment-3"
USER = "was-students"
PASSCODE = "assignment-3-is-fun"
QUERIES_PATH = "queries/"

test_img = "test.png"

elements = {
    "BlindStateUp": 0,
    "BlindStateDown": 0,
    "LampStateOn": 0,
    "LampStateOff": 0
}


def execute_insert_query(query):
    encoded_query = urllib.parse.quote_plus(query)
    endpoint = GRAPH_URL + "/statements?update=" + encoded_query
    response = requests.post(endpoint, auth=(USER, PASSCODE), verify=True)
    return response.text


output = subprocess.check_output([f'./{DARKNET_PATH}darknet', "detector", "test", f'{DARKNET_PATH}obj.data',
                                  f'{DARKNET_PATH}yolov4-four-obj.cfg', f'{DARKNET_PATH}yolov4-obj_final.weights', test_img])
output_str = str(output)
for key in elements.keys():
    count = output_str.count(key)
    elements[key] = count

print("Following Elements were detected:")
print(elements)

template = ""
with open("queries/insertStateTemplate.rq", 'r') as templatefile:
    template = templatefile.read()

template_elements = []
template_attributes = []

template_bindings = []
for elem, count in elements.items():
    if count > 0:
        if "Blind" in elem:
            print(elem, count)
            for i in range(1, count + 1):
                # Elements
                blind = "?blind{} a was:Blind.".format(i)
                blind_state = "?blindState{} a was:{}.".format(i, elem)

                # Bindings
                blind_bind = "BIND(IRI(CONCAT(\"https://was-course.interactions.ics.unisg.ch/#Blind-\", strUUID())) AS ?blind{})".format(i)
                blind_state_bind = "BIND(IRI(CONCAT(\"https://was-course.interactions.ics.unisg.ch/#{}-\", strUUID())) AS ?blindState{})".format(elem, i)

                # Attributes
                has_blind = "?room was:hasBlind ?blind{}.".format(i)
                has_blind_state = "?blind{} was:hasBlindState ?blindState{}.".format(
                    i, i)

                template_elements += [blind, blind_state]
                template_bindings += [blind_bind, blind_state_bind]
                template_attributes += [has_blind, has_blind_state]
        if "Lamp" in elem:
            for i in range(1, count + 1):
                # Elements
                lamp = "?lamp{} a was:Lamp.".format(i)
                lamp_state = "?lampState{} a was:{}.".format(i, elem)

                # Bindings
                lamp_bind = "BIND(IRI(CONCAT(\"https://was-course.interactions.ics.unisg.ch/#Lamp-\", strUUID())) AS ?lamp{})".format(i)
                lamp_state_bind = "BIND(IRI(CONCAT(\"https://was-course.interactions.ics.unisg.ch/#{}-\", strUUID())) AS ?lampState{})".format(elem, i)

                # Attributes
                has_lamp = "?room was:hasLamp ?lamp{}.".format(i)
                has_lamp_state = "?lamp{} was:hasLampState ?lampState{}.".format(
                    i, i)

                template_elements += [lamp, lamp_state]
                template_bindings += [lamp_bind, lamp_state_bind]
                template_attributes += [has_lamp, has_lamp_state]

template = template.replace("[elements]", "\n".join(template_elements))
template = template.replace("[attributes]", "\n".join(template_attributes))
template = template.replace("[bindings]", "\n".join(template_bindings))

print("Executing insert statement")
execute_insert_query(template)
execute_insert_query(readfile(QUERIES_PATH + query_map["clear"]))
