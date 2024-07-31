import requests import openai import json import logging import sys import os

logging.basicConfig(filename='cve_interpreter.log', level=logging.INFO) openai.api_key = os.getenv('OPENAI_API_KEY')

def fetch_cve_data(cve_id): url = f"https://services.nvd.nist.gov/rest/json/cve/1.0/{cve_id}" response = requests.get(url) return response.json()

def gpt4_interpret_cve(cve_data, model="gpt-4"): cve_data_json = json.dumps(cve_data, indent=2) prompt = f"Analyze the following CVE data and suggest remediation steps in code:\n{cve_data_json}" try: response = openai.Completion.create( engine=model, prompt=prompt, max_tokens=150 ) return response.choices[0].text.strip() except Exception as e: logging.error(f"Error interpreting CVE data: {e}") return None

def generate_image(description): try: response = openai.Image.create( prompt=description, n=1, size="1024x1024" ) image_url = response['data'][0]['url'] return image_url except Exception as e: logging.error(f"Error generating image: {e}") return None

def main(): if len(sys.argv) < 2: print("Usage: python cve_interpreter.py <CVE_ID> []") sys.exit(1) cve_id = sys.argv[1] model = sys.argv[2] if len(sys.argv) > 2 else "gpt-4"

 model = sys.argv[2] if len(sys.argv) > 2 else "DALL-E[3]"
