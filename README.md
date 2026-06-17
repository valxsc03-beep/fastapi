# Proyecto FastAPI - Gestión de Clientes, Facturas y Transacciones

## Información del estudiante

* **Nombre:** Valeria Sandoval
* **Número de ficha:** 3407184

---

# Estructura del proyecto

```txt
proyecto_clientes/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── cliente.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   └── routers/
│       ├── __init__.py
│       ├── cliente.py
│       ├── facturas.py
│       └── transacciones.py
│
├── venv/
├── requirements.txt
└── README.md
```

---

# Descripción del proyecto

Este proyecto fue desarrollado con FastAPI utilizando Python.

El sistema permite gestionar clientes, facturas y transacciones mediante endpoints CRUD.

El proyecto implementa:

* Creación de clientes
* Listado de clientes
* Edición de clientes
* Eliminación de clientes
* Gestión de facturas
* Gestión de transacciones
* Organización modular del proyecto
* Uso de modelos Pydantic y SQLModel
* Uso de routers
* Uso de entorno virtual

---

# Modelos implementados

## Cliente

Contiene:

* id
* nombre
* edad
* descripcion

## Factura

Contiene:

* id
* fecha
* cliente

Incluye un método para calcular el valor total de la factura.

## Transacción

Contiene:

* id
* valor_unitario
* cantidad
* factura_id

---

# Endpoints implementados

## Clientes

* GET /clientes
* POST /clientes
* GET /cliente/{cliente_id}
* PUT /cliente/{cliente_id}
* DELETE /cliente/{cliente_id}

## Facturas

* GET /facturas
* POST /facturas
* GET /factura/{factura_id}
* PUT /factura/{factura_id}
* DELETE /factura/{factura_id}

## Transacciones

* GET /transacciones
* POST /transacciones
* GET /transaccion/{transaccion_id}
* PUT /transaccion/{transaccion_id}
* DELETE /transaccion/{transaccion_id}

---

# Historial de desarrollo

Durante el desarrollo del proyecto se realizaron las siguientes actividades:

* Creación de la estructura modular del proyecto.
* Configuración del entorno virtual.
* Instalación de FastAPI, Uvicorn y SQLModel.
* Creación de modelos utilizando Pydantic y SQLModel.
* Implementación de endpoints CRUD para clientes, facturas y transacciones.
* Organización de routers para cada módulo del sistema.
* Configuración y ejecución del servidor local con Uvicorn.
* Pruebas funcionales mediante Swagger UI.
* Corrección de errores de imports y estructura del proyecto.

---

# Instalación del proyecto

## 1. Clonar el repositorio

```bash
git clone LINK_DEL_REPOSITORIO
```

---

## 2. Entrar al proyecto

```bash
cd proyecto_clientes
```

---

## 3. Crear entorno virtual

### Windows

```bash
python -m venv venv
```

---

# Activar entorno virtual

## Windows CMD

```bash
venv\Scripts\activate.bat
```

## Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

## Linux

```bash
source venv/bin/activate
```

---

# Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecutar el proyecto

```bash
python -m uvicorn app.main:app --reload
```

---

# Acceso al proyecto

## API principal

```txt
http://127.0.0.1:8000
```

## Documentación Swagger

```txt
http://127.0.0.1:8000/docs
```

---

# Tecnologías utilizadas

* Python
* FastAPI
* Uvicorn
* Pydantic
* SQLModel

---

# Archivo requirements.txt

```txt
fastapi
uvicorn
pydantic
sqlmodel
```
