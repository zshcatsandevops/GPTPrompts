import requests
import openai
import json
import logging
import time
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(filename='cve_interpreter.log', level=logging.INFO)

openai.api_key = 'your-openai-api-key-here'

def fetch_latest_cve_id():
    url = "https://services.nvd.nist.gov/rest/json/cves/1.0?resultsPerPage=1&sortDescending=true"
    response = requests.get(url)
    if response.status_code == 200:
        cve_items = response.json().get('result', {}).get('CVE_Items', [])
        if cve_items:
            return cve_items[0]['cve']['CVE_data_meta']['ID']
    return None

def fetch_cve_data(cve_id):
    url = f"https://services.nvd.nist.gov/rest/json/cve/1.0/{cve_id}"
    response = requests.get(url)
    return response.json()

def codex_interpret_cve(cve_data):
    cve_data_json = json.dumps(cve_data, indent=2)
    prompt = f"""Analyze the following CVE data and suggest remediation steps in code: {cve_data_json}"""
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
    last_cve_check = datetime.min
    while True:
        if datetime.now() - last_cve_check >= timedelta(hours=1):
            cve_id = fetch_latest_cve_id()
            if cve_id:
                cve_data = fetch_cve_data(cve_id)
                interpretation = codex_interpret_cve(cve_data)
                if interpretation:
                    logging.info(f"Interpretation for {cve_id}: {interpretation}")
                else:
                    logging.error(f"No interpretation available for {cve_id}")
            last_cve_check = datetime.now()
        time.sleep(60)  # Sleep for a minute before checking again

if __name__ == "__main__":
    main()
