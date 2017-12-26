#!/usr/bin/python3

import json
import os
from pprint import pprint

class GestureRecognition:

	def execute(self):
		os.system("streamer -f jpeg -o examples/Sawyer_GesRec/RorL/webcam.jpeg -c /dev/video1")
		os.system("./build/examples/openpose/openpose.bin --image_dir examples/Sawyer_GesRec/RorL --write_keypoint_json examples/Sawyer_GesRec/keypoints_RorL --write_images examples/Sawyer_GesRec/rendered_RorL")

		dir_path = os.path.dirname(os.path.realpath(__file__))


		#data = json.load(open("arm_right_keypoints.json"))
		data = json.load(open(os.path.join(dir_path, "webcam_keypoints.json")))


		elbowR = data["people"][0]["pose_keypoints"][9]
		handR = data["people"][0]["pose_keypoints"][12]
		elbowL = data["people"][0]["pose_keypoints"][18]
		handL = data["people"][0]["pose_keypoints"][21]

		# direction will be positive if pointing right and negative if pointing left
		DirR = elbowR - handR
		DirL = elbowL - handL

		# Find which abosulte distance is greater --> this will be the actual 
		# direction that the user is pointing
		if(abs(DirL) <= abs(DirR)):
			# pointing right is given value of 0 
			this_way = 0
		else: 
			#pointing left is given value of 1
			this_way = 1

		pprint("Direction: " + str(this_way))

if __name__ == "__main__":
	thing = GestureRecognition()
	thing.execute()

