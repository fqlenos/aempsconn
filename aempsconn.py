import aempsconn

aemps = aempsconn.Orchestrate(logger=aempsconn.logger())
aemps.medicamentos.add_condition(key="nombre", value="ibu*")
for i in range(3):
    aemps.medicamentos.add_condition(key="pagina", value=str(i))
    aemps.medicamentos.get()
