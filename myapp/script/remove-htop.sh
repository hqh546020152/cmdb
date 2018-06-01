#!/bin/bash
#


yum remove -y htop &> /dev/null
stats=$?
if [ $stats -eq 0 ];then
	echo "{ \"status\" : \"0\" , \"messages\" : \"Remove Nginx Succeed\"}"
else
	echo "{ \"status\" : \"1\" , \"messages\" : \"Remove Nginx Error\"}"
fi
