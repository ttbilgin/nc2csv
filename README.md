netCDF to CSV Converter

netCDF to CSV Converter
=======================

This Python script converts netCDF files to CSV format. It utilizes the `netCDF4` and `xarray` libraries for handling netCDF files and data, respectively.

Usage
-----

    python script_name.py -i input_file.nc [-tr]

Arguments
---------

*   `-i`, `--input`: Specifies the input netCDF file path. This argument is required.
*   `-tr`, `--turkish_num_format`: Use this flag to enable Turkish format for float/double numbers. When this flag is provided, the script replaces dots with commas in the output CSV file.

Example
-------

    python script_name.py -i input_data.nc -tr

This command converts the `input_data.nc` file to CSV format, using Turkish number formatting.

Notes
-----

*   The script creates a new CSV file with the same name as the input file but with the "\_modified.csv" suffix. You can change the output file naming convention in the script.
*   By default, the script uses a semicolon (`;`) as the separator in the output CSV file. You can modify the `sep` parameter in the script if you prefer a different separator.
*   If you encounter any issues or need additional information, please refer to the [GitHub repository](link_to_your_repo) for support.

Requirements
------------

Make sure to have the required libraries installed before running the script:

    pip install netCDF4 xarray

License
-------

This script is licensed under the [MIT License](link_to_license_file).
