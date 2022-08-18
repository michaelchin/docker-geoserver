#!/bin/bash

export $(cat .env | xargs)
bash ./_upload_netcdf.sh
