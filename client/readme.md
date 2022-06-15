#### requirements

`conda install -c conda-forge geoserver-rest`

`conda install -c conda-forge python-dotenv`

Use "python38" env on my macbook to run jupyter notebook. 

change admin/gplates password, go to https://geosrv.earthbyte.org/geoserver/web/wicket/bookmarkable/org.geoserver.security.web.UserGroupRoleServicesPage?5&filter=false

`gdal_translate -of NetCDF -a_ullr -180 90 180 -90 paleotopo_1.00d_$i.00Ma.nc zipped_for_geoserver/paleotopo_1.00d_$i.00Ma.nc` need to georeferencing...

You need to install netcdf plugin to use netcdf grids.