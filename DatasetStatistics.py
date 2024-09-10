# Copyright 2024 (C) antillia.com. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

#
# DatasetStatistics.py

# 2024/02/01 : Toshiyuki Arai antillia.com

import glob
import os
import sys
import traceback
import matplotlib.pyplot as plt
import numpy as np 

class DatasetStatistics:

  def __init__(self, root_dir):
    sub_dirs = os.listdir(root_dir)
    dataset = {}
    n = 1
    self.x = []
    self.y = []
    self.labels = []
    for sub_dir in sub_dirs:
      self.x.append(n)
      n += 1
      self.labels.append(sub_dir +"/images")
    
      subsub_dirs = os.listdir(root_dir + "/"+ sub_dir)
    
      for subsub_dir in subsub_dirs:
        fullpath = root_dir + "/" +  sub_dir + "/" + subsub_dir
        if subsub_dir == "masks":
           continue
        files = glob.glob(fullpath + "/*.jpg")
        count = len(files)
        self.y.append(count)

    #print(" x     {}".format(self.x))
    #print(" y     {}".format(self.y))
    #print(" label {}".format(self.labels))
   
  def plot(self, title, output_dir):

    fig, ax = plt.subplots()
    plt.bar(self.x, self.y, tick_label=self.labels)
    #self.add_value_label(x, y)
    for i in range(1, len(self.x) + 1):
      plt.text(i, self.y[i - 1], self.y[i - 1], ha="center")

    #ax.legend()
    plt.title(title)
    plt.ylabel("Number of Images")

    #plt.show()
    filename = title + "_Statistics" + ".png"
    output_filepath = os.path.join(output_dir, filename)
    plt.savefig(output_filepath)
    print("=== Saved {}".format(output_filepath))

if __name__ == "__main__":
  try:
    dataset_dir = "./"
    output_dir  = "./"
    print("{}".format(sys.argv))

    if len(sys.argv) == 2:
      dataset_dir = sys.argv[1]
    if not os.path.exists(dataset_dir):
      error = "Not found " + dataset_dir
      raise Exception(error)
    if not os.path.exists(output_dir):
      os.makedirs(output_dir)

    title = os.path.basename(dataset_dir)
    print("--- dataset_dir {}".format(dataset_dir))
    print("--- title       {}".format(title))
    
    statistics = DatasetStatistics(dataset_dir)
    statistics.plot(title, output_dir)

  except:
    traceback.print_exc()
 
