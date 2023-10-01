# aempsconn

Library designed for interacting with the AEMPS API.

## Examples
```python
import aempsconn

# Initialize all the modules with the same configuration.
aemps = aempsconn.Orchestrate(logger=aempsconn.CustomLogger(level=50))

# Create a filter needed for the wanted request.
# This filter is custom for "/medicamento" endpoint.
filter1 = aemps.filter_medicamento.num_registro.equals("59494")
# Download the med that satisfies the previous custom filter.
med = aemps.medicamento.get(filter=filter1)

# If med is not null prints the name.
if med is not None:
    print(med.nombre)

# Create a new filter needed for the wanted request.
# This filter is custom for "/medicamentos" endpoint.
filter2 = (
    aemps.filter_medicamentos.nombre.equals("paraceta*")
    .comercializado.equals(True)
    .laboratorio.equals("cinfa")
    .receta.equals(True)
)
# Download all the meds that satisfy the previous custom filter.
meds = aemps.medicamentos.get(filter=filter2)

# If meds are not null iterates and prints the names.
if meds is not None:
    for med in meds:
        print(med.nombre)

```