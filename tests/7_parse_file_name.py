import glob

files = glob.glob('/home/tloureiro/projects/cmip6_downloader/siarean_all_all/' + '*.nc')

for filename in files:
    start_date_portion = filename.split('_')[-1].split('-')[0]

    starting_year = start_date_portion[:4]
    starting_month = start_date_portion[4:]
    print(starting_year + '_' + starting_month)



    '/home/tloureiro/projects/cmip6_tools/transformed/siarean_SImon_CESM2-WACCM_historical_r3i1p1f1_gn_185001-201412.nc'