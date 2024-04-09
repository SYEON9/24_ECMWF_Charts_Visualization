


"""
!pip install Magics
!pip install MagPlus
!pip install ecmwflibs
!pip install netCDF4
!pip install ecmwf-data ecmwf-opendata magpye
"""

#import nbformat as nbf
from Magics import macro as magics
from magpye import GeoMap
from Magics.macro import *

from variable_create import *

#=================================================#
#  Program: ECMWF Charts visualization tutorial
#  Purpose: [차수예]"자율형 공동활용체계 구축을 위한 범용 수치예보모델 개발" 사업 중
#           가시화 도구 시험
#  Reference: ECMWF (https://charts.ecmwf.int/?facets=%7B%22Product%20type%22%3A%5B%5D%2C%22Range%22%3A%5B%22Medium%20%2815%20days%29%22%5D%2C%22Parameters%22%3A%5B%5D%2C%22Type%22%3A%5B%22Forecasts%22%5D%7D)
#             Magics (https://github.com/ecmwf/notebook-examples/tree/master/visualisation)
#  Author: Su-Yeon Kim
#  Date: 2024.04.09
#-------------------------------------------------#


####################################################################
# STEP 01. 변수 로드
# Mean sea level pressure와 wind speed 를 예시로 사용함.
#
####################################################################
# data path
path = 'C:/Users/KIMSUYEON/Desktop/syeon_file/2024/202402_next_generation_numerical_example/KIM_data/post/'
file_name = 'prs.ft006.nc'

# geopotential height
psl = magics.mnetcdf(
    netcdf_filename = path + file_name,     # file name
    netcdf_value_variable = 'psl',          # variable name
)

wind_vector = magics.mnetcdf(
    netcdf_filename = path + file_name,     # file name
    netcdf_level_dimension_setting = 850,   # air pressure
    netcdf_x_component_variable = 'u',      # vector compoonent
    netcdf_y_component_variable = 'v',
)

# -----------------------------------------------------------------
# STEP 01.1 변수 생성 및 변경
# wind speed variable create
# -----------------------------------------------------------------

metadata = "{'long_name': 'wind_speed', 'units':'m/s'}"
wind_speed, lats, lons = wind_speed(path, file_name, 6)
wind_speed2 = tomagics(wind_speed, lats, lons, metadata)    # magics에서 사용하는 action 형태로 변환

####################################################################
# STOP 02. visualization
####################################################################
contour = magics.mcont(
    contour_automatic_setting = 'ecmwf',
    legend='on',
)

contour_wind = magics.mcont(
    contour = 'off',
    contour_shade = 'on',
    contour_automatic_setting =  "style_name",
    contour_style_name = "sh_grn_f10t100lst"
)

legend = magics.mlegend(
    legend_display_type = "continuous",
    legend_text_font_size=0.75,
    legend_text_colour ='navy'
)

magics.plot(psl, contour, wind_speed2, contour_wind, wind_vector, magics.wind(), legend, magics.mcoast())