#!/bin/bash

basedomain="outpost.com"
hits=0

for i in {a..z}
do
	result=`whois -Q ${i}${basedomain} | grep "No match"`
	if [[ ${#result} -gt 0 ]]
		then
			echo $i$basedomain" is available"
			hits=`expr $hits + 1`
	fi
	sleep 0.5
done

echo $hits" free domains found"