# Module 5 - Overview and Objectives
Summary

In this module, we discuss techniques for anonymizing and deanonymizing network traffic data. Anonymization is the process of removing information that can be used to identify a user, and may be done as a post-processing effort, or by using systems that hide the user’s identity during normal operations. Anonymity has been a major concern in network security for the past thirty years, with especially active interest in the last decade with the rise and fall of napster and other peer-to-peer applications.
Objectives

By the end of this module, students will be able to:

    Describe the techniques used to quantify anonymization: the anonymity set and k-anonymity.
    Describe mechanisms which are used to provide user anonymity – onion routing and DHTs.
    Describe the difficulty in anonymizing data.
    Identify techniques and information that can be used to deanonymize data.
    Understand anonymization drivers and benefits,
    Describe anonymization techniques and methods
    Explain limitations and challenges to anonymization & legal considerations
    Future of anonymization and putting anonymization into practice

 

Begin this module by viewing the lectures in the recommended order. After viewing the lectures, complete the assigned reading. Viewing the lectures and completing the readings will prepare you to participate in the Module 5 Discussion. The lectures will also prepare you to complete the assignment. Feel free to post any questions you may have about the material to the Q&A area of the Discussion Board.

---

# Module 5 - Readings

All pdf's attached below  (except NIST SP 800-207)

    Pang et al, “The Devil and Packet Trace Anonymization”  (will help with Discussion questions this week)- pdf attached
    Dingledine et al, “Tor: The Second Generation Onion Router”
    Wright et al, “Uncovering Spoken Phrases in Encrypted Voice over IP Communications”
    Narayan and Shmatikov, “Robust De-Anonymization of Large Sparse Datasets”
    Coull et al, “The Challenges of Effectively Anonymizing Network Data”
    Eckersley, “How Unique is Your Web Browser?”
    McCoy D., Bauer, K. et. Al., "Shining Light in Dark Places Understanding the Tor Network"
    Kang, R. et. Al., "Why Do People Seek Anonymity on the Internet? Informing Policy and Design"
    NSA Zero Trust Architecture Security Model, pdf (can be used for assignment, as well as, the NIST SP 800-207)
    DoD Zero Trust Plan. Seven Pillars to ZT, pdf
    NIST SP 800-207 Zero Trust Architecture; link to access; https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf 

Links to an external site.   (might need to copy and paste into browser)
Rennhard, et. al. "An Architecture for an Anonymity Network"  pdf attached
Farah, T. "Algorithms and Tools for Anonymization of the internet traffic"  pdf attached
Kanaskar, R. (2018), "The Impact of Net Neutrality and Additional Regulations on the Future of the Internet of Things in the United States."
Narayanan, A., et. al. (n.d.), "Robust De-anonymization of Large Sparse Datasets"  (will help with Discussion questions this week)- pdf attached 
New Article about Anonymity for cyber:  Catch Me If You Can. Cyber Anonymity.pdf
A Best Practice Approach to Anonymization:  A Best Practice Approach to Anonymization.pdf

Attachments

    Pang.pdf 

Dingledine.pdf
Wright.pdf
Coull.pdf
Eckersley.pdf
Narayan and Shmatikov.pdf
Shining Light in Dark Places.Understanding Tor.pdf
Why Do People Seek Anonymity on the Internet.pdf
NSA.Zero Trust Architecture Security Model.PDF
Department of Defense Zero Trust Plan.pdf
An Architecture for an Anonymity Network.pdf
alogrithms and tools for anonymization of the interent traffic.pdf
The Impact of Net Neutrality.pdf
Robust De-anonymization Datasets-1.pdf
 
 
 ---
 
# Module 5 - Anonymization defined, types, benefits
What is data anonymization?

Data anonymization describes various techniques to remove or block data containing personally identifiable information (PII
Links to an external site.). Data anonymization promotes data privacy

Links to an external site. while maintaining the integrity and usefulness of the overall data set.

This approach supports analysis and research without revealing the identity of any subjects involved. For example, a drug trial wants all data about a new pharmaceutical's impact, but does not need to know the names of individual patients. Data anonymization uses one of several approaches to halt access to patients' PII while still enabling researchers to benefit from the clinical data. If, in another case, a cybersecurity incident causes a breach, anonymized data helps users stay safe by ensuring their PII has been isolated from the compromised data.

 

Types of Data Anonymization

There are 6 basic types of data anonymization

Links to an external site., including:

    Data masking

Data masking software
Links to an external site. replaces sensitive data, such as credit card numbers, driver’s license numbers, and Social Security Numbers, with either meaningless characters, digits, or symbols – or seemingly realistic, but fictitious, masked data. Masking test data

