import datetime
import json
import os

import google.protobuf as pbg
import framework_pb2 as framework_pb2


def loadmdl(json_path):
    print('mdl json path : ' + json_path)
    with open(json_path, 'r') as f:
        json_dick = json.load(f)
        # print(json_dick)
        layers = (json_dick['layer'])
        for layer in layers:
            print(layer)


