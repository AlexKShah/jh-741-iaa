Module 3 - Assignment

    Due Wednesday by 11:59pm Points 100 Submitting a text entry box or a file upload

In this assignment you will look up information on a set of 11 addresses, including domain name, ownership, CIDR block and routing. The assignment for module 3 is attached as a PDF. Download the assignment and answer each question. Submit the assignment in either Word or PDF format.

Due Wed @ 1159pm EST
Attachments

Assignment 3-4.pdf

CIDR definition:   Classless Inter-Domain Routing (CIDR) is an IP address allocation method that improves data routing efficiency on the internet. Every machine, server, and end-user device that connects to the internet has a unique number, called an IP address, associated with it. Devices find and communicate with one another by using these IP addresses. Organizations use CIDR to allocate IP addresses flexibly and efficiently in their networks. 

 

Classless Inter-Domain Routing (CIDR) allows network routers to route data packets to the respective device based on the indicated subnet. Instead of classifying the IP address based on classes, routers retrieve the network and host address as specified by the CIDR suffix.

 

Benefits of CIDR:

With Classless Inter-Domain Routing (CIDR), your organization has more flexibility in assigning IP addresses and routing data between devices.
Reduce IP address wastage

CIDR provides flexibility when you determine the network and host identifier assignments on an IP address. You can use CIDR to provision the required number of IP addresses for a particular network and reduce wastage. Besides, CIDR reduces routing table entries and simplifies data packet routing. 
Transmit data quickly

CIDR allows routers to organize IP addresses into multiple subnets more efficiently. A subnet is a smaller network that exists within a network. For example, all devices connected to a router are on the same subnet and have the same IP address prefix.

With CIDR, your organization can create and consolidate multiple subnets. This allows data to reach the destination address without taking unnecessary paths. 
Create a Virtual Private Cloud

A virtual private cloud (VPC) is a private digital space hosted within the cloud. It allows your organization to provision workloads in an isolated and secure environment. A VPC uses CIDR IP addresses when it transfers data packets between connected devices. 
Create supernets flexibly

A supernet is a group of subnets with similar network prefixes. CIDR allows flexibility in creating supernets, which isn’t possible in conventional masking architecture. For example, your organization can combine IP addresses into a single network block using a notation like this:

    192.168.1 /23 
    192.168.0 /23

This notation applies a subnet mask of 255.255.254.0 to the IP address, which returns the first 23 bits as the network address. The router needs only one routing table entry to manage data packets between devices on the subnets.

 

reference link:    https://aws.amazon.com/what-is/cidr/

Links to an external site.  

 

best, jason

-----

Assignment 3
Answers to the following questions for each Address below. Answers should be
submitted via Blackboard. Submission must be in either Word or PDF format.
1. www.wikipedia.org
2. www.cnn.com
3. www.foxnews.com
4. www.aleae.com
5. www.amazon.com
6. www.google.com
7. 23.55.27.118
8. 104.112.42.112
9. 216.58.219.196
10. 23.46.57.18
11. 128.244.42.5
1. Provide the domain name, top-level domain, subdomain, and the root domain of this
address? (applies to numbers 1 through 6 above).
2. To what CIDR-block does the address’s resolved IP address belong and who owns the
CIDR-block? (applies to all 1 through 11 above)
3. What is the country of origin for the address? (applies to all 1 through 11 above)
4. To what Autonomous System does it belong? (applies to all 1 through 11 above)
5. Run Traceroute and list the path and (latency per hop) from your system to the
address? Note: if home router prevents traceroute to run successful against 1 through
11 above, can use on-line traceroute utilities that start from a different router to answer
this question. (applies to all 1 through 11 above)
6. For IP addresses only, what DNS FQDNs are associated with the IP address?
(Can use reverse DNS lookup/resolution) (only applies to 7 through 11 above)
7. Why might Boarder Gateway Protocol (BGP) sometimes be preferred over Open
Shortest Path First (OSPF)? Support your answer.
8. Discuss eight (8) differences between BGP and OSPF. (i..e, Implementation,
Convergence, Design, Size of the network, Function, Algorithm, Protocol, Type, etc.)
9. Explain what CIDR Classful and Classless addresses are & when you would use both?
Note: amazon link below will help
Note: some helpful websites to aid in completing this assignment:
https://www.ultratools.com/tools/asnInfoResult?domainName=AS14907 
https://www.ipaddressguide.com/cidr
ASN WHOIS lookup; https://dnschecker.org/asn-whois-lookup.php
https://aws.amazon.com/what-is/cidr/