# Real-time Medical Mask Detection Based on Faster RCNN
This is an official implementation of blog: website-under-construction

## Dataset
We use a small dataset [Face Mask Detection](https://www.kaggle.com/andrewmvd/face-mask-detection), found available on Kaggle. In this dataset, we have 853 images belonging to 3 classes ('with mask', 'without mask' and 'masks worn incorrectly'). And the whole dataset is stored in `data_augmentation/input`.
## Data Augmentation
With files(images and annotations) to augment put in `input/`(Do not create sub directories). Create a `output` folder under directory of '../data_augmentation' with two sub-folders `images` and `annotations` in it. The relative locations of files are as follows：
```bash
|--data_augmentation
   |--util
   |--augment.py
   |--input
   |--output
      |--images
      |--annotations      
```
Change the **INPUT_DIR** and **OUTPUT_DIR** in `augment.py` to corresponding paths. **AUGMENT_SIZE** decides haw many augmented images will be produced from one original image.
```bash
INPUT_DIR = '../data_augmentation/input'
OUTPUT_DIR = '../data_augmentation/output'
AUGMENT_SIZE = 4
```
Run script:
```bash
python ../data_augmentation/augment.py
```
Augmented images and annotations are generated in `output/`.
## Requirements
Python 3.8 or later with all [requirements.txt](https://github.com/Ribosome-rbx/Realtime-Medical-Mask-Detection-Based-on-Faster-RCNN/blob/master/requirements.txt) dependencies installed, including `torch>=1.7`. To install run:
```bash
pip install -r requirements.txt
```
## Train
Open [mask-fasterrcnn.ipynb](https://github.com/Ribosome-rbx/Realtime-Medical-Mask-Detection-Based-on-Faster-RCNN/blob/master/mask-fasterrcnn.ipynb) with Colab. 
Change **data_path** and **output_path** in `augment.py` to corresponding paths, and run blocks in the notebook.
```bash
data_path = r'../data_augmentation/output'
output_path = r'../results'
```

## Real-time Mask Detection
Since colab cannot connect to the local camera on your computer, you have to build a local environment. After that, change **model_path** to corresponding local path:
```bash
model_path = r'C:\Downloads\Epoch_24_model.pt'
```
Run script:
```bash
python C:\Downloads\Medical-Mask-Detection-Based-on-Faster-RCNN\realtime\camera.py
```
However, the processing speed is much slower than our expectation, which only achieves to detect one frame for each five seconds. The way for feeding frame into the model have a lot of room to be optimized. For more details, please check the source code.
## About me
**EDUCATION**: 
+ Bachelor of Communication Engineering (2022.7 Expected)
+ Qiushi Honor College, Tianjin University (TJU)

**CONTACT ME**: 
- E-mail: rongboxiang@tju.edu.cn
- Address: 92 Weijin Road, Tianjin, P.R. China
