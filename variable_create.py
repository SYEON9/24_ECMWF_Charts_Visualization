

from Magics.macro import *
from Magics import macro as magics

import netCDF4 as nc
import numpy.ma as ma   # masked_array->ndarray 변환
import numpy as np      # action create
import json

# ECMWF 시각화 가능한 형태(Action)으로 형 변환 함수
def tomagics(dataset, lats, lons, metadata):
    values = dataset.astype(np.float64)
    lat = lats.astype(np.float64)
    lon = lons.astype(np.float64)

    data = magics.minput(
        input_field = values,
        input_field_initial_latitude = lat[0],
        input_field_latitude_step = lat[1]-lat[0],
        input_field_initial_longitude = lon[0],
        input_field_longitude_step = lon[1]-lon[0],
        input_mars_metadata = metadata,
    )
    return data

"""
    data['levs'][:]
    masked_array(data=[1000.,  975.,  950.,  925.,  900.,  875.,  850.,  800.,
                    750.,  700.,  650.,  600.,  550.,  500.,  450.,  400.,
                    350.,  300.,  250.,  200.,  150.,  100.,   70.,   50.,
                     30.,   20.,   10.,    7.,    5.,    3.,    1.],
"""
def wind_speed(path, file_name, height, levs):
    data = nc.Dataset(path+file_name)

    # total precipitation 생성하기
    if height=='prs':
        u = data['u']
        v = data['v']
        w_speed = (u[:]**2 + v[:]**2)**0.5

    # masked array -> ndarray 변환

    w_speed2 = ma.getdata(w_speed)
    lats = ma.getdata(data['lats'][0,levs,:,:])
    lons = ma.getdata(data['lons'][0,levs,:,:])

    return w_speed2, lats, lons

