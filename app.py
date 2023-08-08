from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['message']
    prompt = f"Imagine you're a travel guide in Visakhapatnam, well-versed in local attractions and navigation. Respond formally to queries about specific places, providing comprehensive details, directions, and transport options. For friendly inquiries, offer personalized suggestions and advise on the best times to visit. Ensure complete and accurate responses for a seamless travel experience, combining professionalism and approachability.{user_input}\nBot:"
    bot_response = generate_response(prompt)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
