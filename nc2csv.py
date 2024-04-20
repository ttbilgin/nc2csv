import argparse
import netCDF4
import xarray as xr
import os
import metpy.calc as mpcalc
from metpy.calc import (mixing_ratio_from_relative_humidity, relative_humidity_from_dewpoint,
                        thickness_hydrostatic)
from metpy.cbook import get_test_data
from metpy.units import units


def replace_dots_with_commas(filename):
    with open(filename, 'r', encoding='ANSI') as file:
        text = file.read()
        text = text.replace('.', ',')
    with open(filename, 'w', encoding='ANSI') as file:
        file.write(text)

def relative_humidity_calculate(dataset):
    # relative humidity calculate
    T = dataset.t2m * units.kelvin
    Td = dataset.d2m * units.kelvin
    rh = relative_humidity_from_dewpoint(T, Td)
    dataset['TdegC']= T.metpy.convert_units('degC')
    dataset['Td_degC']=Td.metpy.convert_units('degC')
    dataset['rh']=rh
    return dataset

	
def wind_speed_calculate(dataset):
    # wind speed calculate
    dataset['w_s'] = mpcalc.wind_speed(dataset.u10, dataset.v10)
    return dataset



def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description='netCDF to CSV Converter')

    # Define input file parameter
    parser.add_argument('-i', '--input', help='Input file path', required=True)
    
    # Define switch for comma or semicolon
    parser.add_argument('-tr', '--turkish_num_format', action='store_true', help='Use Turkish format for float/double numbers.')

	# Define switch for relative humidity
    parser.add_argument('-rh', '--relative_humidity', action='store_true', help='calculate relative humidity.')

	# Define switch for wind speed
    parser.add_argument('-ws', '--wind_speed', action='store_true', help='calculate wind speed.')

    # Parse command-line arguments
    args = parser.parse_args()

    # Check if help is requested
    if not (args.input):
        parser.print_help()
        return




    print(f"Input file: {args.input}")

    
    netCDFdata = netCDF4.Dataset(args.input, mode='r')
    dataset = xr.open_dataset(xr.backends.NetCDF4DataStore(netCDFdata))
	
    if args.relative_humidity:
        dataset=relative_humidity_calculate(dataset)

    if args.wind_speed:
        dataset=wind_speed_calculate(dataset)
		
    #csv ye  aktarmak için
    df= dataset.to_dataframe()
    # Change the extension of the input file
    input_filename, input_extension = os.path.splitext(args.input)
    new_input_file = input_filename + "_modified" + ".csv"  # Change ".txt" to your desired new extension

    df.to_csv(new_input_file,sep=';')
    if args.turkish_num_format:
        replace_dots_with_commas(new_input_file)
		

		

if __name__ == '__main__':
    main()
