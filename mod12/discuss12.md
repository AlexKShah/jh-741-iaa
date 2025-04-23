Question 1

Defensive products like firewalls, and IDS/IPS systems can detect elements of TCP/IP attacks like SYN flooding and IP spoofing as mentioned in the Attack & Defense paper. As part of a broader security implementation they can help in preventing some of these types of attacks. A firewall could inspect and identify network traffic and deny suspicious packets based on sets of rules. While an attacker can get around basic rule sets, enterprise firewall applications can look at repeated attempts to open connections like in SYN flooding and deny or limit the number of connections made to a server from that address. Though an attacker with significant resources can still overwhelm the firewall's protections. An IDS/IPS system such as a network based system inspecting requests and patterns made to servers, or host based on the server itself, can detect anomalies and irregularities that might reveal an attack. For example SYN flooding traffic compared to a baseline would stand out and the source IP addresses could be blocked or rate limited. And in IP spoofing, aspects like routing and timing information can inform the tool whether the IP address is suspicious.

---

Question 2

Vulnerability scanners like Nessus and network sniffing utilities like Wireshark can be used effectively to find weak spots in a network's security before attackers are able to take advantage of it. The server can be inspected by Nessus or Nmap to find open ports and vulnerabilities that the security team could attempt to close off to attackers. These tools could also be used to find the thresholds needed to break functionality by simulating attacks. For example security staff can flood a server with SYN packets to determine how well a firewall, IDS, or server configuration is handling the elevated number of connections by examining traffic on Wireshark and monitoring services. 

---

Question 3

Smurf attacks are more worrisome than Ping of Death since Ping of death relies on an oversizes ping packet that some systems might not be able to handle. With the prevalence of the attack type, I would hope that patches to discard oversized ICMP packets would be implemented in network hardware like routers or at least in rules in a firewall though this may be impossible if the packet is unable to be parsed. Smurf attacks on the other hand rely on exploiting existing mechanisms in ping to spoof the target's address as the one making the ping to the broadcast address of the subnet which makes other devices on the subnet respond to the target as if it made many requests, which can overwhelm the target. Since the smurf attack relies more on legitimate addressing and tactics that are harder to detect, compared to a ping of death where the payload size could be a simple check, the smurf attack seems to me to be more damaging and harder to prevent.

Sources:
Saini, J. R. (2014). (PDF) attacks & defense mechanisms for TCP/ IP based protocols. Retrieved from https://www.researchgate.net/publication/260877113_Attacks_Defense_Mechanisms_for_TCP_IP_Based_Protocols 

https://www.fortinet.com/resources/cyberglossary/smurf-attack

https://www.fortinet.com/resources/cyberglossary/ping-of-death