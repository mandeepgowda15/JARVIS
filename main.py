from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True)
    intent = data['queryResult']['intent']['displayName']
    course_name = data['queryResult']['parameters']['course_name']
    course_name = course_name.upper()
    if intent == 'course_selection':
        # Your logic for course selection
        if course_name == 'DATA SCIENCE':
            response = {
                'fulfillmentText': 'Data science has been registered as your course you"ll be notified soon',
            }
        elif course_name == 'MACHINE LEARNING':
            response = {
                'fulfillmentText':'Machine Learning has been registered as your course you"ll be notified soon',
            }
        elif course_name == 'ENTREPRENEURSHIP':
            response = {
                'fulfillmentText': 'Entrepreneurship has been registered as your course you"ll be notified soon',
            }
        elif course_name == 'CYBER SECURITY':
            response = {
                'fulfillmentText': 'Cyber Security has been registered as your course you"ll be notified soon',
            }

        elif course_name == 'CLOUD COMPUTING':
            response = {
                'fulfillmentText': 'Cloud Computing has been registered as your course you"ll be notified soon',
            }

    else:
        # Handle other intents
        response = {
            'fulfillmentText': 'I\'m sorry, I didn\'t understand that.',
        }

    return jsonify(response)

@app.route('/')
def index():
    return 'Hello, this is the root page!'

if __name__ == '__main__':
    app.run(port=3000)


