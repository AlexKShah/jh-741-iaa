# Module 5 - Discussion

## Question 1:

 "The Devil and Packet Trace Anonymization" (pdf provided in the "Readings" section) provides a detailed process for a.) producing an anonymous traffic trace of raw network data, and b.) anonymizing packets at the link, network, and transport layers (OSI layers 2-4).

 Consider alternative data sources such as HTTP or SMTP – given a particular source of log data, what steps would be involved in anonymizing that trace?  (e.g. approaches to consider- deletion, encryption, generalization, masking the log data, obfuscation, etc.)

## Question 2:

 Discuss what fields in both Netflow and packet headers without payload data sources could be used potentially to break anonymity and their relative strength.

question 1

From the lectures and looking at my browser in Panopticlick, there are several identifying portions of HTTP requests such as those made in a browser that could fingerprint devices. For example, the User agent string, session IDs and similar fields should probably be removed from data for anonymization. But others could be randomized to provide some benefit to studying the traffic like assigning randomized identifiers. From the linked Computerphile video they discussed that producing a hash or set from a limited pool of identifiers could be insufficient to anonymize them. The paper also discusses checksums being used to identify payloads and the need to recalculate checksums after anonymization. Whether HTTP or email over SMTP, certain fields like sender and receiver need to be randomized to provide anonymization. We also saw from the lectures that certain types of protocols might reveal information about the contents of messages by observing information about them, such as encrypted voip messages using different bit lengths for different phonemes. While payloads would probably not be included in an anonymized view of traffic, there are means of measuring lengths, timing, and behavioral patterns that can reveal details about the maker of the traffic and with a enough examples, potentially identify individual users. Techniques like rounding timestamps, and other pseudononymous methods could make these patterns harder to infer, or injecting noise into the data using statistical techniques to make the data more uniform could also help reduce this likelihood. So anonymizing traffic requires careful consideration of the type of traffic, the need for including certain fields, and how removing or obscuring techniques could be used in a way that doesn't allow for identifying patterns. 

question 2

In Netflow and packet headers, information collected about the source, destination and nature of the traffic, even without the payload, can uniquely map traffic and break anonymity. IP addresses and ports can be used to directly identify individuals and are the most important to remove. Session information like being able to follow the protocol, ports, packet size, and number of packets in a sequence of packets can reveal information about the traffic being exchanged. From the lectures we also saw that the timing and duration of exchanges can be used to roughly determine distances and routing information. Looking more broadly at the netflow and packet header data over time can reveal patterns about communication in common between parties, or other behavioral and statistical analyses can be done to isolate groups of packets or users. For example clustering on packet size can reveal encrypted traffic types like video from voip. Some good techniques could be to mask or randomize certain fields, make others more broad like rounding timestamps or padding sizes, and limiting or standardizing ranges of values that could be more unique like packet header information containing information about source parameters or Netflow session details.




low entropy data, want uniform distribution

low latency mixes duration can show distance

voip encodes didfferent sounds at differrent bit lengths

biometrics, surfing habits, typing habist, location

one way functions like hashing and checksums
