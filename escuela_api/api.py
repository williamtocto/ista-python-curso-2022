
from flask import Flask, jsonify
from flask import request
from hashlib import new
import json
from operator import itemgetter


app = Flask(__name__)


def leerArchivo():
    ruta_archivo = '../datos/estudiante.csv'
    with open(ruta_archivo, 'r') as a:
        next(a, None)
        archivo = a.readlines()
    return archivo


listado_estudiantes = []


@app.route('/lista_estudiantes')
def listar():
    listado = {}
    contenido = leerArchivo()
    for linea in contenido:
        linea = linea.rstrip()
        listado_estudiantes.append(linea.split(","))
    listado_estudiantes.sort(key=itemgetter(1))
    return jsonify({"estudiantes": listado_estudiantes})


@app.route('/registro_asistencia', methods=['POST'])
def agregar_asistencia():
    new_registro = {

    "cedula": json.request.get['cedula'],
    "materia": json.request.get['materia'],
    "fecha_año": json.request.get['fecha_año'],
    "fecha_mes": json.request.get['fecha_mes'],
    "fecha_dia": json.request.get['fecha_dia']
    }
    print(new_registro)

    return 'received'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
