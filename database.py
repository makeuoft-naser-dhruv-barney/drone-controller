
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import numpy as np
import time


class database_data

    def __init__(self):
        self.API_KEY = "nLKf417RNJc0pBjvbeHXa9spG8d7G3zgffVULmi1nZ5b"
        self.USERNAME = "44a88f8f-23e0-4865-a77b-fc485a24abd0-bluemix"

        self.client = Cloudant.iam(self.USERNAME, self.API_KEY, connect=True)
        self.database = self.client['sensor']
        self.result_collection = Result(self.database.all_docs, include_docs=True)

        # reserve space for graph, 3 attributes & 100 datapoints
        self.graph = np.array((3, 100));
        self.update_graph()

    def update_graph(self):
        time.sleep(2)
        self.result_collection = Result(self.database.all_docs, include_docs=True)
        graph_points = self.result_collection[ : 100]

        # put all points inside a giant matrix
        for i in range(1, 100):
            payload_data = graph_points[i]['payload']['d']
            self.graph[1, i] = payload_data['Temp']
            self.graph[2, i] = payload_data['Pressure']
            self.graph[3, i] = payload_data['Humidity']
        self.update_graph()

    def get_graph(self):
        return self.graph