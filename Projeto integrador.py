from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta' 

# Usuário de exemplo
usuarios = {
    'usuario': 'senha'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in usuarios and usuarios[username] == password:
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        flash('Usuário ou senha inválidos!')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('index'))
    
    return f'Bem-vindo, {session["username"]}! <a href="/logout">Sair</a>'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
