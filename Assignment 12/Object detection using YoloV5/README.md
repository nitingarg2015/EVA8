## Assignment 10 Object detection using Yolo V5  

### Objectives  
1. Create custom data set with 4 classes
2. Create bounding boxes for those classes
3. Train using Yolo V3
4. Download small YouTube Video
5. Extract frames
6. Detect classes
7. Generate video
8. Upload video

### Approach  
1. I used Yolo V5 model from Ultrlytics to complete this assignment --> !git clone https://github.com/ultralytics/yolov5  
2. Person protection equipment dataset was used with 300 images, and bounding boxes were created on these using labelimg in Yolo compatible format  
3. Unzipped the annotated images into "datasets" folder in the root directory of colab
4. Modified /content/yolov5/data/coco128.yaml file with following details: path: ../datasets/cusdata, train: images, val: images
classes: person, vest, red, blue, white, yellow (removed all other classes)  
5. Installed requirements  
6. Trained the model for 50 epochs with yolov5m.pt weights file: #!python train.py --img 640 --epochs 50 --data coco128.yaml --weights yolov5m.pt  
7. Downloaded a youtube video  
8. Extracted frames from the video using opencv  
9. Ran Yolo V5 detection model on the extracted images: !python detect.py --weights runs/train/exp/weights/best.pt --source /content/clip  
10. Merged images with bounding boxes into a video using opencv  


### Outcomes: Sample images with bounding boxes  
<img width="245" alt="image" src="https://user-images.githubusercontent.com/13360207/228169278-d49270f9-4110-4794-8772-5ec498d4982e.png">
<img width="262" alt="image" src="https://user-images.githubusercontent.com/13360207/228169371-bfa45ce0-4293-4a0d-b61e-3ab29531781b.png">
<img width="260" alt="image" src="https://user-images.githubusercontent.com/13360207/228169505-1a5f67e9-8669-4312-a09d-ef52c9f3c587.png">


