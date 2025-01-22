from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/authorization', methods=['POST', 'GET'])
def form_authorizations():
    if request.method == 'POST':
        Login = request.form.get('Login')
        Password = request.form.get('Password')

        db_lp = sqlite3.connect('login_password.db')
        cursor_db = db_lp.cursor()
        cursor_db.execute(('''
                           SELECT password FROM passwords 
                           WHERE login = '{}';
        ''').format(Login))

        pas = cursor_db.fetchall()
        cursor_db.close()

        try:
            if pas[0][0] != Password:
                return render_template('auth_bad.html')
        except:
            return render_template('auth_bad.html')

        db_lp.close()
        return render_template('successfulauth.html')

    return render_template('authorization.html')

@app.route('/registration', methods=['POST', 'GET'])
def form_registration():
    if request.method == 'POST':
        Login = request.form.get('Login')
        Password = request.form.get('Password')

        db_lp = sqlite3.connect('login_password.db')
        cursor_db = db_lp.cursor()
        cursor_db.execute(('''
                           INSERT INTO passwords 
                           VALUES ('{}', '{}');
        ''').format(Login, Password))

        db_lp.commit()
        cursor_db.close()
        db_lp.close()

        return render_template('successfulregis.html')

    return render_template('registration.html')


if __name__ == '__main__':
    app.run()
