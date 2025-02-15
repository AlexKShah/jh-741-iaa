The NIST CyberSecurity White Paper on Internet of Things (IoT) Trust Concerns enumerates on 17 technical trust areas for any IoT system, based on the authors discussion presented in the NIST SP 800-183, Network of Things.

https://csrc.nist.gov/files/pubs/other/2018/10/17/iot-trust-concerns/ipd/docs/iot-trust-concerns-draft.pdf

Question:

Choose 4 of them and provide in a discussion the following: (Answer Both questions on your initial response)

    1. your viewpoints on whether you agree or disagree with the author’s defined trust issues
    
    2. how they differ for IoT as compared to traditional legacy and/or enterprise IT systems.

Provide your reasoning for your opinion. Please cite your sources.

Initial responses and at least one (1) substantive response to a fellow classmate are due next Thurs @ 1159pm EST.

please provide your initial post by Saturday @ 1159pm EST.  this gives enough time for your classmates to respond. 

I agree with the NIST paper that Scalability, Security, Ownership/Control, and Reliability are important factors in trusting IoT devices. These factors have huge concerns for the use and adoption of smart devices and could present long term issues as more and more devices come online. 

Scalability and Security are big factors in IoT devices that go hand in hand, as each device adds attack surface. Though these lectures and concerns are from ~2018 there hasn't been all that much to regulate or fix the lack of testing and security. I still hear about hacked models of cameras and DDoS being run on unsuspecting user's washing machines as part of a botnet. Many people run out and buy a product based on price and features, and don't often consider security as part of a buying decision. So like the NIST paper is saying, there is an explosion in the number of devices associated with each person, which is an increase in the number of devices that have security concerns, energy demands and consume bandwidth and resources. Compared to traditional/legacy systems, we are bringing many more IoT devices online than we are taking offline or replacing. When you replace your cell phone you likely don't keep the second one active, comparatively many people just keep adding new smart devices to their home. And they often configure it once and never go back to change the settings or think about updating it. Traditional systems are more centralized for update and control whereas smart devices are more distributed and need to be kept up to date per device.

Another trust factor is Ownership and Control, where IoT devices are often limited to working with certain software or are mostly closed off, making them hard to integrate with or trust their internal operation. Device providers can stop providing support at any time including security updates. So users might get stuck with an integral part of their smart device chain that isn't evaluated for security or might lose functionality. With a limited ability to black box test these devices, there could be unforeseen problems or vulnerabilities. The NIST paper suggests a chain of custody scenario that cascading events could lead to failure or injury, but this also lends to a wider problem. What happens when lots of black box products are left insecure or broken on the network? Or what happens to a workflow when a device is forced offline? In a more and more common user experience scenario, a Spotify car product was discontinued a year after its release and left owners with a brick. The device interacted with Spotify over an internet connection and once Spotify decided to stop support, owners didn't have any ability to make the device work with other services or to use the hardware for other purposes. Spotify's suggestion was to throw it away responsibly. [1] This highlights how fragile the product space is and sets a bad expectation for how companies are planning the life cycle of these products.

With such limited ability to inspect how the device works and to use its rigidly defined input/output parameters, this also leads to Reliability concerns. There might be compatibility issues in the evolving smart device landscape and it seems like there are few guarantees when working with these devices. The NIST paper lays out how sensors can create bad data that could create problems when processed by other devices or when used to make decisions. Or when devices are fed corrupt data you can only turn to black box testing to find out how it will react, or when it inevitably happens in the field you'll find out whether it's garbage in garbage out or if it crashes.

These factors and compatibility issues make the reliability of IoT devices more concerning than traditional computing which at least have some limited guarantees for compatibility or more stable standards and certifications. Especially since in IoT "the instantaneously changing nature of IoT systems will induce emergent and complex chains of custody and make it difficult to ensure and correctly measure reliability." as per the NIST paper. [2] Which is made further concerning by the growing scale. So I think these trust issues will persist, as there isn't likely to be a fast solution toward standardizing this growing area of devices.

[1] https://support.spotify.com/us/article/car-thing-discontinued/
[2] https://csrc.nist.gov/files/pubs/other/2018/10/17/iot-trust-concerns/ipd/docs/iot-trust-concerns-draft.pdf