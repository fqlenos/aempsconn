import aempsconn

aemps = aempsconn.Orchestrate(logger=aempsconn.logger(level=50))

"""
Ejemplo 1:
- Estableces condiciones para obtener 1 solo medicamento con:
    - aemps.medicamento.add_condition()
    - * puedes llamar a esta función tantas veces como condiciones quieras añadir
- Llamas a la función que realiza la petición:
    - aemps.medicamento.get()

El resultado ya es de tipo Medicamento.
"""
aemps.medicamento.add_condition(key="nregistro", value="59494")
medicamento = aemps.medicamento.get()
print(medicamento.nombre)

"""
Ejemplo 2:
- Estableces condiciones para obtener n medicamentos con:
    - aemps.medicamentos.add_condition()
    - * puedes llamar a esta función tantas veces como condiciones quieras añadir
- Llamas a la función que realiza la petición:
    - aemps.medicamentos.get()

El resultado ya es de tipo Medicamento.
"""
aemps.medicamentos.add_condition(key="nombre", value="paraceta*")
aemps.medicamentos.add_condition(key="comerc", value=1)
aemps.medicamentos.add_condition(key="laboratorio", value="cinfa")
medicamentos = aemps.medicamentos.get()
if medicamentos is not None:
    for med in medicamentos:
        print(f"[*] {med.nombre.title()}")
        print(f"\t- {med.labtitular.title()}")
        for via in med.viasAdministracion:
            print(f"\t- {via.nombre.title()}")
