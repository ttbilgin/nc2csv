netCDF to CSV Converter
=======================

This Python script converts netCDF files to CSV format. It utilizes the `netCDF4` and `xarray` libraries for handling netCDF files and data, respectively.
It provides additional functionality to calculate relative humidity and wind speed from the input data.


netCDF is default format when downloading ERA5 data. ERA5 is the fifth generation ECMWF atmospheric reanalysis of the global climate covering the period from January 1940 to present. It is produced by the Copernicus Climate Change Service (C3S) at ECMWF and provides hourly estimates of a large number of atmospheric, land and oceanic climate variables. The data cover the Earth on a 31km grid and resolve the atmosphere using 137 levels from the surface up to a height of 80km. ERA5 includes an ensemble component at half the resolution to provide information on synoptic uncertainty of its products.

## Features

- Convert netCDF files to CSV format
- Calculate relative humidity from temperature and dew point data
- Calculate wind speed from u10 and v10 components
- Option to use Turkish number format for float/double numbers (comma instead of dot)

Usage
-----

    python nc2csv.py -i sample_data.nc [-tr] [-rh] [-ws]

Arguments
---------

*   `-i`, `--input`: Specifies the input netCDF file path. This argument is required. A sample_data.nc file is given in repo files.
*   `-tr`, `--turkish_num_format`: Use this flag to enable Turkish format for float/double numbers. When this flag is provided, the script replaces dots with commas in the output CSV file.
*   `-rh`, `--relative_humidity`: Calculate relative humidity
*   `-ws`, `--wind_speed`: Calculate wind speed

Example
-------

    python nc2csv.py -i sample_data.nc -tr -rh -ws

This command will convert the `input.nc` file to CSV format, calculate relative humidity and wind speed, and save the result as `input_modified.csv`.

## Output

The script will generate a CSV file with the same name as the input file, but with `_modified` appended and the `.csv` extension. The output file will be saved in the same directory as the input file.

## Functions

### `replace_dots_with_commas(filename)`

This function replaces all occurrences of the dot (`.`) character with a comma (`,`) in the specified file. It is used when the `-tr` or `--turkish_num_format` argument is provided to ensure that float/double numbers are represented using the Turkish number format.

### `relative_humidity_calculate(dataset)`

This function calculates the relative humidity from the temperature (`t2m`) and dew point (`d2m`) data in the input dataset. It adds three new variables to the dataset: `TdegC` (temperature in degrees Celsius), `Td_degC` (dew point in degrees Celsius), and `rh` (relative humidity).

### `wind_speed_calculate(dataset)`

This function calculates the wind speed from the `u10` and `v10` components in the input dataset. It adds a new variable `w_s` (wind speed) to the dataset.


Notes
-----

*   The script creates a new CSV file with the same name as the input file but with the "_modified.csv" suffix. You can change the output file naming convention in the script.
*   By default, the script uses a semicolon (`;`) as the separator in the output CSV file. You can modify the `sep` parameter in the script if you prefer a different separator.
*   If you encounter any issues or need additional information, please refer to the turgay.bilgin(at)btu.edu.tr for support.

Requirements
------------

- Python 3.x
- netCDF4
- xarray
- metpy
  
Make sure to have the required libraries installed before running the script:
*   https://docs.xarray.dev/en/stable/
*   https://unidata.github.io/netcdf4-python/

install required libraries:

    pip install netCDF4 xarray

How To cite this repo ?
------------

If you use this tool for preparing thesis, dissertation or paper, you may cite it in following format:

    Bilgin T.T. (2023). netCDF to CSV Converter. https://github.com/ttbilgin/nc2csv/


License
-------

This script is licensed under the MIT License.
