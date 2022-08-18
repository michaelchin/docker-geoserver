#!/bin/bash

mkdir -p zipped_for_geoserver

for i in $(seq 0 395); do 

  gdal_translate -of NetCDF -a_ullr -180 90 180 -90 paleotopo_1.00d_$i.00Ma.nc zipped_for_geoserver/paleotopo_1.00d_$i.00Ma.nc

  cd zipped_for_geoserver

  zip paleotopo_1.00d_$i.00Ma.nc.zip paleotopo_1.00d_$i.00Ma.nc

  rm paleotopo_1.00d_$i.00Ma.nc

  cd ..

done

