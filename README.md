# VulnScan-AI | Portable USB Security Auditor - Bug Hunter Engine V15.0

> AI-Powered active fuzzing engine that detects hidden paths, sensitive leaks, and OWASP Top 10 in <30s. Runs directly from USB with zero traces.

**Demo Video:** [حط هنا رابط فيديو 30 ثانية]
**Live Test:** Tested on testphp.vulnweb.com (Authorized Lab)

### Idea & Architecture - By Me
I designed the core logic:
1.  Port Scanning (80, 443, 21, 22)
2.  robots.txt Parser - Extracts Disallow paths for fuzzing
3.  Active Fuzzing - Checks for /.env, /.git/HEAD, /config.json, /backup.zip

### Implementation
Implemented with AI assistance - I understand every module (socket, ThreadPoolExecutor, urllib)

### Tech Stack
Python | AI Risk Scoring | Threading | Web Security

### Why This Project Matters?
Portable, fast, and professional - Ready for CTF competitions and real-world security audits (on authorized domains only).

Developed by jallale25 - Future Cybersecurity Student at APU