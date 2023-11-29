netCDF to CSV Converter
=======================

This Python script converts netCDF files to CSV format. It utilizes the `netCDF4` and `xarray` libraries for handling netCDF files and data, respectively.

netCDF is default format when downloading ERA5 data. ERA5 is the fifth generation ECMWF atmospheric reanalysis of the global climate covering the period from January 1940 to present. It is produced by the Copernicus Climate Change Service (C3S) at ECMWF and provides hourly estimates of a large number of atmospheric, land and oceanic climate variables. The data cover the Earth on a 31km grid and resolve the atmosphere using 137 levels from the surface up to a height of 80km. ERA5 includes an ensemble component at half the resolution to provide information on synoptic uncertainty of its products.

Usage
-----

    python nc2csv.py -i sample_data.nc [-tr]

Arguments
---------

*   `-i`, `--input`: Specifies the input netCDF file path. This argument is required. A sample_data.nc file is given in repo files.
*   `-tr`, `--turkish_num_format`: Use this flag to enable Turkish format for float/double numbers. When this flag is provided, the script replaces dots with commas in the output CSV file.

Example
-------

    python nc2csv.py -i sample_data.nc -tr

This command converts the `sample_data.nc` file from netCDF to CSV format, using Turkish number formatting. The converted file name is sample_data_modified.csv and saved in the same folder.

Notes
-----

*   The script creates a new CSV file with the same name as the input file but with the "_modified.csv" suffix. You can change the output file naming convention in the script.
*   By default, the script uses a semicolon (`;`) as the separator in the output CSV file. You can modify the `sep` parameter in the script if you prefer a different separator.
*   If you encounter any issues or need additional information, please refer to the turgay.bilgin(at)btu.edu.tr for support.

Requirements
------------

Make sure to have the required libraries installed before running the script:
* https://docs.xarray.dev/en/stable/
* https://unidata.github.io/netcdf4-python/

    pip install netCDF4 xarray

How To cite this repo ?
------------

If you use this tool for preparing thesis, dissertation or paper, you may cite it in following format:

    Bilgin T.T. (2023). netCDF to CSV Converter. https://github.com/ttbilgin/nc2csv/


License
-------

This script is licensed under the MIT License.
