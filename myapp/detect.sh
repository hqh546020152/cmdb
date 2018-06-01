#!/bin/bash
#
A="Null"
A=`hostname`
B="Null"
B=`cat /proc/cpuinfo| grep "processor"| wc -l`
C="Null"
C=`free -mh |grep "Mem" |awk '{ print $2 }'`
D="Null"
D=`uname -m`
E="Null"
E=`cat /etc/redhat-release`
F="Null"
F=`uname  -r`
G="Null"
g=`df -h |grep "dev" |grep "vd"| awk '{ print $2 }'|tr '\n' ','`
G=`echo ${g%,*}`
I="Null"
ip add &> /dev/null
[ $? -eq 0 ] && H=`ip addr |grep inet |grep -v inet6 | grep "eth"|awk '{print $2}' |awk -F "/" '{print $1}'`
I=`curl -s ip.sb`
ps -ef &> /dev/null
if [ $? -eq 0 ];then
        t_tag="mysql moogodb postgre elasticsearch redis memcached hadoop nginx tomcat php docker zabbix_server zookeeper grafana fdfs_trackerd fdfs_storaged logstash kafka rocketmq"
        tag=
        for J in $t_tag;do
                K=`ps -ef |grep $J |wc -l`
                [ $K -ge 2 ] && tag="$J,$tag"
        done
        tag=`echo ${tag%,*}`
fi
echo "{ \"tagname\" : \"$A\" , \"cpu\" : \"$B\" , \"memory\" : \"$C\" , \"systemd_version\" : \"$E\" , \"kernel_version\" : \"$F\" , \"space\" : \"$G\" , \"i_ip\" : \"$H\" , \"e_ip\" : \"$I\" , \"tag\" : \"$tag\" }"