Industrial Control Systems (ICS) are sometimes referred to as Cyber Physical Systems (CPS) or Operational Networks (OT).  When ICS/OT was first designed, developed and implemented they were air-gapped and/or isolated from other networks and conventional enterprise systems.  However, as new customer demands/capabilities emerge; Ethernet, remote access, and Industrial Internet of Things (IIoT's) are being used extensively in industrial automation applications, and in office environments of industrial firms, as well as, in building automation/emergency systems requiring the convergence of IT and OT networks.  

Question 1: Explain four (4) main operational differences between ICS/OT and IT networks, and how all four (4) create possible new attack vectors?

Question 2: Review the attached Unified Facility Criteria (UFC) for IT.OT networks ppt & Section 2.2 through Section 2.3 of the Purdue Enterprise Architecture.UFC 4-010-06 (part of the readings for this module), then provide your reasoning for why applying cybersecurity controls to the converged IT-OT Tier structure might create challenges?   

Hint: (think of Traditional IT and Non-Traditional IT interfaces, protocols, etc.).    Support your reasoning and cite all sources.

Question 1

ICS/OT and IT networks have different priorities for securing operations. For example, in the SANS survey, respondents said their primary business concern for ICS/OT was availability. This is also backed up by the UFC guidelines Chapter 3 3-2. In comparison, the traditional IT CIA triad prioritizes data confidentiality before availability. This difference in priorities can determine how risks are treated, for example ICS systems might not use encryption or strong authentication at the lower levels (L0, L1). These levels might have "dumb" sensors that are incapable of encryption or non networked devices might not have encryption because it's not a priority and probably don't get upgraded to maintain availability. In an IT environment most if not all devices would be networked and would require encryption and authentication considerations to preserve confidentiality. The difference in risk and potential attack vectors lead to different design decisions and maintenance paths. These devices would also be kept up to date and downtime for upgrades would be reasonable to IT. In comparison those unencrypted devices in an ICS network might never get upgraded unless it was part of some other rollout. There has also been a shift away from strictly airgapped, non networked portions of ICS environments to make it more convenient to access remotely or deploy like Industrial IoT devices. Making ICS more like IT has introduced additional attack vectors like stealing credentials leading to direct access or more capabilities in pivoting once some of the infrastructure has been reached.

---

Question 2

The mix of priorities, capabilities, and expectations from the different layers in a mixed IT/OT system can be challenging to secure. For example, the lower level L0/L1 devices in the UFC document Figure 2-1 shows analog and binary outputs from sensors, controllers, and non networked hardware. These components can be difficult to monitor using traditional IT integrations. For example, intrusion systems or setting up logging and monitoring to continuously verify the security of the operation. In the SANS document, surveyed ICS installations conducted security audits a handful of times per year, if that. So there is a clear difference where IT components are expected to generate alerts immediately compared to OT components being evaluated on a semi regular basis. And compared to monitoring the spin of a turbine with an analog sensor or the chosen setting of a dial, security in traditional IT layers revolve around access control mechanisms and event monitoring. These types of design decisions are not easily compatible with an established industrial setting without integrating parts and tools carefully. And to make things more difficult, whether designing a new system or integrating with an existing system, it will be a significant challenge to achieve the high availability goals of the OT side with the access and continuously monitored side of the IT systems.

Sources

DesRuisseaux, Daniel. (2018). Practical Overview of Implementing IEC 62443 Security Levels in Industrial Control Applications.

Gregory-Brown, Bengt. (2017). SANS Institute Information Security Reading Room Securing Industrial Control Systems-2017.

US Department of Defense. (2016). CYBERSECURITY OF FACILITY-RELATED CONTROL SYSTEMS. UFC 4-010-06.