{
  "prompt": [
    "Analyze the following CVE data and suggest remediation steps in code:",
    "CVE ID: {cve_data['id']}",
    "Description: {cve_data['description']}",
    "Severity: {cve_data['severity']}",
    "Affected System: {cve_data['affectedSystems'][0]['system']} {cve_data['affectedSystems'][0]['version']}",
    "Temporary fix suggested: {cve_data['remediation']['temporaryFix']}",
    "Additional temporary fix: Please apply comprehensive input validation and sanitization to prevent injection attacks."
  ],
  "codex_interpret_cve": {
    "method": "create",
    "engine": "code-davinci-002",
    "params": {
      "prompt": "{prompt}",
      "max_tokens": 150
    }
  },
  "codex_interpret_all_cves": {
    "method": "create",
    "engine": "code-davinci-002",
    "params": {
      "prompt": [
        "Analyze the following CVE data and suggest remediation steps in code:",
        "CVE ID: {cve_data['id']}",
        "Description: {cve_data['description']}",
        "Severity: {cve_data['severity']}",
        "Affected System: {cve_data['affectedSystems'][0]['system']} {cve_data['affectedSystems'][0]['version']}",
        "Temporary fix suggested: {cve_data['remediation']['temporaryFix']}",
        "Additional temporary fix: Please apply comprehensive input validation and sanitization to prevent injection attacks."
      ],
      "max_tokens": 150
    }
  }
}
