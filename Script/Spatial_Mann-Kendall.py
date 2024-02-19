# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:18:03 2023

@author: suvankarh
"""
import rasterio
import numpy as np
from glob import glob
from tqdm import tqdm
import pymannkendall as mk

#Input/Output Folder
inpfol = r"E:\CO2_ODIAC\Seasonal\Monsoon"
outfol = r"E:\CO2_ODIAC\Seasonal\output\Monsoon"
fl = glob(inpfol + '/*.tif') # You can also filter by Season '/*Winter.tif'
fl.sort()

# Read and stack raster data, save metadata
raster_files = (fl)
metadata = None

stacked_data = []
for file in raster_files:
    with rasterio.open(file) as src:
        if metadata is None:
            metadata = src.meta
        stacked_data.append(src.read(1))
stacked_data = np.array(stacked_data)

# Perform Mann-Kendall test for each pixel
height, width = stacked_data.shape[1], stacked_data.shape[2]
result_tau = np.zeros((height, width))
result_slope = np.zeros((height, width))
result_z = np.zeros((height, width))
result_p = np.zeros((height, width))

for i in tqdm(range(height), desc='Processing Rows'):
    for j in range(width):
        pixel_series = stacked_data[:, i, j]
        result = mk.original_test(pixel_series, alpha = 0.05) # Or any other test
        result_tau[i, j] = result.Tau  # For other statistic from the result(type "result.Tau or slope or z or p")
        result_slope[i, j] = result.slope
        result_z[i, j] = result.z
        result_p[i, j] = result.p

# Update metadata
metadata.update({
    'dtype': 'float32',
    'count': 1
})

# Write the result to a new GeoTIFF file
with rasterio.open(outfol + '/Monsoon_mk_results_tau.tif', 'w', **metadata) as dst:
    dst.write(result_tau.astype('float32'), 1)

with rasterio.open(outfol + '/Monsoon_mk_results_slope.tif', 'w', **metadata) as dst:
    dst.write(result_slope.astype('float32'), 1)

with rasterio.open(outfol + '/Monsoon_mk_results_z.tif', 'w', **metadata) as dst:
    dst.write(result_z.astype('float32'), 1)

with rasterio.open(outfol + '/Monsoon_mk_results_p.tif', 'w', **metadata) as dst:
    dst.write(result_p.astype('float32'), 1)
    


