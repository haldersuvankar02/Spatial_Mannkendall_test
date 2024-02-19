The Mann-Kendall test is a powerful tool in statistical analysis for detecting trends in time series data. Unlike parametric tests, it does not assume any specific distribution of the data, making it robust and widely applicable across various fields.
In essence, the test evaluates whether there is a consistent monotonic trend, either increasing or decreasing, present in a dataset over time. It assesses the strength and significance of the trend by comparing the ranks of data points within the series. If there is a significant trend, the test provides evidence to support the existence of a systematic change over time.
One of the key advantages of the Mann-Kendall test is its ability to handle data with outliers and non-normal distributions, which are common in many real-world scenarios. It's particularly valuable in environmental studies, hydrology, climatology, and other fields where researchers need to analyze trends in variables like temperature, precipitation, river flow, or air quality.
By providing a rigorous statistical framework for trend detection, the Mann-Kendall test helps researchers make informed decisions and draw reliable conclusions about the direction and magnitude of changes in their data over time.

Data used:
Here we are using ODIAC CO2 monthy data from 2000 to 2019. Data was taken from https://db.cger.nies.go.jp/dataset/ODIAC/DL_odiac2022.html. The Open-Data Inventory for Anthropogenic Carbon dioxide (ODIAC) is a high-spatial resolution global emission data product of
CO2 emissions from fossil fuel combustion (Oda and Maksyutov, 2011).

Reference:
 Mann, H. B., & Kendall, M. G. (1945). "A test for randomness against trend." Econometrica: Journal of the Econometric Society, 245-259.
 Oda, Tomohiro. “ODIAC Fossil Fuel CO2 Emissions Dataset.” GeoTIFF,NetCDF. National Institute for Environmental Studies, 2015. https://doi.org/10.17595/20170411.001.
 Oda, T., and S. Maksyutov. “A Very High-Resolution (1 Km×1 Km) Global Fossil Fuel CO2 Emission Inventory Derived Using a Point Source Database and Satellite Observations of Nighttime Lights.” Atmospheric Chemistry and Physics 11, no. 2 (January 18, 2011): 543–56. https://doi.org/10.5194/acp-11-543-2011.
 Oda, Tomohiro, Shamil Maksyutov, and Robert J. Andres. “The Open-Source Data Inventory for Anthropogenic CO2 version 2016 (ODIAC2016): A Global Monthly Fossil Fuel CO2 Gridded Emissions Data Product for Tracer Transport Simulations and Surface Flux Inversions.” Earth System Science Data 10, no. 1 (January 18, 2018): 87–107. https://doi.org/10.5194/essd-10-87-2018.
