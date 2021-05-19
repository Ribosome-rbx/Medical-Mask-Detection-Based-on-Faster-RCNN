{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Real-time Medical Mask Detection Based on Faster RCNN\n",
    "This is an official implementation of blog: website-under-construction\n",
    "\n",
    "## Dataset\n",
    "We use a small dataset [Face Mask Detection](https://www.kaggle.com/andrewmvd/face-mask-detection), found available on Kaggle. In this dataset, we have 853 images belonging to 3 classes ('with mask', 'without mask' and 'masks worn incorrectly'). And the whole dataset is stored in `data_augmentation/input`.\n",
    "## Data Augmentation\n",
    "With files(images and annotations) to augment put in `input/`(Do not create sub directories). Change the **INPUT_DIR** and **OUTPUT_DIR** in `augment.py` to corresponding paths. **AUGMENT_SIZE** decides haw many augmented images will be produced from one original image.\n",
    "```bash\n",
    "INPUT_DIR = '../data_augmentation/input'\n",
    "OUTPUT_DIR = '../data_augmentation/output'\n",
    "AUGMENT_SIZE = 4\n",
    "```\n",
    "Run script:\n",
    "```bash\n",
    "python ../data_augmentation/augment.py\n",
    "```\n",
    "Augmented images and annotations are generated in `output/`.\n",
    "## Requirements\n",
    "Python 3.8 or later with all [requirements.txt](https://github.com/Ribosome-rbx/Medical-Mask-Detection-Based-on-Faster-RCNN/blob/master/requirements.txt) dependencies installed, including `torch>=1.7`. To install run:\n",
    "```bash\n",
    "pip install -r requirements.txt\n",
    "```\n",
    "## Train\n",
    "Open [mask-fasterrcnn.ipynb](https://github.com/Ribosome-rbx/Medical-Mask-Detection-Based-on-Faster-RCNN/blob/master/mask-fasterrcnn.ipynb) with Colab. \n",
    "Change **data_path** and **output_path** in `augment.py` to corresponding paths, and run blocks in the notebook.\n",
    "```bash\n",
    "data_path = r'../data_augmentation/output'\n",
    "output_path = r'../results'\n",
    "```\n",
    "\n",
    "## Real-time Mask Detection\n",
    "Since colab cannot connect to the local camera on your computer, you have to build a local environment. After that, change **model_path** to corresponding local path:\n",
    "```bash\n",
    "model_path = r'C:\\Downloads\\Epoch_24_model.pt'\n",
    "```\n",
    "Run script:\n",
    "```bash\n",
    "python C:\\Downloads\\Medical-Mask-Detection-Based-on-Faster-RCNN\\real-time\\camera.py\n",
    "```\n",
    "However, the processing speed is much slower than our expectation, which only achieves to detect one frame for each five seconds. The way for feeding frame into the model have a lot of room to be optimized. For more details, please check the source code."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
