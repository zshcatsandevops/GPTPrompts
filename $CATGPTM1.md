[
  {
    "service": "dalle",
    "prompt": "A futuristic city skyline at sunset",
    "size": "1024x1024",
    "number_of_images": 1
  },
  {
    "service": "bing",
        elif service == "bing":
            query = request_data.get("query")
            number_of_results = request_data.get("number_of_results", 5)
            response = process_bing_request(query, number_of_results)
        else:
            response = {"error": "Unknown service"}
        
        responses.append(response)
    
    return json.dumps(responses, indent=2)

# Example usage with a combined JSON request
combined_requests = '''
[
  {
    "service": "dalle",
    "prompt": "A futuristic city skyline at sunset",
    "size": "1024x1024",
    "number_of_images": 1
  },
  {
    "service": "bing",
    "query": "latest news on AI",
    "number_of_results": 5
  }
]
'''

response = handle_requests(combined_requests)
print(response)
