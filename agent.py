import os
from anthropic import Anthropic


def main():
	client = Anthropic(api_key = os.environ["ANTHROPIC_API_KEY"])
	prompt = "Is ai agent the future answer yes on no?"

	resp = client.messages.create(
		model = "claude-sonnet-4-6",
		max_tokens = 100,
		messages = [
			{"role": "user", "content": prompt}
		]
	)

	print(resp.content[0].text)

main()