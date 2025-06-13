from flask import Flask, render_template, request, redirect
from utils.manejo_datos import cargar_datos, guardar_datos

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define las rutas de la aplicación
@app.route('/')
def index():
    productos = cargar_datos()
    return render_template('index.html', productos=productos)

# Ruta para agregar un producto
@app.route('/agregar', methods=['POST'])
def agregar():
    # Carga los productos actuales
    productos = cargar_datos()
    # Crea un nuevo producto con los datos del formulario
    nuevo = {
        "id": productos["id"].max() + 1 if not productos.empty else 1,
        "nombre": request.form['nombre'],
        "categoria": request.form['categoria'],
        "stock": int(request.form['stock']),
        "precio": float(request.form['precio'])
    }
    # Agrega el nuevo producto a la lista y guarda los datos
    productos = productos._append(nuevo, ignore_index=True)
    guardar_datos(productos)
    # Redirige a la página principal
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
