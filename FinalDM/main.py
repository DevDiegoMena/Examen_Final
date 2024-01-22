from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET'])
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/calcular_descuento', methods=['POST'])
def calcular_descuento():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    tarros = int(request.form['tarros'])

    precio_tarro = 9000
    total_sin_descuento = tarros * precio_tarro

    if 18 <= edad <= 30:
        descuento = 0.15
    elif edad > 30:
        descuento = 0.25
    else:
        descuento = 0

    total_con_descuento = total_sin_descuento * (1 - descuento)

    return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                           total_con_descuento=total_con_descuento, descuento=total_sin_descuento * descuento)

@app.route('/ejercicio2', methods=['GET'])
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/verificar_usuario', methods=['POST'])
def verificar_usuario():
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']

    if usuario == 'juan' and contrasena == 'admin':
        mensaje = 'Bienvenido administrador juan'
    elif usuario == 'pepe' and contrasena == 'user':
        mensaje = 'Bienvenido usuario pepe'
    else:
        mensaje = 'Usuario y/o contraseña incorrecta'

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
