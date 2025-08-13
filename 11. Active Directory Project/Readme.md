
# Active Directory Security & Administration Project
This project is a comprehensive, hands-on learning program focused on Active Directory (AD) administration, security hardening, and threat detection.
It consists of 60 structured tasks organized into three progressive levels—Basic, Intermediate, and Advanced—designed to simulate real-world enterprise scenarios in a controlled lab environment.
Participants gain experience in user and group management, Group Policy deployment, privileged access control, certificate services, DNS security, advanced threat detection, and disaster recovery using industry-standard tools and best practices.

## Project Overview
The project covers:
Core AD administration fundamentals.
Implementation of security policies and hardening measures.
Advanced threat detection and mitigation techniques.
Disaster recovery and compliance alignment.
It is designed to be performed in a virtual lab setup to ensure safe experimentation and learning without impacting production environments.

## Key Implementations
Level 1 – Basic Security & Administration
Created and managed user accounts and security groups.
Applied Organizational Unit (OU) structures and basic Group Policy Objects (GPOs).
Configured password and account policies.
Enabled basic auditing and account lockout monitoring.

Level 2 – Intermediate Hardening & Delegation
Implemented fine-grained password policies for admins.
Configured delegated permissions following least privilege principles.
Disabled insecure protocols (SMBv1, NTLM where Kerberos is available).
Deployed Local Administrator Password Solution (LAPS).
Configured AD Certificate Services and DNS security measures.

Level 3 – Advanced Security & Threat Detection
Deployed Privileged Access Management (PAM) and Just Enough Administration (JEA).
Integrated Multi-Factor Authentication (MFA) via ADFS.
Simulated Golden Ticket and DCShadow attacks for detection training.
Performed disaster recovery drills and high-availability setups.
Applied Microsoft, NSA, and CIS security baselines.

## Tools & Technologies
| Category                         | Tools / Technologies                                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Operating Systems & Services** | Windows Server (Evaluation), Active Directory Domain Services (AD DS), Active Directory Federation Services (ADFS) |
| **Administrative Tools**         | RSAT (Remote Server Administration Tools), Windows Admin Center, PowerShell (ActiveDirectory Module)               |
| **Security & Compliance**        | Microsoft Security Compliance Toolkit, LAPS (Local Administrator Password Solution), DNSSEC                        |
| **Monitoring & Auditing**        | Event Viewer, Azure Sentinel (Free Tier), Custom Audit Policies, SACLs                                             |
| **Lab & Simulation**             | Hyper-V for DC cloning, Virtualized test network for attack simulations                                            |


## Achievements
Built a fully functional Active Directory lab from scratch.
Enforced security policies in line with industry standards.
Successfully detected and mitigated simulated AD attacks.
Developed documentation and reporting skills for security configurations.
Gained hands-on experience with enterprise-grade AD security tools.

## Recommendations
Implement continuous monitoring using Microsoft Defender for Identity.
Review Group Policies regularly for security and relevance.
Adopt tiered administration to minimize privilege escalation risks.
Maintain offline backups for critical AD data.
Explore Azure AD integration for hybrid identity management.

## Conclusion
This project provided end-to-end exposure to AD administration, security hardening, and enterprise threat detection. The structured approach ensured mastery of core administration, advanced security controls, and disaster recovery techniques, enabling direct application to corporate IT environments.