Links to an external site. makes it available for development or testing purposes, without compromising the privacy of the original information.

Data masking can be applied to a specific field, or to entire datasets, using a variety of techniques such as character substitution, data shuffling, and truncation. Data can be masked on demand or according to a schedule. The data masking suite includes data tokenization
Links to an external site., which irreversibly substitutes personal data with random placeholders, and synthetic data generation

Links to an external site., when the amount of production data is insufficient.

    Pseudonymization

Pseudonymization anonymizes data by replacing any identifying information with a pseudonymous identifier, or pseudonym. Personal information that is commonly replaced includes names, addresses, and Social Security Numbers.

Pseudonymized data
Links to an external site. reduces the risk of PII exposure or misuse, while still allowing the dataset to be used for legitimate purposes. In the pseudonymization vs anonymization Links to an external site. equation, the former is reversible (unlike data tokenization solutions Links to an external site.), and is often used in combination with other privacy-enhancing technologies, such as data masking vs encryption

Links to an external site..

    Data aggregation

Data aggregation, which combines data collected from many different sources into a single view, is used to gain insights for enhanced decision-making, or analysis of trends and patterns. Data can be aggregated at different levels of granularity, from simple summaries to complex calculations, and can be done on categorical data, numerical data, and text data.

Aggregated data can be presented in various forms, and used for a variety of purposes, including analysis, reporting, and visualization. It can also be done on data that has been pseudonymized, or masked, to further protect individual privacy.

    Random data generation

Random data generation, which randomly shuffles data in order to obscure sensitive information, can be applied to an entire dataset, or to specific fields or columns in a database. Often used together with data masking tools
Links to an external site. or data tokenization tools

Links to an external site., random data generation is ideal for clinical trials, to ensure that the subjects are not only randomly chosen, but also randomly assigned to different treatment groups. By combining different types of data anonymization, bias is reduced, while the validity of the results is increased.

    Data generalization

Data generalization, which replaces specific data values with more generalized values, is used to conceal PII, such as addresses or ages, from unauthorized parties. It substitutes categories, ranges, or geographic areas for specific values. For example, a specific address, like 1705 Fifth Avenue, can be generalized to downtown, midtown or uptown. Similarly, the age 55 can be generalized to an age group called 50-60, or middle-aged adults.

    Data swapping

Data swapping replaces real data values with fictitious, but similar, ones. For instance, a real name, like Don Johnson, can be swapped with a fictitious one, like Robbie Simons. Or a real address, like 186 South Street, can be swapped with a fictitious one, like 15 Parkside Lane. Data swapping is similar to the random data generator, but rather than shuffling the data, it replaces the original values with new, fictitious ones.

 

  Source:  https://www.k2view.com/what-is-data-anonymization/#:~:text=There%20are%206%20basic%20types%20of%20data%20anonymization%2C,5.%20Data%20generalization%20...%206%206.%20Data%20swapping

Links to an external site.

 

Why Anonymize Data? Benefits and Drivers

There are several compelling reasons why organizations should systematically anonymize data:

    Upholding Privacy Rights

Anonymization helps prevent misuse of personal data and protects user privacy rights. Regulations like GDPR and CCPA mandate anonymization before processing any consumer data. Fines for non-compliance can amount to 4% of global revenue.

    Increased Data Security

Once anonymized, data holds little value for cybercriminals since identities cannot be stolen or compromised. This greatly reduces risks from potential data breaches.

    Enabling Safe Data Sharing and Collaboration

Anonymized datasets can be freely shared with third parties for research, analytics, machine learning and other purposes without revealing sensitive PII. This facilitates open data collaboration.

    Simplified Legal Compliance

Anonymizing customer data simplifies compliance with regional privacy laws when moving data globally. Data can be anonymized to meet the strictest regulations.

    Maintaining Data Utility

While protecting privacy, anonymization aims to retain useful patterns and insights required for analytics, machine learning, and other applications.

    Greater Transparency

Anonymized data can be made publicly accessible to increase transparency. Eg. government agencies releasing open anonymized datasets.
Techniques and Methods for Anonymization

Various techniques are employed to remove identifying information and ensure anonymity:

    Encryption

Encryption scrambles PII data elements into completely unreadable formats using cryptographic methods like AES-256. Only authorized parties with the appropriate decryption keys can reconstitute the original data.

# Encrypt PII data using PyCrypto AES-256

from Crypto.Cipher import AES

import hashlib

def encrypt(pii_data):

   hash = hashlib.sha256(b‘mysecretkey‘).digest()

   cipher = AES.new(hash, AES.MODE_EAX)

   ciphertext, tag = cipher.encrypt_and_digest(pii_data.encode(‘utf-8‘))

   return ciphertext, tag

