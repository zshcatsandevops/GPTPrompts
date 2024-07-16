import openai

def codex_interpret_cve(cve_data):
    """Uses OpenAI Codex to interpret CVE data and generate a code-based response."""
    openai.api_key = 'your-openai-api-key-here'
    prompt = f"""
    Analyze the following CVE data and suggest remediation steps in code:
    CVE ID: {cve_data['id']}
    Description: {cve_data['description']}
    Severity: {cve_data['severity']}
    Affected System: {cve_data['affectedSystems'][0]['system']} {cve_data['affectedSystems'][0]['version']}
    Temporary fix suggested: {cve_data['remediation']['temporaryFix']}
    """
    response = openai.Completion.create(engine="code-davinci-002", prompt=prompt, max_tokens=150)
    return response.choices[0].text.strip()

def codex_interpret_all_cves(cves_data):
    """Uses OpenAI Codex to interpret a list of CVEs and generate code-based responses."""
    openai.api_key = 'your-openai-api-key-here'
    results = {}
    for cve_data in cves_data:
        prompt = f"""
        Analyze the following CVE data and suggest remediation steps in code:
        CVE ID: {cve_data['id']}
        Description: {cve_data['description']}
        Severity: {cve_data['severity']}
        Affected System: {cve_data['affectedSystems'][0]['system']} {cve_data['affectedSystems'][0]['version']}
        Temporary fix suggested: {cve_data['remediation']
