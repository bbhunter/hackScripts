cat $1 | sed 's/^/{"type":"Host", "fqdn":"/g' | sed 's/$/"},/g' | sed '$s/,$/]/g' | sed '1 s/^/[/g'
#rabbitmqadmin publish exchange=amq.default routing_key=updateDB
