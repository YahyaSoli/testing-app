from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Render the HTML file as a template
    return render_template('index.html')  # assuming your HTML file is named index.html and is in the templates directory

@app.route('/submit', methods=['POST'])
def submit():
    # Get the room number from the form data
    room_number = request.form['room-number']
    
    # Now you can use the room_number variable as needed
    print(room_number)  # Just for demonstration, you might want to do something else with it

    # Redirect or respond with a success message, or handle the data as needed
    return "Room number received: " + room_number

if __name__ == '__main__':
    app.run(debug=True)
