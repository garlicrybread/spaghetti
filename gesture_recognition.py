import json
from pprint import pprint

#data = json.load(open("arm_right_keypoints.json"))
data = json.load(open("arm_out_keypoints.json"))


# Looking for 64.8064 and 26.6664, 195.602 and 230.244
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

pprint(this_way)

pprint(DirR)
pprint(DirL)
# pprint(elbowR)
# pprint(handR)
# pprint(elbowL)
# pprint(handL)
