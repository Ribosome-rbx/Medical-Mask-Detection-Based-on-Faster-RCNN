import torchvision
import torch
from torchvision import transforms, datasets, models
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from PIL import Image
import cv2
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

model_path = r'C:\Users\11270\Downloads\Epoch_24_model.pt'

def get_model_instance_segmentation(num_classes): 
    # load an instance segmentation model pre-trained pre-trained on COCO 
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True) 
    # get number of input features for the classifier 
    in_features = model.roi_heads.box_predictor.cls_score.in_features 
    # replace the pre-trained head with a new one 
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes+1) 
    # plus background 
    return model

def gain_box_score(im, preds):
    """Draw detected bounding boxes."""
    if  len(preds[0]) == 0:
        cv2.imshow("Video detection", im)
    else:
        for pred in preds:
            for i, box_label in enumerate(zip( pred["boxes"], pred["labels"] )):
                box, label = box_label
                xmin, ymin, xmax, ymax = box
#--------------------  Create a Rectangle patch -----------------------      
                if label==1:
                    class_name='with_mask'
                    color = (0, 255, 0)
                elif label==2:
                    class_name='without_mask'
                    color = (0, 0, 255)
                elif label==3:
                    class_name='mask_worn_improperly'
                    color = (255, 255 ,0)
                score = pred['scores'][i]
#---------------------  Bounding Box painting --------------------------      
                if score > 0.65:
                    cv2.rectangle(im, (xmin, ymin), (xmax, ymax), color, 1)  
                    cv2.putText(im, str(class_name)+str(round(score.item(),2)), (xmin,int(ymax-ymax/20)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1) #print class name
                    cv2.imshow("Video detection",im)
                    print('*****', 'Bbox:', i , '*****' )
                    print('Class: ', str(class_name))
                    print('Scores: ', str(round(score.item(),2)))
                    print('boxes: ',f'{int(xmin)}, {int(ymin)}, {int(xmax)}, {int(ymax)}')
                    print('image shape: ', im.shape)  
                else:
                    cv2.imshow("Video detection", im)
            print('********************','\n')

model = get_model_instance_segmentation(3)
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model.load_state_dict(torch.load(model_path, map_location = device))
model.to(device)

