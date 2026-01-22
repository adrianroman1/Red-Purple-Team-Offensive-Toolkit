# 🟣 Purple Team: Adversary Emulation & Detection

This module demonstrates the collaboration between Red Team (Offensive) and Blue Team (Defensive) to validate and improve detection capabilities.

## 🏹 Scenario: PowerShell Lateral Movement
- **Objective:** Emulate Tactic [T1021.006](https://attack.mitre.org).
- **Red Side:** Executing obfuscated PowerShell scripts to establish remote sessions.
- **Blue Side:** Analyzing SIEM logs for Event ID 4624 (Logon) and process creation of `wsmprovhost.exe`.

## 🔄 Improvement Loop
1. Execute attack simulation.
2. Identify detection gaps in EDR/SIEM.
3. Deploy Sigma rules or hardening policies.
4. Re-verify until the IoC (Indicator of Compromise) is detected.
