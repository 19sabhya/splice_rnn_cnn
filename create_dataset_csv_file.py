import numpy as np
import sys
import os
import random


def create_dataset_file(myDir, is_tp_files):
	if is_tp_files:
 		data_csv_file = open("../splice_rnn_cnn/data/spImages.csv", "w")
	else:
		data_csv_file = open("../splice_rnn_cnn/data/auImages.csv", "w")
	format_ = ['.JPG' , '.jpg', 'jpeg', '.png', '.tiff', '.TIFF', '.Tiff', '.Tif', '.TIF', '.tif', '.bmp']
	print(myDir)
	for root, dirs, files in os.walk(myDir, topdown=False):
		for name in files:
			for type_ in format_:
				if name.endswith(type_):
					fullName = os.path.join(root, name)
					data_csv_file.write("%s\n" % (fullName))
					break
  			
	data_csv_file.close()


# load the original image
create_dataset_file('../splice_rnn_cnn/data/Au', 0)
create_dataset_file('../splice_rnn_cnn/data/Sp', 1)

