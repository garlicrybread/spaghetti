# Capture image from webcam
streamer -f jpeg -o examples/Sawyer_GesRec/RorL/webcam.jpeg

# Process image using openpose
./build/examples/openpose/openpose.bin --image_dir examples/Sawyer_GesRec/RorL --write_keypoint_json examples/Sawyer_GesRec/keypoints_RorL --write_images examples/Sawyer_GesRec/rendered_RorL

# Run Python script to find gestures
./examples/Sawyer_GesRec/keypoints_RorL/gesture_recognition.py