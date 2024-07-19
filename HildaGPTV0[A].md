import requests, openai, json, logging, sys, os
logging.basicConfig(filename='cve_interpreter.log', level=logging.INFO)
openai.api_key = os.getenv('OPENAI_API_KEY')

def fetch_cve_data(cve_id): 
    url = f"https://services.nvd.nist.gov/rest/json/cve/1.0/{cve_id}"
    return requests.get(url).json()

def gpt4_interpret_cve(cve_data, model="gpt-4"): 
    prompt = f"Analyze the following CVE data and suggest one sentence remediation steps in code:\n{json.dumps(cve_data, indent=2)}"
    try: 
        return openai.Completion.create(engine=model, prompt=prompt, max_tokens=30).choices[0].text.strip()
    except Exception as e: 
        logging.error(f"Error interpreting CVE data: {e}")
        return None

def generate_image(description): 
    try: 
        return openai.Image.create(prompt=description, n=1, size="1024x1024")['data'][0]['url']
    except Exception as e: 
        logging.error(f"Error generating image: {e}")
        return None

def main(): 
    cve_id, model = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "gpt-4")
    if "gpt" in model:
        print(gpt4_interpret_cve(fetch_cve_data(cve_id), model))
    else:
        print(generate_image("Description for DALL-E image"))

if __name__ == "__main__":
    main()
