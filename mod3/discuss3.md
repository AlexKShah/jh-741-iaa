The Border Gateway Protocol (BGP) is the default routing protocol to route traffic among Internet domains. While BGP performs adequately in identifying viable paths that reflect local routing policies and preferences to destinations, the lack of built-in security allows the protocol to be exploited by route hijacking. Route hijacking occurs when an entity accidentally or maliciously alters an intended route. Such attacks can (1) deny access to Internet services, (2) detour Internet traffic to permit eavesdropping and to facilitate on-path attacks on endpoints (sites), (3) miss-deliver Internet network traffic to malicious endpoints, (4) undermine Internet Protocol (IP)-address-based reputation and filtering systems, and (5) cause routing instability in the Internet.

One method to resolve this problem is to incorporate route origin validation (ROV) by using the Resource Public Key Infrastructure (RPKI) in a manner that mitigates some misconfiguration and malicious attacks associated with route hijacking.   

Request for Comment (RFC) 6810 found here: https://tools.ietf.org/html/rfc6810 discusses the use of public-private cryptographic key pairs to validate whether or not networks are allowed to make their BGP route announcements.   Additionally, NIST Cybersecurity Special Publication 1800-14B: Protecting the Integrity of Internet Routing by using BGP Route Origin Validation (ROV) methods with Resource Public Key Infrastructure (RPKI) to address and resolve erroneous network routes from being exchanged.   NIST Discussion can be accessed here: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1800-14.pdf

After looking through both RFC 6810 and NIST SP answer the below questions.   Your initial post must answer all three (3) questions.

While the need for securing BGP is well understood, the willingness and adoption of security measures has been slow to be implemented, with only 37 autonomous systems using route validation.  



---

Question 1:

In your opinion why do you think securing BGP configurations is slow to be adopted?  (e.g. resources, architectures, costs, configuration)

BGP involves peer agreements and many considerations when setting up routes that are often based on business as well as technical reasons that make securing BGP a convoluted and hard to regulate "kludge". Even if there were a good way to transition to a more secure method of authenticating and routing that everyone could agree to adopt (unlikely anytime soon), there is a lot of resistance to upsetting the existing configurations and methods of setting them up by tier 1's. ISPs are probably reluctant to having to incur any costs from implementing any changes, which could also introduce limitations or cause downtime. And since routing between ASes is between black boxes, there might be compatibility problems with the non standardized ways that each ISP has set up their systems over the decades that they are unlikely to change without good reason. There are problems in the proposed solutions such as in RFC6810 which mentions entirely new problems in familliar ways like someone downstream could set up their infrastructure to check for keys on the hour and cause a large surge in requests that upstream key stores would have to handle. It would also introduce entirely new hardware/software to be maintained with their own security and misconfiguration vulnerabilities.

---

Question 2:

Is it easier to use ROV with RPKI with some network environments (i.e. legacy/enterprise IT, OT/ICS, IoT's, wireless, cloud, homogeneous, heterogeneous, and autonomous) over others?

I would imagine that there are differences between these network environments where smaller providers and more homogenous networks, could deploy ROV with RPKI more easily. So for example a small ISP or cloud provider would be able to introduce these security concepts into their existing infrastructure but a legacy enterprise with a complex heteregenous system with many edges would be more cumbersome. In systems that were set up to be more autonomous, making changes would be especially frustrating. And organizations that have leaned on upstream ISPs to handle problems would be less likely and less able to adapt their infrastructure. 

---

Question 3:

What are some attacks used against BGP and how can they be detected as well as defended (e.g. Pretty Good BGP, Listen & Whisper, Detect False Route Announcements, ROV with RPKI) ? 

Problems with advertisement/announcement need to be handled with careful observation to catch changes that might effect routing and availability. Like with the 2008 Pakistan/Youtube situation, even purposeful changes to routing can be misconfigured and propagate up to unsuspecting groups. A lack of vigilance and communication allowed these changes to cause a major outage. A couple proposed solutions to malevolent route hijacking/spoofing are to use ROV with RPKI or Pretty Good BGP to validate the authenticity of route announcements but like we saw in 2008, legitimate configuration changes can have unintended consequences. Listen in Listen & Whisper can help detect changes to route advertisements between peers to more quickly detect when a configuration changes and how it impacts routes and availability to see if changes both legitimate and malicious have side effects. Whisper then works similarly to other proposed authentication methods to cryptographically check for fake advertisements. So the Listen portion of listen and whisper to verify how configuration changes impact availability, and some form of authentication to prevent spoofing could prevent a large amount of common BGP attacks and problems.

Sources:

[1] Mod 3 lectures
[2] https://tools.ietf.org/html/rfc6810  
[3] https://www.usenix.org/legacy/publications/library/proceedings/nsdi04/tech/subramanianListen/subramanianListen_html/paper.html