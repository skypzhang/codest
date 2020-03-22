#!/bin/bash
local_time=$(data +"%Y%m%d %H:%M:%S")
local_ip=$(ifconfig ens33 | grep netmask | tr -s " " | cut -d" " -f3)
free_mem=$(cat /proc/meminfo | grep Avai | tr -s " " | cut -d" " -f2)
free_disk=$(df | grep "/$" | tr -s " " | cut -d" " -f4)
cpu_load=$(cat /proc/loadavg | cut -d' ' -f3)
login_user=$(who | wc -l)
procs=$(ps aux | wc -l)
cs=$(vmstat 1 2 | tail -n +4 | tr -s ' ' | cut -d' ' -f13)

