from netCDF4 import Dataset
import netCDF4
from argparse import ArgumentParser
import glob
import os
from datetime import datetime
from datetime import timedelta
import numpy as np
import warnings


def get_file_info(full_file_path):

    file_info = {}

    file_info['file_name'] = os.path.basename(full_file_path)

    file_name_parts = file_info['file_name'].split('_')

    file_info['variable_name'] = file_name_parts[0]
    file_info['realm_time_frequency'] = file_name_parts[1]
    file_info['model_name'] = file_name_parts[2]
    file_info['experiment'] = file_name_parts[3]
    file_info['run_number'] = file_name_parts[4]
    file_info['start_date'] = file_name_parts[6].split('.')[0].split('-')[0]
    file_info['end_date'] = file_name_parts[6].split('.')[0].split('-')[1]

    return file_info


if __name__ == '__main__':

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

    for full_file_path in files:

        file_info = get_file_info(full_file_path)

        output_file = Dataset(output_folder + os.sep + file_info['file_name'], 'w')
        input_file = Dataset(full_file_path)

        starting_year = file_info['start_date'][:4]
        starting_month = file_info['start_date'][4:]

        if file_info['experiment'] == 'historical':
            starting_date = datetime(1, 1, 1)
        else:
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
                    new_date = netCDF4.num2date(value, variable.units, variable.calendar)

                    month_variable[i] = int(new_date.month)
                    year_variable[i] = int(new_date.year)
                    i += 1
            variable_output[:] = variable[:]

        output_file.close()
