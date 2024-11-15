from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/auth/discord/callback')
def discord_callback():
    # Handle the OAuth2 callback here
    # You can extract the authorization code from the request parameters
    code = request.args.get('code')

    # Process the code to exchange it for an access token
    # ...

    # Redirect the user to a success page or handle the token as needed
    return redirect('https://example.com/success')  # Replace with your desired redirect URL

if __name__ == '__main__':
    app.run(debug=True)
