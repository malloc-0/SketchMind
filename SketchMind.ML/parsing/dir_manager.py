#!/usr/bin/env python

import os
import uuid
import json

current_path = os.path.dirname(os.path.abspath(__file__))


def get_res_dir(name):
    if name[-4:] == ".jpg":
        return os.path.abspath(os.path.join(current_path, "/img/" + name + ".jpg"))
    else:
        return os.path.abspath(os.path.join(current_path, "/img/" + name + ".jpg"))


def get_tmp_dir(is_erode=False):
    if is_erode:
        return os.path.abspath(os.path.join(current_path, "/tmp/erode_" + uuid.uuid4() + ".jpg"))
    else:
        return os.path.abspath(os.path.join(current_path, "/tmp/thresh_" + uuid.uuid4() + ".jpg"))


def get_result_dir(name="result"):
    return os.path.abspath(os.path.join(current_path, "/result/" + name + "_" + uuid.uuid4() + ".jpg"))


def dump_json(dir, json_content):
    with open(dir, 'w', encoding='utf-8') as json_file:
        json.dump(json_content, json_file, ensure_ascii=False)
    json_file.close()
