import dns.resolver
from dns import reversename
import netaddr
import argparse
import multiprocessing
parser = argparse.ArgumentParser()
parser.add_argument("ipRange", help="IP range to scan for PTR records")
parser.add_argument("dnsServer", help="DNS Server to use for this scan. Comma delimited for more than one.")
parser.add_argument("--threads", type=int, default=10, help="Number of threads to use")
args = parser.parse_args()

net = netaddr.IPNetwork(args.ipRange)
myResolver = dns.resolver.Resolver()
myResolver.nameservers = args.dnsServer.split(",")
myResolver.timeout=.25
myResolver.lifetime=.25

def resolve(ip):
    addr=reversename.from_address(str(ip))
    try:
        print myResolver.query(addr, "PTR")[0]
    except dns.exception.Timeout:
        print "nope"

p = multiprocessing.Pool(args.threads)
p.map(resolve, net)
