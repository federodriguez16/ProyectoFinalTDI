from flask import Flask, render_template, flash, request, redirect, url_for, send_file
import os
import shutil
from werkzeug.utils import secure_filename
from markupsafe import escape
from procesamiento import crop, scale, objectDetector


# Variables auxiliares

id = 1
extension = ''
ayuda = []
categoria = []
counts = 0

# Configuracion Flask

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'boca el mas grande de argentina'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Funciones Auxiliares


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Funciones Aplicacion

# Pagina Principal


@app.route("/")
def index():
    return render_template('index.html')

# Carga y procesamiento de imagenes


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.form)

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # En caso de que se haya introducido una imagen de manera correcta se guarda la imagen
        if file and allowed_file(file.filename):
            global id
            global extension
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Dejamos la imagen original y se trabaja con una copia
            ext = filename.split('.')
            extension = ext[1]
            nombre = f"{id}.{ext[1]}"
            shutil.copy(f"static/uploads/{filename}",
                        f"static/processing/{nombre}")
            id += 1

            global ayuda
            global categoria
            global counts
            counts = 0
            l = 1
            ayuda = []
            categoria = []
            lines = ["id,label,y_min,x_min,y_max,x_max\n"]
            # Opcion 1 -- crop
            if request.form['x'] != '':
                try:
                    crop(nombre, int(float(request.form['x'])), int(float(request.form['y'])), int(
                        float(request.form['ancho'])), int(float(request.form['alto'])))
                except:
                    print("Hubo un error con el crop")

            # Opcion 2 -- scale
            if request.form['scale'] != '':
                scale(nombre, int(float(request.form['scale'])))

            # Opcion 3 -- object detector
            if request.form['object-detector'] == '1':

                try:
                    predicciones = objectDetector(nombre)
                    print(predicciones)
                    for i in predicciones:
                        print(type(i))
                        ayuda.append(
                            f"class=cuadros style=position:absolute;top:{i['y_min']}px;left:{i['x_min']}px;width:{i['x_max']-i['x_min']}px;height:{i['y_max']-i['y_min']}px")
                        print(ayuda)
                        categoria.append(i['label'])
                        lines.append(
                            f"{l},{i['label']},{i['y_min']},{i['x_min']},{i['y_max']},{i['x_max']}\n")
                        l += 1
                    counts = len(ayuda)
                except:
                    print("error con el detector")

            # Movemos la imagen del sector de procesamiento para que el usuario pueda descargarla
            os.rename(f"static/processing/{nombre}",
                      f"static/downloads/{nombre}")
            print(ayuda)
            print(categoria)
            print(counts)

            try:
                os.remove(f"static/downloads/{id-1}-objetos.csv")
            except:
                print("no existe el archivo")

            f = open(f"static/downloads/{id-1}-objetos.csv", "a")
            f.writelines(lines)
            f.close()
            return redirect(url_for('descargar'))


# Pagina de descarga de imagen
@app.route('/descarga')
def descargar():
    return render_template('descarga.html', archivo=str(id-1), exten=extension, texto=ayuda, cat=categoria, counts=counts)

# Descarga de la imagen


@app.route('/download')
def download():
    path = f'static/downloads/{str(id-1)}.{extension}'
    return send_file(path, as_attachment=True)


@app.route('/download-metadata')
def downloadMetadata():
    path = f'static/downloads/{id-1}-objetos.csv'
    return send_file(path, as_attachment=True)

# Pagina de prueba


@app.route("/test")
def prueba():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
