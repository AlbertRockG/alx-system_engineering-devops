# Postmortem: The Great PHP Module Heist

**Issue Summary**

On **September 15, 2024**, from **09:00 AM to 10:30 AM UTC**, our website decided to take an unexpected coffee break. Approximately **60% of users** encountered the dreaded **HTTP 500 Internal Server Error** when trying to access our site. The culprit? A missing PHP module that Apache relies on to process PHP files. In other words, our server misplaced a critical piece of its own puzzle.

**Timeline**

- **09:00 AM UTC** - Monitoring systems lit up like a Christmas tree with HTTP 500 errors.
- **09:05 AM UTC** - On-call engineer receives alerts and reluctantly puts down their coffee.
- **09:10 AM UTC** - Checked Apache logs; initial hunch pointed to a misconfiguration.
- **09:20 AM UTC** - Restarted Apache service, hoping for a miracle. No dice.
- **09:30 AM UTC** - Noticed PHP files weren't being served; suspected PHP-FPM had gone AWOL.
- **09:40 AM UTC** - Verified PHP-FPM was running smoothly; confusion intensifies.
- **09:50 AM UTC** - Escalated the issue to the DevOps "detectives."
- **10:00 AM UTC** - DevOps team employed `strace` to trace Apache's system calls; discovered the missing `libphp5.so` module.
- **10:15 AM UTC** - Reinstalled the missing PHP module; Apache seemed pleased.
- **10:20 AM UTC** - Restarted Apache; services restored, users rejoiced.
- **10:30 AM UTC** - Monitored system to confirm stability; incident officially resolved.

**Root Cause and Resolution**

The root cause was the unexpected disappearance of the `libphp5.so` module, essential for Apache to process PHP files. A recent system update, orchestrated by a misconfigured package management script, accidentally removed this module. Without it, Apache couldn't interpret PHP code, leading to HTTP 500 errors site-wide.

To resolve the issue, we attached `strace` to the running Apache process. This revealed that Apache was frantically searching for `libphp5.so` but coming up empty-handed—much like searching for your keys when they're in your pocket. We promptly reinstalled the missing PHP module using the package manager and restarted Apache. Services were restored immediately, and normal operations resumed.

**Corrective and Preventative Measures**

- **Audit Package Scripts**: Our package management scripts will be reviewed to prevent unauthorized module "heists."
  - *Task*: Implement safeguards in scripts to avoid accidental removal of critical packages.
- **Enhance Monitoring**: Introduce alerts for missing or corrupted essential modules.
  - *Task*: Set up file integrity monitoring for `libphp5.so` and other vital components.
- **Automate Module Management**: Employ Puppet to ensure essential modules are always present and accounted for.
  - *Task*: Create Puppet manifests to manage and enforce the presence of necessary PHP modules.
- **Update Documentation**: Enrich our runbooks with this incident's learnings for future reference.
  - *Task*: Add a troubleshooting section on using `strace` and conduct training sessions for the team.

---

By turning a technical hiccup into a detective story, we hope this postmortem not only informs but also entertains. After all, even servers have their mysterious ways, and it's up to us to keep them on the straight and narrow.
