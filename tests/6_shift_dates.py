from netCDF4 import Dataset
from datetime import datetime
from datetime import timedelta

# rootgrp = Dataset("siarean_SImon_CESM2_1pctCO2_r1i1p1f1_gn_000101-005012.nc", "r", format="NETCDF4")
rootgrp = Dataset("output.nc")

start_date = datetime(1, 1, 1)

for value in rootgrp.variables['time']:
    new_date = start_date + timedelta(days=float(value))
    print(new_date.month)
    print(new_date.year)

rootgrp.close()