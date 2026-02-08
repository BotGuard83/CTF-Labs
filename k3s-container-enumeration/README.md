# K3s Container Enumeration Lab

## Overview

This lab demonstrates container enumeration techniques against a Kubernetes K3s environment after gaining initial access to a container.

This simulates real-world attacker post-exploitation behavior.

---

## Initial Access

Access obtained via compromised credentials using Hydra brute-force attack against exposed web login.

Target:
192.168.1.183

Credentials discovered:
admin : password123

---

## Container Enumeration

Commands used:

id
whoami
ps aux
mount
ls /
find / -name "*.sock" 2>/dev/null

Discovered:

/run/k3s/containerd/containerd.sock

---

## Security Significance

This socket provides access to container runtime and could allow:

• Container escape attempts  
• Host filesystem access  
• Privilege escalation  
• Kubernetes cluster compromise  

---

## Skills Demonstrated

• Container enumeration  
• Kubernetes security assessment  
• Linux privilege boundary analysis  
• Post-exploitation techniques  
• Real-world attacker workflow  

---

## Tools Used

Kali Linux  
Hydra  
Kubernetes (K3s)  
Containerd  
Linux enumeration tools  

---

## Author

Giuseppe Bottaro  
GitHub: https://github.com/BotGuard83
