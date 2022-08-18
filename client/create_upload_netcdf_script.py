#!/usr/bin/env python
import json
import os

from dotenv import load_dotenv
from geo.Geoserver import Geoserver

workspace_name = "test-paleo_topo"

script_path = os.path.dirname(os.path.realpath(__file__))
load_dotenv(f"{script_path}/.env")  # take environment variables from .env.

# connect to geoserver
geo = Geoserver(
    "https://geosrv.earthbyte.org/geoserver/",
    username=os.environ.get("username"),
    password=os.environ.get("password"),
)

# create workspace
geo.create_workspace(workspace=workspace_name)

# #### build a shell script to do the uploading
# easier to create a .sh file than calling subprocess from python
with open(f"{script_path}/_upload_netcdf.sh", "w+") as f:
    for i in range(0, 10):
        # create coverage store
        cfg = {
            "coverageStore": {
                "name": f"paleotopo_{i}_Ma",
                "type": "NetCDF",
                "enabled": True,
                "_default": False,
                "workspace": {"name": workspace_name},
                "url": "file:placeholder.nc",
            }
        }
        create_cmd_str = (
            "curl -u $username:$password  -XPOST "
            '-H "Content-type: application/json" '
            "-d "
            f"'{json.dumps(cfg)}' "
            f"https://geosrv.earthbyte.org/geoserver/rest/workspaces/{workspace_name}/coveragestores"
        )
        # print(create_cmd_str)

        # update store coverage
        update_cmd_str = (
            "curl -u $username:$password -XPUT "
            '-H "Content-Type: application/zip" '
            '-H "Accept: application/json" '
            f"--data-binary @./zipped_for_geoserver/paleotopo_1.00d_{i}.00Ma.nc.zip "
            f'"https://geosrv.earthbyte.org/geoserver/rest/workspaces/{workspace_name}/coveragestores/paleotopo_{i}_Ma/file.netcdf?coverageName=paleotopo_{i}_Ma"'
        )

        f.write(create_cmd_str + "\n")
        f.write('printf "\\n" \n')
        f.write(update_cmd_str + "\n")
        f.write('printf "\\n" \n')
        f.write("sleep 2\n")


# ret = subprocess.run(["chmod", "+x", "upload_netcdf.sh"], capture_output=True)
# print(ret.stderr)
# print(ret.stdout)
# ret = subprocess.run(["bash", "./upload_netcdf.sh"], capture_output=True)
# print(ret.stderr)
# print(ret.stdout)
