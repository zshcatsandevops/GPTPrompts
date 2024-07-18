import requests
import openai
import json
import logging

# Configure logging
logging.basicConfig(filename='cve_interpreter.log', level=logging.INFO)

openai.api_key = 'your-openai-api-key-here'

def fetch_cve_data(cve_id):
    url = f"https://services.nvd.nist.gov/rest/json/cve/1.0/{cve_id}"
    response = requests.get(url)
    return response.json()

def codex_interpret_cve(cve_data):
    cve_data_json = json.dumps(cve_data, indent=2)
    prompt = f"""
Analyze the following CVE data and suggest remediation steps in code:
{cve_data_json}
"""
    try:
        response = openai.Completion.create(
            engine="code-davinci-002",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        logging.error(f"Error interpreting CVE data: {e}")
        return None

def main():
    cve_id = "CVE-2023-12345"  # Example CVE ID
    cve_data = fetch_cve_data(cve_id)
    interpretation = codex_interpret_cve(cve_data)
    
    if interpretation:
        logging.info(f"Interpretation for {cve_id}: {interpretation}")
    else:
        logging.error(f"No interpretation available for {cve_id}")

if __name__ == "__main__":
    main()
