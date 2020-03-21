#!/bin/bash
ip=139.159.138.6
for i in {1..100} 
do
ssh $ip "hostname" >> host.txt
awk '{print '${ip}',$0 }' host.txt >> host2.txt
done &
wait
