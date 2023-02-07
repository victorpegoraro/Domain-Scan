#!/usr/bin/env
import dns.resolver, ipinfo, socket
from ipwhois import IPWhois
from pprint import pprint

def dnsresolve(target_domain):
    # Cconfig records
    record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
    # Create a DNS resolver
    resolver = dns.resolver.Resolver()
    # loop for record types
    for record_type in record_types:
        try:
            answers = resolver.resolve(target_domain, record_type)
        except dns.resolver.NoAnswer:
            continue
        # Print the answers
        print(f"{record_type}:")
        for rdata in answers:
            print(f" {rdata}")

        print( "=-" * 20 )


def get_ipinfo(access_token, ip_address):
    
    # create a client object with the access token
    handler = ipinfo.getHandler(access_token)
    # get the ip info
    details = handler.getDetails(ip_address)
    # print the ip info
    for key, value in details.all.items():
        print(f"{key}: {value}")
        print( "=-" * 20 )

    
def whois(ip):
    # USe whois library
    obj = IPWhois(ip)
    res=obj.lookup_whois()
    pprint(res)


# Start program
if __name__ == "__main__":
    print( "-=" * 6, "DOMAIN SCAN", "-=" * 6 )

    domain = input("[$] Enter domain:")
    
    print("[+] Target : ", domain)
    print( "=-" * 20, "\n" )

    # get the ip address from the command line
    try:
        ip_address = socket.gethostbyname(domain)

        print("[$] DNS Resolve:", "\n")
        dnsresolve(domain)

        print("\n[$] IP infos:\n")
        # Insert your api key
        get_ipinfo('<your-ipinfo-api-key>', ip_address)

        print("\n[$] Whois:\n")
        whois(ip_address)

    except:
        print("Error")

