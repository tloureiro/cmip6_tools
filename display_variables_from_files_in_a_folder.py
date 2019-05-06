from netCDF4 import Dataset
from argparse import ArgumentParser
import glob
import os

variables_dict = {}

parser = ArgumentParser(description='Display variables contained in all files inside a directory')

parser.add_argument("-d", "--directory", dest="directory",
                    help="directory containing nc files", metavar="", required=True)

directory = vars(parser.parse_args())['directory']

files = glob.glob(directory + '*.nc')

for file in files:
    print(os.path.basename(file))
    rootgrp = Dataset(file, "r", format="NETCDF4")

    variables = list(rootgrp.variables.keys())
    for variable in variables:

        print('\t' + variable)

        if variable in variables_dict:
            variables_dict[variable] += 1
        else:
            variables_dict[variable] = 0


print()
print('Total files: ' + str(len(files)))
print()

print('Found variables:')
for found_variable_name, found_variable_frequency  in variables_dict.items():
    print(found_variable_name + ': found in ' + str(found_variable_frequency) + ' files')

print()