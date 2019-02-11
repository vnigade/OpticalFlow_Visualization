# MIT License
#
# Copyright (c) 2018 Tom Runia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to conditions.
#
# Author: Tom Runia
# Date Created: 2018-08-03

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
import flow_vis
import cv2
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description='Visualize optical flow')
parser.add_argument("flow_dir", help="Optical flow directory")
parser.add_argument("video_name", help="Video name ")
parser.add_argument("--frame_num", type=int, default=1, help="Frame number to be used")

args = parser.parse_args()
flow_dir = args.flow_dir
video_name = args.video_name
frame_num="frame" + "%06d" % (args.frame_num) + '.jpg'

u = cv2.imread(flow_dir + "x/" + video_name + "/" + frame_num, 0) 
v = cv2.imread(flow_dir + "y/" + video_name + "/" + frame_num, 0)
u = np.array(u) 
v = np.array(v)
u = u - np.mean(u)
v = v - np.mean(v)

flow_color = flow_vis.flow_xy_to_color(u, v, convert_to_bgr=False)
plt.imshow(flow_color)
plt.show()
