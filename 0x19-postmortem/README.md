Postmortem
`Based on 0x17-web_stack_debugging_3`
![500](https://miro.medium.com/v2/resize:fit:1050/1*P-Zu0RX33TUT0S6yyFNPYA.jpeg)
**Issue Summary:**

- **Duration:** The website was out for about 10 minuets on 15/8/2024, between 12:05 AM and 12:15 AM CAT
- **Impact:** Users were encountered a 500 Internal Server Error during this period.
- **Root Cause:** The server malfunctioned due to a typo in a configuration file.

**Timeline:**

- **Issue Detected:** Monitoring systems raised alerts at 12:05 AM CAT regarding the error.
- **Actions Taken:**
  - Engineers investigated server logs to identify the problem.
- **Misleading Paths:**
  - Initially thought the issue might be related to server settings or updates.
- **Escalation:** Senior engineers were engaged to lead the investigation.
- **Resolution:** A script was run on the server to correct the typo in the configuration file at 12:14 AM CAT, restoring the website.

**Root Cause and Resolution:**

- **Root Cause:** A typo in a configuration file.
- **Resolution:** A script was deployed to automatically fix the typo.

**Corrective and Preventative Measures:**

- **Improvements/Fixes:**
  - Pair Programming.
  - Testing
  - Automated Backups
- **Tasks:**
  - Review the code by another when making complex configuration changes to reduce the likelihood of errors
  - Test configuration files before deployment.
  - Regularly back up configuration files so we can restore them if a typo causes an issue.
