from netCDF4 import Dataset
rootgrp = Dataset("siarean_SImon_CESM2_1pctCO2_r1i1p1f1_gn_000101-005012.nc", "r", format="NETCDF4")
# print(rootgrp.variables['time_bnds'][:])

print(list(rootgrp.variables.keys()))

rootgrp.close()