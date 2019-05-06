from netCDF4 import Dataset
import netCDF4
import warnings


warnings.filterwarnings("ignore")

rootgrp = Dataset("crop.nc", "r", format="NETCDF4")

# del(rootgrp.variables['time_bnds'])

print(list(rootgrp.variables.keys()))

rootgrp.close()


# input file
dsin = Dataset("siarean_SImon_CESM2_1pctCO2_r1i1p1f1_gn_000101-005012.nc")

# output file
dsout = Dataset("crop.nc", "w", format="NETCDF4")

# Copy dimensions
for dname, the_dim in dsin.dimensions.items():
    print
    dname, len(the_dim)
    dsout.createDimension(dname, len(the_dim) if not the_dim.isunlimited() else None)

# Copy variables
for v_name, varin in dsin.variables.items():
    outVar = dsout.createVariable(v_name, varin.datatype, varin.dimensions)
    print
    varin.datatype

    # Copy variable attributes
    outVar.setncatts({k: varin.getncattr(k) for k in varin.ncattrs()})

    outVar[:] = varin[:]
# close the output file
dsout.close()
