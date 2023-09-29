# aempsconn

Library designed for interacting with the AEMPS API.

## Examples
```python
import aempsconn

aemps = aempsconn.Orchestrate(logger=aempsconn.logger(level=50))

aemps.medicamento.add_condition(key="nregistro", value="59494")
medicamento = aemps.medicamento.get()

if medicamento is not None:
    print(medicamento.nombre.title())
    
else:
    print("No existen medicamentos que cumplan con esas condiciones.")
```

```python
import aempsconn

aemps = aempsconn.Orchestrate(logger=aempsconn.logger(level=50))

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

else:
    print("No existen medicamentos que cumplan con esas condiciones.")
```