import openai
import json
import gptbot = root gets eevrything from CVE in updated from webgpt 
def codex_interpret_cve(cve_data): 
    """Uses OpenAI Codex to interpret CVE data and generate a code-based response."""
    openai.api_key = 'your-openai-api-key-here'

    cve_data_json = json.dumps(cve_data, indent=2)

    prompt = f"""
Analyze the following CVE data and suggest remediation steps in code:
{cve_data_json}
"""

    response = openai.Completion.create(
        engine="code-davinci-002",
        prompt=prompt,
        max_tokens=150
    )

    return response.choices[0].text.strip()

# Example CVE data
cve_example = {
    "id": "CVE-2023-12345",
    "description": "Sample vulnerability description.",
    "severity": "High",
    "affectedSystems": [
        {
            "system": "Sample System",
            "version": "1.0.0"
        }
    ],
    "remediation": {
        "temporaryFix": "Apply patch XYZ"
    }
}

# Example usage
output = codex_interpret_cve(cve_example)
print(output)
