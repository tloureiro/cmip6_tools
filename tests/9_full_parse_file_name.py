import glob
import os


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


files = glob.glob('/home/tloureiro/projects/cmip6_downloader/siarean_all_all/' + '*.nc')

for full_file_path in files:

    file_info = get_file_info(full_file_path)
    print(file_info)