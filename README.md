# API de Gestión de Clientes, Facturas y Transacciones

Sistema backend desarrollado con FastAPI y SQLModel para la gestión de clientes, facturas y transacciones financieras mediante una arquitectura modular y relaciones entre entidades.

---

## Tecnologías utilizadas

- Python
- FastAPI
- SQLModel
- Uvicorn
- Pydantic

---

## Arquitectura del sistema

Cliente (1)
   │
   ▼
Factura (N) ─── valor_total (propiedad calculada)
   │
   ▼
Transacción (N)

---

## Estructura del proyecto

```txt
app/
│
├── enrutador/
│   ├── clientes.py
│   ├── facturas.py
│   └── transacciones.py
│
├── modelos/
│   ├── clientes.py
│   ├── facturas.py
│   └── transacciones.py
│
├── conexion_bd.py
├── main.py
│
base_datos.db
requirements.txt
README.md