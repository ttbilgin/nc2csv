import argparse
import netCDF4
import xarray as xr
import os


def replace_dots_with_commas(filename):
    with open(filename, 'r', encoding='ANSI') as file:
        text = file.read()
        text = text.replace('.', ',')
    with open(filename, 'w', encoding='ANSI') as file:
        file.write(text)





def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description='netCDF to CSV Converter')

    # Define input file parameter
    parser.add_argument('-i', '--input', help='Input file path', required=True)
    
    # Define switch for comma or semicolon
    parser.add_argument('-tr', '--turkish_num_format', action='store_true', help='Use Turkish format for float/double numbers.')



    # Parse command-line arguments
    args = parser.parse_args()

    # Check if help is requested
    if not (args.input):
        parser.print_help()
        return




    print(f"Input file: {args.input}")

    
    netCDFdata = netCDF4.Dataset(args.input, mode='r')
    dataset = xr.open_dataset(xr.backends.NetCDF4DataStore(netCDFdata))
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
