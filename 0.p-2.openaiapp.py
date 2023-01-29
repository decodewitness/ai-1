import openai

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

openai.api_key = open_file('apikey.txt')


def gpt3_completion(prompt, engine='text-davinci-003', temp=0.7, top_p=1.0, tokens=1600, freq_pen=0.0, pres_pen=0.0, stop=['<<END>>']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    try:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=temp,
            max_tokens=tokens,
            top_p=top_p,
            frequency_penalty=freq_pen,
            presence_penalty=pres_pen,
            stop=stop)
    finally:
        text = response['choices'][0]['text'].strip()
        return text


def handlePrompt():
    question = input("\nPrompt: ")
    rephrased = "rephrase: \"" + question + "\""
    prompt = gpt3_completion(rephrased)
    print("\n+ Response:\n")
    response = gpt3_completion(prompt)
    print(response)


if __name__ == '__main__':
    while True:
        handlePrompt()