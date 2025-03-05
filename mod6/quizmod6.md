Flag question: Question 1
Question 1 10 pts
Per the MITRE ATT&CK framework for Mobile devices, what is the mitigation steps for Hijack Execution Flow (T1625)?

The MITRE framework suggests attestation and system partition integrity checks to prevent malicious apps from hijacking code execution flow. Remote attestation compares the state of the device or payload with a remote verifier to detect alterations. System integrity checks protect boot files and other critical system files by making them read only, restricting access, and comparing the hash values before execution. 
https://attack.mitre.org/techniques/T1625/
 
Flag question: Question 2
Question 2 10 pts
How does "just-in-time" compiling differ from normal code compilation?

JIT compiled code is translated at execution, rather than ahead of time with normal code compilation. This allows JIT compiled code to be more adaptable to different runtime environments and resource/execution constraints as needed which statically compiled code can't adjust for. This allows for on the fly optimizations like speeding up commonly executed paths, and remains secure because the precompiled byte code that's translated to machine code at run time can be attested.
 
Flag question: Question 3
Question 3 10 pts
"Juice-jacking" is an attack where an adversary sets up a rogue USB "charging station" for the public to plug into, but, in addition to charging the phone, it can mount the phone's storage device and either read data or place malware on it.  Which of the following countermeasures can successfully prevent a juice-jacking attack?
Group of answer choices
Mount the storage device as read-only
**Only use wall outlets to charge your phone in public
Use only USB charging stations provided by well-known sponsors (Verizon, T-Mobile, etc.)
Charge only using USB 2.0 or later
 
Flag question: Question 4
Question 4 10 pts
The use of a "process VM", like Dalvik, allows mobile applications to have safe access to all system resources.
Group of answer choices
True
**False
 
Flag question: Question 5
Question 5 10 pts
Explain how some of the biometric authentication mechanisms (face recognition, fingerprints, finger swipes, etc.) on mobile devices when enabled can be more secure than mobile passwords and PIN's.

Compared to passwords and pins, biometrics can be more secure. On one hand they are something you carry with you and can't be forgotten, and are potentially a longer length/higher entropy than alphanumeric passwords or numeric pins. Passwords can also be transferred or stolen, compared to biometrics which only one person can hold. And biometrics can be used in addition to a password/pin for multi factor authentication. 

Flag question: Question 6
Question 6 10 pts
What are the components that make up the Enterprise Mobile Device Lifecycle?

The Enterprise Mobile Device Development Lifecycle includes understanding the mobile use case and current capabilities, conducting a risk assessment, selecting deployment, device, and processes for the use case and risk factors, setting the chosen policy, configuring and provisioning devices for the policy, verifying the devices and policies by testing, auditing the devices throughout, and disposing or safely reusing of devices and policies when the lifecycle begins a new phase or a device changes hands.

Flag question: Question 7
Question 7 10 pts
The Dalvik VM process for writing Android apps can be done in two ways.  1.)  The new process VM called Android Runtime (ART) with the default language suggested by the Android Studio IDE being Kotlin.  The bytecode is still Dex (Dalvik executable, *.dex files), therefore the newer development process is Kotlin -> Dex executable-> Android Runtime (ART).  Or 2.)  the more familiar/older process being Software Development Kit (SDK) -> Java -> Dex executable/.APK file      
Group of answer choices
**True
False
 
Flag question: Question 8
Question 8 10 pts
The Android OS runs based on the Linux kernel, is open-source, and is maintained by Google Inc. T or F
Group of answer choices
**True
False
 
Flag question: Question 9
Question 9 10 pts
What threats are addressed with Remote/Secure Wipe?

If a device is physically compromised like if it is lost or stolen, the data on the device can be removed remotely so that anyone who has access to the device can no longer access its contents. This could also happen with a compromised device taken over by malware to limit the spread or in the case of an insider threat to limit access to networks or data.
 
Flag question: Question 10
Question 10 10 pts
List two ways malware can attempt to hide itself on a mobile device.

Malware on a mobile device could use advanced tactics like hijacking execution flow to execute malicious code hidden from the user, or modifying system files to remain undetected. It could similarly disguise itself as a system process or use obfuscation techniques to prevent signature detection.

Flag question: Question 11
Question 11 10 pts
Does Jailbreaking or Rooting a device bypass built-in restrictions on security, OS use, and other functions?   
Group of answer choices
**True
False
 
Flag question: Question 12
Question 12 10 pts
What threats are addressed with Mobile Threat Defense?
Mobile Threat Defense systems can detect network attacks like MITM, app based attacks like malicious apps or data leaks, platform attacks like rootkits, detect out of date versions of software/OS and configurations, block blacklisted apps and sites, stop unauthorized certificates from being installed, and potentially prevent phishing.
 
Flag question: Question 13
Question 13 10 pts
Per the MITRE ATT&CK framework for Mobile devices, what is the mitigation steps for Endpoint Denial of Service (T1642)?

Mitigating a mobile device endpoint from being DOSed involves updating the device to patch security vulnerabilities that enable the DOS to happen, and preventing apps from gaining administrative privileges to make changes that could cause DOS to happen such as by training users not to immediately allow permissions.

https://attack.mitre.org/techniques/T1642/
 
Flag question: Question 14
Question 14 10 pts
Under the “Operate & Maintain” of the Lifecycle, list six (6) items that comprehensive auditing should cover?

A comprehensive audit should cover enumerating enterprise audit objectives, using periodic audits to establish a security baseline, using auditors with security assessment experience, using automated audit processes to cover all IT infrastructure and mobile devices, analyze the audit results rather than use a checklist for compliance, and use a third party audit to report on enterprise risks.
 
