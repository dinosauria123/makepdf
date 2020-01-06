# -*- coding: utf-8 -*-

import base64
import json
import os
import codecs
import sys
from requests import Request, Session
from io import BytesIO
from PIL import Image

args = sys.argv

filename = args[1]

def pil_image_to_base64(pil_image):
    buffered = BytesIO()
    pil_image.save(buffered, format="PNG")
    str_encode_file = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return str_encode_file

def recognize_image(pil_image):
        str_encode_file = pil_image_to_base64(pil_image)
        str_url = "https://vision.googleapis.com/v1/images:annotate?key="
        str_api_key = args[2]
        str_headers = {"Content-Type": "application/json"}
        str_json_data = {
            "requests": [
                {
                    "image": {
                        "content": str_encode_file
                    },
                    "features": [
                        {
                            "type": "TEXT_DETECTION",
                            "maxResults": 2048
                        }
                    ]
                }
            ]
        }

        obj_session = Session()
        obj_request = Request("POST",
                              str_url + str_api_key,
                              data=json.dumps(str_json_data),
                              headers=str_headers
                              )
        obj_prepped = obj_session.prepare_request(obj_request)
        obj_response = obj_session.send(obj_prepped,
                                        verify=True,
#                                        timeout=60
                                        )

        if obj_response.status_code == 200:
            with codecs.open(args[1] + ".json", "w", "utf-8") as outfile:
                dump=json.dumps(obj_response.json(), indent=2, ensure_ascii=False)
                outfile.write(dump)
                
if __name__ == "__main__":
    image_path = filename
    pil_image = Image.open(image_path)
    recognize_image(pil_image)
