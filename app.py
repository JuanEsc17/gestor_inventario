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

@app.route('/eliminar/', methods=['POST'])
def eliminar():
    # Carga los productos actuales
    productos = cargar_datos()
    # Obtiene el ID del producto a eliminar
    id_producto = int(request.form['id'])
    # Filtra el DataFrame para eliminar el producto
    productos = productos[productos['id'] != id_producto]
    # Guarda los datos actualizados
    guardar_datos(productos)
    # Redirige a la página principal
    return redirect('/')

@app.route('/buscar', methods=['GET'])
def buscar():
    # Carga los productos actuales
    productos = cargar_datos()
    # Obtiene el término de búsqueda del formulario
    termino = request.args.get('termino', '').lower()
    # Filtra los productos que coinciden con el término de búsqueda
    resultados = productos[productos['nombre'].str.lower().str.contains(termino)]
    return render_template('index.html', productos=resultados)

@app.route('/filtrar', methods=['GET'])
def filtrar():
    # Carga los productos actuales
    productos = cargar_datos()
    # Obtiene la categoría del formulario
    categoria = request.args.get('categoria', '')
    # Filtra los productos por categoría
    if categoria:
        resultados = productos[productos['categoria'] == categoria]
    else:
        resultados = productos
    return render_template('index.html', productos=resultados)

@app.route('/editar', methods=['POST'])
def editar_post():
    productos = cargar_datos()
    id_producto = int(request.form['id'])
    # Busca el producto por ID
    idx = productos[productos['id'] == id_producto].index
    if not idx.empty:
        if request.form['nombre']:
            productos.at[idx[0], 'nombre'] = request.form['nombre']
        if request.form['categoria']:
            productos.at[idx[0], 'categoria'] = request.form['categoria']
        if request.form['stock']:
            productos.at[idx[0], 'stock'] = int(request.form['stock'])
        if request.form['precio']:
            productos.at[idx[0], 'precio'] = float(request.form['precio'])
        guardar_datos(productos)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