pii_data = ‘John Doe|123 Main St‘

encrypted_data, nonce = encrypt(pii_data)

print(encrypted_data)

# b‘\x8b\xc2\x9b\x08\xddT\xect\x87\xf6\x94\xf2...‘

 

    Generalization

This technique replaces specific values like names and ages with broader categories like occupation, age ranges, zip codes etc. This increases ambiguity while preserving overall patterns.

For example:

Original Data
	

Anonymized Data

John Doe, 36
	

Legal Professional, 30s

Jane Dean, 41
	

Medical Professional, 40s

 

    Randomization

Random noise is added to various data attributes to mask the actual values. For example, slightly altering timestamps, geo-locations, transaction amounts in a randomized manner. This preserves overall statistical properties while masking original data.

    Differential Privacy

This injects mathematical noise into statistical databases to prevent identification of individuals through querying, even if the attacker has outside information. Used by companies like Apple and Google.

    Pseudonymization

Here, actual PII identities are replaced with artificial identifiers or pseudonyms that are randomly generated. This separates identities from the associated data.

For example:

Name
	

Email
	

Pseudonym

John Doe
	

jdoe@email.com
	

9371hk2j3

Jane Dean
	

jadean@email.com
	

8237kln23

 

    Synthetic Data Generation

Fully artificial and simulated data is created such that it statistically resembles real data without being directly copied from it. Used to expand limited datasets.
Putting Anonymization into Practice

To implement data anonymization effectively:

    First perform a risk assessment on datasets based on sensitivity to determine the extent of anonymization required.
    Choose the right anonymization techniques based on data types, use cases and attack models.
    Anonymize data as early as possible – at time of collection or entry into datastores.
    Continuously monitor and refine techniques to prevent re-identification if new vulnerabilities emerge.
    Balance data utility vs privacy protection – don‘t blindly over-anonymize and reduce usefulness.
    Utilize robust open source and commercial solutions like ARX, Amnesia, Privitar, Informatica, TokenEx.
    Employ pseudonymization and differential privacy methods to enable re-identification only when required.

 
Legal Requirements for Anonymization

Major privacy regulations worldwide mandate the use of anonymization under specific conditions:

    GDPR– Sensitive EU citizen data must be anonymized before transferring or processing outside the EU region.
    CCPA/CPRA– Any data being sold or disclosed requires anonymization as per CCPA‘s "reasonable linkability" standard.
    HIPAA– Allows sharing of anonymized health data if very low risk of re-identification.
    PDPA– Thailand, Philippines privacy laws also require consent before sharing anonymized data.

 

Globally, over 120 countries now have data privacy laws – making systematic anonymization necessary to avoid substantial penalties.
Limitations and Challenges With Anonymization

While anonymization has clear benefits, some key challenges remain:

Irreversible Process – Limits re-identification even for legitimate internal purposes once removed. Maintaining mapping tables has security risks.

Complex Implementation – Getting it right requires significant data science, cryptography and domain expertise – especially for large diverse datasets.

Lowering Data Utility – Excessive poorly-tuned anonymization can destroy analytic value, patterns, and accuracy.

Re-identification Risks – Sophisticated attacks or insider threats may be able to de-anonymize some sensitive datasets.

Increased Costs – Manual anonymization and custom tooling development requires additional effort and resources.

Thus, the ideal solution involves semi-reversible pseudonymization coupled with strong access controls and auditing.
The Future of Data Anonymization

Data anonymization adoption will grow significantly in the near future driven by trends like:

    Increasing consumer privacy demands requiring consent and anonymization.
    New data privacy laws like India‘s upcoming data protection law providing users more control.
    High impact of data breaches forcing stronger cybersecurity measures like anonymization.
    Advances in anonymization techniques using ML, edge computing and federated learning.
    Higher maturity of risk assessment and mitigation.
    User-centric tools empowering individuals to control anonymizing their personal data.
    Growth of platforms like Ekata and InfoSum that offer privacy-preserving data clean rooms for analysis.
    Integration of anonymization capabilities into mainstream business intelligence and analytics tools.

 

Overall, data anonymization enables the critical data analysis that our increasingly digital economy relies on – while upholding the privacy and consent that users rightfully expect. Getting the trade-offs right will require collaboration between regulators, technology leaders, and the public.

Source: https://www.marketingscoop.com/ai/data-anonymization/


---

# Google's FLoC Article Related to Anonymization

Good day,

a fellow classmate provided this url during office hours discussing Google's FLoC idea which relates to this week's topic, Anonymization. I encourage everyone to take a look.

https://www.eff.org/deeplinks/2021/03/googles-floc-terrible-idea

Links to an external site.

best, jason