def universal_prompt_builder(topic, format="question", persona="helpful assistant", constraints=""):
  """
  This function generates a prompt for a large language model.

  Args:
    topic: The topic of the prompt.
    format: The desired format of the output (e.g., "question", "story", "code").
    persona: The desired persona of the language model (e.g., "helpful assistant", "creative writer").
    constraints: Any additional constraints on the output (e.g., "must be less than 100 words").

  Returns:
    A string containing the generated prompt.
  """

  prompt = f"Generate a {format} about {topic}."

  if persona:
    prompt = f"As a {persona}, {prompt}"

  if constraints:
    prompt = f"{prompt} {constraints}"

  return prompt

# Example usage
print(universal_prompt_builder(topic="the meaning of life", format="poem", persona="philosophical AI"))
