import os
import json
from openai import OpenAI
from tqdm import tqdm
import time

client = OpenAI()

def build_system_prompt():
    return "You are a helpful assistant."

def build_user_prompt(data):
    return f"""
    <insert prompt here>
    """


def process_file(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        lines = f_in.readlines()

        for line in tqdm(lines, desc="Processing"):
            data = json.loads(line)
            prompt = build_user_prompt(data)

            max_retries = 5
            retry_wait = 60

            for attempt in range(max_retries):
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": build_system_prompt()},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0
                    )

                    rewritten_json = response.choices[0].message.content.strip()

                    if rewritten_json.startswith("```"):
                        rewritten_json = "\n".join(rewritten_json.splitlines()[1:-1]).strip()

                    try:
                        rewritten_data = json.loads(rewritten_json)
                        rewritten_data["example_id"] = data["example_id"]
                        f_out.write(json.dumps(rewritten_data) + "\n")
                        f_out.flush()
                    except json.JSONDecodeError:
                        print(f"[Warning] Could not decode JSON for example_id {data.get('example_id')}. Output was:\n{rewritten_json[:200]}")

                    break

                except Exception as e:
                    error_str = str(e)
                    if "rate_limit_exceeded" in error_str or "Rate limit" in error_str:
                        wait_time = retry_wait

                        import re
                        match = re.search(r'Please try again in (\d+(\.\d+)?)s', error_str)
                        if match:
                            wait_time = float(match.group(1)) + 5

                        print(f"[Rate Limit] Waiting {wait_time}s before retrying for example_id {data.get('example_id')} (attempt {attempt + 1}/{max_retries})")
                        time.sleep(wait_time)
                    else:
                        print(f"[Error] on example_id {data.get('example_id', 'unknown')}: {e}")
                        break


if __name__ == "__main__":
    input_filepath = ''
    output_filepath = ''
    process_file(
        input_filepath,
        output_filepath
    )
