from netCDF4 import Dataset
from argparse import ArgumentParser
import glob
import os
from datetime import datetime
from datetime import timedelta
import numpy as np
import warnings

warnings.filterwarnings("ignore")

parser = ArgumentParser(description='Injects month and year from time')

parser.add_argument("-d", "--directory", dest="directory",
                    help="directory containing nc files", metavar="", required=True)

parser.add_argument("-o", "--output_folder", dest="output_folder",
                    help="output_folder", metavar="", required=True)

directory = vars(parser.parse_args())['directory']
output_folder = vars(parser.parse_args())['output_folder']

if not os.path.isdir(output_folder):
    os.mkdir(output_folder)

files = glob.glob(directory + '*.nc')

for file in files:
    output_file = Dataset(output_folder + os.sep + os.path.basename(file), 'w')
    input_file = Dataset(file)

    start_date_portion = file.split('_')[-1].split('-')[0]

    starting_year = start_date_portion[:4]
    starting_month = start_date_portion[4:]
    starting_date = datetime(int(starting_year), int(starting_month), 1)

    for dimension_name, size in input_file.dimensions.items():
        output_file.createDimension(dimension_name, len(size) if not size.isunlimited() else None)

    for variable_name, variable in input_file.variables.items():

        if variable_name != 'siarean' and variable_name != 'time':
            continue

        variable_output = output_file.createVariable(variable_name, variable.datatype, variable.dimensions)

        attributes = {}
        for attribute_name in variable.ncattrs():
            attributes[attribute_name] = variable.getncattr(attribute_name)
        variable_output.setncatts(attributes)

        if variable_name == 'time':
            month_variable = output_file.createVariable('month', np.int32, variable.dimensions)
            year_variable = output_file.createVariable('year', np.int32, variable.dimensions)
            i = 0
            for value in variable:
                new_date = starting_date + timedelta(days=float(value))
                month_variable[i] = int(new_date.month)
                year_variable[i] = int(new_date.year)
                if(file == '/home/tloureiro/projects/cmip6_downloader/siarean_all_all/siarean_SImon_CESM2-WACCM_historical_r3i1p1f1_gn_185001-201412.nc'):
                    print(len(variable))
                    print(year_variable[i])
                i += 1
        variable_output[:] = variable[:]

    output_file.close()
