from calendar import c
from cmath import pi
from doctest import OutputChecker
from flask import Flask, request
import csv
import json

app = Flask(__name__)

# Arracan en localhost:5000,  se lo puede borrar
@app.route('/')
def index():
    return 'Hello, World!'

# Punto 14 del pdf del proyecto
@app.route('/lista_estudiantes')
def lectura_de_estudiantes():
    with open('../datos/estudiante.csv') as archivo:
        lectura = csv.reader(archivo)
        next(lectura)
        estudiante_lista = []
        for fila in lectura:
            estudiante_lista.append(
                {'cedula': fila[0],
                'primer_apellido': fila[1],
                'segundo_apellido': fila[2],
                'primer_nombre': fila[3],
                'segundo_nombre': fila[4]
                })
    return json.dumps(sorted(estudiante_lista, key=lambda c: c['primer_nombre']  + c['primer_apellido'] ))

# Punto 15 
@app.route('/registro_asistencia', methods=['POST'])
def creacion_de_asistencia():
    with open('../datos/asistencia.csv', 'a' , newline='') as archivo:
        escritor = csv.writer(archivo,delimiter=',')
        escritor.writerow([
            request.json['cedula'],
            request.json['materia'],
            request.json['fecha_año'],
            request.json['fecha_mes'],
            request.json['fecha_dia']])
    return 'Asistencia registrada con exito' + request.json['cedula']

# Punto 26 
@app.route('/login/<cedula>/<primer_nombre>')
def login(cedula,primer_nombre):
    with open('../datos/estudiante.csv') as archivo:
        lectura = csv.reader(archivo)
        next(lectura)
        estudiante_lista = []
        for fila in lectura:
            if fila[0] == cedula and fila[3] == primer_nombre:
                estudiante_lista.append(
                {'cedula': fila[0],
                'primer_apellido': fila[1],
                'segundo_apellido': fila[2],
                'primer_nombre': fila[3],
                'segundo_nombre': fila[4]
                })
    return 'correcto'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
