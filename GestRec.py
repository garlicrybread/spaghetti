#!/usr/bin/python3

import json
import os
from pprint import pprint


class GestureRecognition:
	def __init__(self, openpose_bin):
		self.openposeDir = openpose_bin

	def execute(self, input_file_dir, output_file_dir):
		os.system("streamer -f jpeg -o examples/Sawyer_GesRec/input_dir/webcam.jpeg -c /dev/video1")
		os.system(self.openposeDir + " --image_dir " + input_file_dir + " --write_keypoint_json " + output_file_dir + " --write_images " + output_file_dir)

		data = json.load(open(os.path.join(output_file_dir, "webcam_keypoints.json")))


		elbowR = data["people"][0]["pose_keypoints"][9]
		handR = data["people"][0]["pose_keypoints"][12]
		elbowL = data["people"][0]["pose_keypoints"][18]
		handL = data["people"][0]["pose_keypoints"][21]

		# direction will be positive if pointing right and negative if pointing left
		DirR = elbowR - handR
		DirL = elbowL - handL

		# Find which absolute distance is greater --> this will be the actual
		# direction that the user is pointing
		if(abs(DirL) <= abs(DirR)):
			# pointing right is given value of 0
			this_way = 0
		else:
			#pointing left is given value of 1
			this_way = 1

		pprint("Direction: " + str(this_way))

if __name__ == "__main__":
	thing = GestureRecognition(os.path.abspath("./build/examples/openpose/openpose.bin"))
	thing.execute("examples/Sawyer_GesRec/input_dir","examples/Sawyer_GesRec/output_dir")

