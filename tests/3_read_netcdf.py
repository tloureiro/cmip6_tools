from netCDF4 import Dataset
# rootgrp = Dataset("siarean_SImon_CESM2_1pctCO2_r1i1p1f1_gn_000101-005012.nc", "r", format="NETCDF4")
rootgrp = Dataset("/home/tloureiro/projects/cmip6_tools/transformed/siarean_SImon_CESM2-WACCM_historical_r3i1p1f1_gn_185001-201412.nc")
print(rootgrp.variables['year'][:])

for value in rootgrp.variables['time']:
    print("%.2f" % value)

print(list(rootgrp.variables.keys()))

print(rootgrp.variables['time'][156] - rootgrp.variables['time'][155])

rootgrp.close()