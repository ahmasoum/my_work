# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import tensorflow as tf
import os
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="inter path to input directory ")
ap.add_argument("-n", "--name", required=True,
	help="inter name of output folder name")


args = vars(ap.parse_args())


input_dir=args["input"]
output_name=args["name"]

convert_dir= input_dir +'/'+output_name
os.mkdir(convert_dir) 

params = tf.experimental.tensorrt.ConversionParams(
    precision_mode='FP32')
converter = tf.experimental.tensorrt.Converter(
                                                input_saved_model_dir=input_dir,
                                                conversion_params=params)
converter.convert()
converter.save(convert_dir)

######################## correct for srving ###################################

"""os.environ["Home"] = pb_dir

tensorflow_model_server \
  --rest_api_port=8501 \
  --model_name=saved_model.pb \
  --model_base_path=/home/faraadid/pb_dir 
"""
















