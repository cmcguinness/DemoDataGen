from openai import OpenAI
from datetime import datetime as dt
import time
import os

# The choice of model will change over time as OpenAI releases new one.  Here are
# some that are current at the time this code was written:
#
# gpt-4-0125-preview    - the latest and greatest, albeit in beta at this moment
# gpt-3.5-turbo-0125    - most recent version of GPT-3.5, doesn't do a great job
#
def generate_csv(sys_prompt: str, user_prompt: str, rows=10, model="gpt-4-0125-preview"):

    openai = OpenAI()

    sys_prompt = sys_prompt + f'You will generate {rows} rows of sample data.\n'

    start = time.time()

    completion = openai.chat.completions.create(
      model=model,
      messages=[
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
      ]
    )

    print(f'Call to OpenAI took {int(time.time()-start)} seconds')
    print(f'Usage: Prompt Tokens={completion.usage.prompt_tokens}, Output Tokens={completion.usage.completion_tokens}')

    results = completion.choices[0].message.content
    lines = results.split('\n')
    in_csv = False

    data = ''

    for l in lines:
        if l == '```csv':
            in_csv = True
            continue
        if l == '```':
            in_csv = False
            continue
        if in_csv:
            data = data + l + '\n'

    if not os.path.isdir('outputs'):
        os.mkdir('outputs')

    tstamp = dt.now().strftime("%Y-%m-%d-%H-%M-%S")

    with open(f'outputs/{tstamp}.csv', 'w') as f:
        f.write(data)

    return f'outputs/{tstamp}.csv'


if __name__ == "__main__":
    with open('sys_prompt.txt', 'r') as f:
        sys_prompt = f.read()

    with open('user_prompt.txt', 'r') as f:
        user_prompt = f.read()

    generate_csv(sys_prompt, user_prompt, rows=10)