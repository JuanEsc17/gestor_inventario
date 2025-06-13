# 📦 Inventario Simple para Emprendedores

Aplicación web creada con **Flask**, que permite gestionar un inventario básico: cargar productos, visualizar una tabla de stock y precios, y mantener los datos guardados en un archivo CSV.

Está pensada para pequeños emprendimientos que necesiten una herramienta simple y rápida para llevar control de sus productos.

---

## 🖥️ Tecnologías utilizadas

- **Python** (Flask, pandas)
- **HTML + Bootstrap 5** (interfaz responsive)
- **CSV** como almacenamiento de datos local

---

## ✨ Funcionalidades

- 📋 Visualización de productos en una tabla
- ➕ Formulario para agregar productos
- 🗃️ Guardado persistente en archivo CSV
- ⚡ Interfaz web simple y rápida

---

## 📂 Estructura del proyecto

```bash
gestor-inventario/
├── app.py # Lógica principal de la app
├── data/
│ └── inventario.csv # Archivo de productos
├── utils/
│ └── manejo_datos.py # Funciones para cargar y guardar CSV
├── templates/
│ ├── layout.html # Plantilla base con Bootstrap
│ └── index.html # Página principal
├── static/
│ └── style.css # Estilos personalizados (opcional)
├── requirements.txt # Dependencias del proyecto
└── README.md
```

---

## 🚀 Cómo ejecutar el proyecto

1. Cloná este repositorio:

```bash
git clone https://github.com/JuanEsc17/inventario-flask.git
cd gestor-inventario
```

2. Instalá las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
python app.py
```

4. Abre el navegador en donde indique la consola.