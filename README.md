Proyecto Final Django – Blog con Usuarios y Mensajería

Descripción del proyecto

Este es mi proyecto final del curso de Python con Django.  
El objetivo fue crear una aplicación web estilo blog, con sistema de usuarios, perfiles, CRUD completo de páginas y una app de mensajería interna.  
El sitio tiene una estructura simple y moderna, con navegación clara y funciones pensadas para practicar lo aprendido durante el curso.

---

 Funcionalidades principales

 Home

Pantalla principal con acceso a todo el contenido.

👤 Usuarios
- Registro con username, email y contraseña  
- Login y Logout  
- Perfil del usuario  
- Edición del perfil  
- Cambio de contraseña  
- Perfil extendido con:
  - Avatar (imagen)
  - Biografía
  - Website
  - Fecha de nacimiento

Blog / Pages

- Listado de páginas en `/pages/`
- Mensaje de “No hay páginas aún” cuando la lista está vacía
- Detalle de página con “Leer más”
- Crear página (solo si está logueado)
- Editar y borrar página (solo el autor)
- Formulario con CKEditor para texto enriquecido
- Imagen por página

Mensajería interna entre usuarios

- Bandeja de entrada (mensajes recibidos)
- Sección de “Enviados”
- Crear nuevo mensaje
- Ver detalle del mensaje
- Marcar como leído
- Responder mensajes
- Eliminar mensajes

---

Tecnologías utilizadas

- Python 3  
- Django 5  
- SQLite3  
- CKEditor  
- HTML / CSS  
- Sistema de templates con herencia  
- Mensajes flash de Django  

---

Estructura del proyecto

```
tuprimera/
│── blog/             → App principal con posts/pages
│── users/            → Registro, perfiles, autenticación
│── messaging/        → Mensajería entre usuarios
│── templates/        → Base, home, about, etc.
│── media/            → Avatares e imágenes subidas
│── static/           → CSS global
│── manage.py
│── requirements.txt
│── README.md
```

---

Cómo ejecutar el proyecto

1. Clonar el repositorio:
   ```bash
   git clone <URL-del-repo>
   ```

2. Crear entorno virtual:
   ```bash
   python -m venv .venv
   ```

3. Activar entorno:

   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux / Mac:
     ```bash
     source .venv/bin/activate
     ```

4. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

5. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```

6. Ejecutar el servidor:
   ```bash
   python manage.py runserver
   ```

7. Abrir en el navegador:
   ```
   http://127.0.0.1:8000/
   ```

---

 Superusuario (para admin)

Para crear un superusuario:

```bash
python manage.py createsuperuser
```

Acceso al panel admin:

```
http://127.0.0.1:8000/admin/
```

---

 .gitignore utilizado

```
__pycache__/
db.sqlite3
media/
.venv/
```


 Estado final

El proyecto cumple con todos los requisitos de la consigna del curso:

- Blog funcional  
- CRUD usando CBVs, mixins y decoradores  
- Sistema de usuarios completo  
- Perfiles extendidos  
- Mensajería interna  
- Templates con herencia  
- Archivos estáticos y media configurados  
- About, Home, Pages  
- README y .gitignore incluidos  
