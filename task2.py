import requests
import urllib
import csv

GRAPH_URL = "https://graphdb.interactions.ics.unisg.ch/repositories/was-assignment-3"
USER = "was-students"
PASSCODE = "assignment-3-is-fun"
QUERIES_PATH = "queries/"


def print_query_results(sparql_query_results):
    reader = csv.DictReader(sparql_query_results.splitlines(), delimiter=',')
    for elem in reader:
        for key, value in elem.items():
            print(key, value)


def execute_insert_query(query):
    string_query = readfile(QUERIES_PATH + query)
    encoded_query = urllib.parse.quote_plus(string_query)
    endpoint = GRAPH_URL + "/statements?update=" + encoded_query
    response = requests.post(endpoint, auth=(USER, PASSCODE), verify=True)
    return response.text


def execute_get_query(query):
    string_query = readfile(QUERIES_PATH + query)
    encoded_query = urllib.parse.quote_plus(string_query)
    endpoint = GRAPH_URL + "?query=" + encoded_query
    response = requests.get(endpoint, auth=(USER, PASSCODE), verify=True)
    return response.text


def readfile(file_path):
    f = open(file_path, "r")
    string_query = f.read()
    return string_query


query_map = {
    "insert": "insertState.rq",
    "get": "getState.rq",
    "clear": "clear.rq"
}


response = execute_insert_query(query_map["insert"])
print("Inserted elements to DB")

response = execute_get_query(query_map["get"])
print("Elements in DB:")
print_query_results(response)

response = execute_insert_query(query_map["clear"])
print("Removed elements from DB")

response = execute_get_query(query_map["get"])
print("Elements in DB:")
print_query_results(response)
