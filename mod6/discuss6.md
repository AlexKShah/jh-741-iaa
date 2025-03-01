# Module 6 - Discussion

Participate in Module 6 by posting an initial response to all four (4) questions. 

Initial responses and at least one (1) substantive thought provoking response to a fellow classmate are due next Wed @ 1159pm EST.

please provide your initial post by Saturday @ 1159pm EST.  this gives enough time for your classmates to respond. 

## Background 1:

California has become the first state to protect mobile application users by enacting a law that is, in some ways, similar to General Data Protection Regulation (GDPR) of the European Union (EU).  The GDPR 2016/679 is a regulation in EU law on data protection and privacy for all individual citizens of the European Union and the European Economic Area (EEA). It also addresses the transfer of personal data outside the EU and EEA areas.  Please read this article: https://www.iubenda.com/blog/the-need-for-privacy-policies-in-mobile-apps-an-overview/ and review this web link as it discusses the EU more in detail  https://www.gdpreu.org/the-regulation/who-must-comply/

### Question 1:  In what ways is this legislation different and in what ways is it similar to GDPR?

### Question 2: Given its differences, do you believe it will have a larger or smaller chance of success in the United States?  Finally, do you think other states will begin to follow suit?
 
## Background 2:

Access the “DoS Attacks on IEEE 802.11 Wireless Networks & Its Proposed Solution” page and read/review Gupta and Garg’s paper.  In this paper they discuss DoS Attacks on management De-authentication, Authentication and Association request frames, and specific prevention methods.

### Question 3: Do you agree with their rationale/reasoning that by maintaining MAC address tables and using traffic filtering you can prevent and/or limit DoS attacks against 802.11 protocols?

### Question 4: What other methods have you seen, used within your organization, or believe have an ability to limit these attacks? (i.e., location-based DoS detection, Content Delivery Networks, Access Controls, Firewalls)


Question 1

GDPR and CCPA are very similar regulations on data collection. Both require companies to make privacy policies, get consent for certain actions, and for the consumer to have certain rights to how their data is used. The CCPA gives consumers in California the rights to disclosure, accessing data, deleting it, opting out of collection, and that the data should not be used in discriminatory ways. The GDPR goes a step further so users could edit their data, restrict or object to how it's processed, and be able to port their data elsewhere. There are more subtle but important differences between the two sets of laws. The GDPR requires a data protection officer be instated to handle data and privacy concerns whereas the CCPA does not. The GDPR protects data collected in the EU from companies in or outside of the EU and for any person in the EU at the time of the collection, even if they are not a resident. The CCPA only protects residents of California from data collection. And there are more criteria in the CCPA for which companies are subject to the laws based on revenue, size, and the number of people whose data the company collects. For GDPR, there aren't any more specific criteria, it applies to any company that collects data of people in the EU. The GDPR also requires opting in before data collection while the CCPA allows data collection to begin when a consumer signs up or makes a purchase. And one of the more important differences is what penalties there are for companies that violate the laws. The CCPA has a range of dollar values from hundreds to thousands per incident depending on the severity and damages. But the GDPR has a much higher cap on fines based on a percent of the companies profit or a fixed cap in the millions of Euros, whichever is larger. So the punishment for violating CCPA is much less severe.

---

Question 2

Compared to GDPR, CCPA has lower penalties, protects only residents of California, and limits which companies are obligated to comply. Businesses lobby against conditions and punishments to their data collection, so a less restrictive law like CCPA would be more likely to be adopted. With these differences, it seems there should be less pushback to implementing similar laws in other states. Since the initial CCPA laws in 2018, several states have put comprehensive data privacy laws in place, and several others have limited data privacy laws or plan to strengthen protections. The differences in each states' laws come down to the companies, the consumers, and the obligations. Such as what types or sizes of companies are required to comply with the laws, the types of consumers and protections they receive, which types of data are covered, and if the protections cover data being disclosed vs sold. For example in Virginia the law covers location data but in Colorado it does not.

---

Question 3

The MAC address method sounds like it has limited functionality, and may not be applicable to all cases. The authors note that an attacker can still find real MAC addresses and spoof them, and it becomes difficult to maintain a MAC table for larger or more dynamic networks. The traffic filtering method appears to be more effective but still has its caveats like an attacker sending management frames from different MAC addresses. In this case the filtering would not prevent DOS attacks. And legitimate traffic might hit the filter and be blocked or throttled which could affect real traffic. 

---

Question 4

One method might not be enough to defeat a DOS attack, but adding a firewall is an easy way to mitigate attacks through predefined rules and prevent them from reaching their destination. MAC addresses can be spoofed or changed, so more reliable authentication methods like certificates can prevent bad actors from using other addresses. In a mixed network like BYOD where multiple devices are expected to be on the network, an IPS system could more thoroughly prevent DOS attacks. There are also modes to 802.11 like protected management frames that try and solve this problem by encrypting and authenticating management frames like deauthentication messages.  

Sources

https://www.okta.com/blog/2021/04/ccpa-vs-gdpr/

https://www.gdpreu.org/ccpa-vs-gdpr/

https://pro.bloomberglaw.com/insights/privacy/state-privacy-legislation-tracker/

https://natlawreview.com/article/state-state-privacy-laws-comparison

https://www.wi-fi.org/beacon/philipp-ebbecke/protected-management-frames-enhance-wi-fi-network-security