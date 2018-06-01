#!/bin/bash
#


yum install -y htop &> /dev/null
stats=$?
if [ $stats -eq 0 ];then
	echo "{ \"status\" : \"0\" , \"messages\" : \"Install Nginx Succeed\"}"
else
	echo "{ \"status\" : \"1\" , \"messages\" : \"Install Nginx Error\"}"
fi
