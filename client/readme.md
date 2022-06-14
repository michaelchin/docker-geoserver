#### requirements

`conda install -c conda-forge geoserver-rest`
`conda install -c conda-forge python-dotenv`


change admin/gplates password, go to https://geosrv.earthbyte.org/geoserver/web/wicket/bookmarkable/org.geoserver.security.web.UserGroupRoleServicesPage?5&filter=false

`gdal_translate -of NetCDF paleotopo_1.00d_40.00Ma.nc test.nc` run this on a linux. not working on my macbook for some reason

You need to install netcdf plugin to use netcdf grids.