Flag question: Question 15
Question 15 10 pts
Briefly discuss why Bring Your Own Device (BYOD) policies are necessary to enhance corporate IT security and how it can be circumvented by end-users.

BYOD policies are necessary because employees are likely to use personal devices and mix personal and enterprise work on devices where sensitive enterprise data could leak to an untrusted party through the use of the device, or the device may be compromised which raises threats to the enterprise data and networks. Setting a policy informs employees on acceptable uses and what not to do, and establishes boundaries and expectations. BYOD policies can be circumvented by a user who breaks the policies outright like installing unapproved apps, shares the device, backs up enterprise data to cloud storage, etc. But also the user might manage to circumvent BYOD directly by resetting the device or otherwise disabling security controls or software. Modifying the device with jailbreaking/rooting could also be used to circumvent security controls. 

Flag question: Question 16
Question 16 10 pts
Provide three characteristics of Mobile Adhoc Networks (MANET's)?

A mobile adhoc network is a decentralized self organized network of wireless devices where nodes act as hosts and routers autonomously, the topology of the network is random and changes as the devices connect and route traffic to one another, and there are usually constraints on the bandwidth, memory, and power of the devices since they can be smaller mobile devices on battery. There also isn't much built in security as there is no centralized firewall or other monitoring or configuration checks in place.
 
Flag question: Question 17
Question 17 10 pts
List five (5) countermeasures/mitigations to a mobile device threat of “exploitation of underlying vulnerabilities in devices”?

Underlying vulnerabilities can be countered by selecting devices carefully with security in mind, isolating the OS and applications, quickly patching vulnerabilities with updates, mobile application vetting, and using mobile threat defense systems. 
 
Flag question: Question 18
Question 18 10 pts
In terms of threat models for mobile platforms are; 1. collecting private data, 2. utilizing computing resources and 3. conducting harmful malicious actions goals which attackers are trying to achieve?   True or False
Group of answer choices
**True
False
 
Flag question: Question 19
Question 19 10 pts
Per the MITRE ATT&CK framework for Mobile devices, what is hooking?

Hooking involves an attacker hooking into an API and redirecting the calls to change the data or behavior, or to bypass security. It can be used to redirect calls for execution and for privilege escalation.

https://attack.mitre.org/techniques/T0874/

 
Flag question: Question 20
Question 20 10 pts
Pretend you're a piece of malware.  List 2 ways you can potentially discover the fact you're running in a virtualized environment.

Malware can identify virtualized environments by checking for giveaways like identifiers, processes, drivers, and configurations like common MAC addresses given to VMs. And it could also use more advanced methods like timing CPU operations and examining memory.
 
Flag question: Question 21
Question 21 10 pts
List six (6) countermeasures/mitigations to a mobile device threat of “Mobile Malware”?

Mobile malware can be countered with user education, selecting devices based on security, quickly patching vulnerabilities with software updates, vetting applications, isolating OS and applications, and using mobile threat defense systems.
 
Flag question: Question 22
Question 22 10 pts
List three mobile platform attack vectors used by adversaries.

Adversaries can use several attack vectors on mobile devices like mobile network services, wifi and internet connection in general, with Bluetooth, and by connected devices over USB and other connections and sensors.
 
Flag question: Question 23
Question 23 10 pts
Under the “Implement Enterprise Mobility Strategy” of the Lifecycle, are the following items to consider; a. On-Premises Architecture, b. Cloud Architecture, c. Device Configuration, d. Device Provisioning, and e. Verification Testing.   
Group of answer choices
**True
False
 
Flag question: Question 24
Question 24 10 pts
What threats are addressed with Mobile Application Vetting?

Mobile Application Vetting can identify vulnerabilities and malicious code in applications such as poor use of cryptography, mishandling information, what dependencies are in use, use of untrusted cloud functions, data collection/selling, and camera/mic use and other permissions the app requires. It can also find malicious device management profiles, detect mobile malware, user privacy violatoins, and find exploitation of underlying vulnerabilities.
 
Flag question: Question 25
Question 25 10 pts
List five (5) countermeasures/mitigations to a mobile device threat of “Credential theft via phishing”?

Credential theft by phishing can be countered by educating users/employee with phishing training and tests, using mobile threat defense systems, implementing mobile device security policies, using strong authentication such as mfa, and setting up remote wiping of devices.
 
Flag question: Question 26
Question 26 10 pts
Are Trojan horses, worms, rootkits and botnets the most “common” mobile malware being used by the adversary to attack mobile platforms?
Group of answer choices
**True
False
 
Flag question: Question 27
Question 27 10 pts

Explain what a Mobile Adhoc Network (MANET) is?

A Mobile adhoc network is a decentralized network of mobile devices that self arrange a network to receive and route messages to one another in a self healing network. Each device is a node and a router in a dynamic topology without a fixed infrastructure. Essentially multiple mobile devices form a peer to peer network with their neighbors to route traffic among themselves without the need for other links. For example, a MANET could be made up of wireless IoT devices and sensors near each other that share messages with one another.

Flag question: Question 28
Question 28 10 pts
Which of the following are potential drawbacks to mobile computing? (choose all that apply)
Group of answer choices
**Limited computational power
**Lack of physical security
**Limited access control complexity (mobile passwords, short PIN's, for example)
**Inability to provide patch updates to devices caused by the number of OS framework software and vendor implementations that Original Equipment Manufacturers (OEM's) have to support.