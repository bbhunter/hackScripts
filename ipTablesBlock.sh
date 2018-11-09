#!/bin/bash

function block {
	echo "[+] Blocking Access"
	iptables -A INPUT -p tcp -m tcp -m multiport ! --dports 22 -j DROP

}

function unblock {
	echo "[+] Unblocking Access"
	iptables -D INPUT -p tcp -m tcp -m multiport ! --dports 22 -j DROP

}

if [ "$1" == 'block' ] 
then
	block
fi

if [ "$1" == 'unblock' ]
then	
	unblock
fi

if [ "$1" == '' ]
then 
	echo "[+] Blocking Access"
	block
	echo "[+] Sleeping for 1 minute"
	sleep 1m
	echo "[+] Unblocking Access"
	unblock
fi

	

