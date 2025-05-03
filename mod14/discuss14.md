Prompt:

As part of the required reading, Idaho National Laboratory, “Cyber Threat and Vulnerability Analysis of the U.S. Electric Sector” Mission Support Center Analysis Report, August 2016, the author discusses two challenges with implementing cybersecurity into ICS/OT Electric utility sectors. 

The two mentioned are 1.) Lack of cyber security personnel and 2.) Lack of cyber hygiene/best practices utilized/implemented.   Read the article, particularly Section 3.6 to 4.0 and answer the following questions;

Question 1. Support your position on whether you agree or disagree with the author that both of the two (2) underlined items above are possible challenges for implementing cyber security OT controls.   Support your answer/reasoning.

Question 2. What other challenges/obstacles are important to consider?  Discuss at least three (3)  (i.e., protocols, platforms, interoperability, regulations, availability concerns, ownership, OS/firmware in-capabilities, etc.).   Support your answer/reasoning.

Question 1

Lack of personnel and cyber hygiene are definitely challenging circumstances for implementing secure OT control. The article talks about studies showing that more than half of the companies surveyed had only one person assigned to ICS/SCADA, and a quarter had no one. This leaves gaps in awareness and diminishes the ability to detect intrusions and unauthorized devices, according to the INL document. And since this is so common, attacks more commonly leverage the lack of awareness to threats. With the lack of personnel, there are fewer people watching out for basics and best practices like passwords, patching vulnerabilities, and physical security. As we have seen from last week's examples, there are often remote access tools and devices with leaked or weak credentials to exploit. And through social engineering, the unpatched vulnerabilities can be exploited once the attacker manages to get a foothold in the network. Even opportunistic hackers with little skill or familiarity can get inside and make changes to an industrial system like we saw with the Oldsmar water treatment case which had poor basic security practices. 

---

Question 2

The unpatched vulnerabilities the authors point out as part of lack of best practices can be seen as a symptom of how ICS systems often involve legacy systems and end up lagging behind in security. It is often more difficult to integrate with old operating systems, software, and controller hardware/firmware while maintaining full coverage. So it's harder to monitor and detect attacks, in addition to the increased attack potential from being outdated such as the example in 3.6.2 where the attack's success was based on old unpatched vulnerabilities from a delay in upgrading. The types of protocols used in ICS are also unencrypted and lack authentication like we discussed about L0 and L1 of the Purdue model. The INL document mentions protocols like Modbus and DNP3 lacking security and authentication measures allowing messages to be intercepted or spoofed. And newer protocols have their drawbacks like IEC 61850 is used over Ethernet which is not isolated or specialized for ICS networks which can make it vulnerable. It's also not feasible to update established protocols to use more secure methods or implement role based access controls that could prevent attacks. The INL document also mentions different organizations and standards groups that are developing regulations that these interconnected but independent grids will be held to, despite having to implement and maintain their own security perimeter and address threats on their own. And with such critical systems subject to different regulatory and organizational levels each trying to address concerns, there could be a lack of accountability that can delay responding to threats, and making decisions to prevent them. 

Sources

Idaho National Laboratory, “Cyber Threat and Vulnerability Analysis of the U.S. Electric Sector” Mission Support Center Analysis Report, August 2016

Purdue Enterprise Architecture.Unified Criteria Facilities (UFC), Cybersecurity of facility-related control systems, UFC 4-010-06, 19 September 16.