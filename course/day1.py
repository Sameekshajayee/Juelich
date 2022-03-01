from os.path import join
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

base = r"C:\Users\samee\Masters Internship\mr_pet\mr_pet"

file = "FE1BP469M-BI_0000.nii.gz"


file_path = join(base, file)
sitk_image = sitk.ReadImage(file_path)

sitk_array = sitk.GetArrayFromImage(sitk_image)

plt.imshow(sitk_array[140, :, :], cmap='gray')
plt.show()











