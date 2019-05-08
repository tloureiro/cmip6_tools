from netCDF4 import Dataset
import netCDF4
import warnings


warnings.filterwarnings("ignore")

file_input = Dataset("siarean_SImon_CESM2_1pctCO2_r1i1p1f1_gn_000101-005012.nc")

file_output = Dataset("output.nc", "w")


for dimension_name, size in file_input.dimensions.items():
    file_output.createDimension(dimension_name, len(size) if not size.isunlimited() else None)

for variable_name, variable in file_input.variables.items():

    if variable_name != 'siarean' and variable_name != 'time':
        continue

    print(variable.datatype)
    variable_output = file_output.createVariable(variable_name, variable.datatype, variable.dimensions)

    attributes = {}
    for attribute_name in variable.ncattrs():
        attributes[attribute_name] = variable.getncattr(attribute_name)
    variable_output.setncatts(attributes)

    i = 0
    for value in variable:
        variable_output[i] = value + 2
        i += 1

    # variable_output[:] = variable[:]


file_output.close()
