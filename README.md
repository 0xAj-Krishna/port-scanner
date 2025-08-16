# 🔎 Port Scanner

A lightweight **multi-threaded Python Port Scanner** that allows you to scan specific ports or a range of ports on a given target (IP/Domain).

---


## 🚀 Features
- Scan single ports (`-p`)
- Scan port ranges (`-p-`)
- Works with both IP addresses and domain names
- Multi-threaded for faster scanning

---

## 🛠️ Usage
```bash
python3 port-scanner.py [TARGET] [OPTION]

```
---

## Options
```bash
-p <PORT> → Scan a single port

-p- <START_PORT-END_PORT> → Scan a port range
```
---

## 🔧 Examples
```bash
# Scan a single port
python3 port-scanner.py example.com -p 80

# Scan a range of ports
python3 port-scanner.py example.com -p- 20-100
```

---

## 📌 Example Output
```bash
     █████╗      ██╗
    ██╔══██╗     ██║
    ███████║     ██║
    ██╔══██║██   ██║
    ██║  ██║╚█████╔╝
    ╚═╝  ╚═╝ ╚════╝ 
        Port Scanner
----------------------------------------
 Author : AJ
 LinkedIn: https://www.linkedin.com/in/blue-aj
 Github : https://github.com/0xAj-Krishna
 Twitter : https://x.com/B1ue_Aj
----------------------------------------

Scanning example.com (93.184.216.34)...
Port 80 is open
Port 443 is open
```
---
## 🚀 Languages
<p align="left">
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> 
</p>

---
## ⚡ Requirements

- Python 3.x

- No external libraries required (uses only socket, threading, and sys from the Python standard library)

## 🧑‍💻 Author

- AJ

## Connect with me:
<p align="left">
<a href="https://x.com/B1ue_Aj" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="0xAj" height="30" width="40" /></a>
<a href="https://www.linkedin.com/in/blue-aj" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="0xAj" height="30" width="40" /></a>
<a href="https://medium.com/@0x_AJ" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/medium.svg" alt="@0xAj" height="30" width="40" /></a>
</p>
