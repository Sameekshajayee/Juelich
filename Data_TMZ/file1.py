from os.path import join
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

base= r'C:\Users\samee\Masters Internship\Data_Response_TMZ'
#reading the excel file
xlfile = join(base,'data_tmz.xlsx')
df= pd.read_excel(xlfile)

patient_ID = '0586'

# reading the images

images_path= join(base,'images')
patient_image= join(images_path, 'brainseg_'+ f'{patient_ID}'+'_0000.nii.gz')
sitk_image = sitk.ReadImage(patient_image)
sitk_array = sitk.GetArrayFromImage(sitk_image)
plt.imshow(sitk_array[30,:,:], cmap='gray')
plt.show()

# Predictions

predictions_path= join(base,'predictions')
patient_prediction= join(predictions_path, 'brainseg_'+ f'{patient_ID}'+'.nii.gz')
sitk_prediction= sitk.ReadImage(patient_prediction)
sitk_prediction_array = sitk.GetArrayFromImage(sitk_prediction)
plt.imshow(sitk_prediction_array[40,:,:], cmap='gray')
plt.show()

# Brain Mask

mask_path = join(base, 'brain_masks')
patient_mask = join(mask_path, 'brainseg_'+ f'{patient_ID}' + '_0000_hd_bet_mask.nii.gz')
sitk_mask= sitk.ReadImage(patient_mask)
sitk_mask_array = sitk.GetArrayFromImage(sitk_mask)
plt.imshow(sitk_mask_array[40,:,:], cmap='gray')
plt.show()

import radiomics
from radiomics import base, cShape, deprecated

