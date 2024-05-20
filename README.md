# AEMPSconn
Library designed for interacting with the CIMA REST API ([AEMPS](https://cima.aemps.es/cima/publico/home.html)).
More information related to the official REST API can be found [here](https://cima.aemps.es/cima/resources/docs/CIMA_REST_API.pdf).

*Note: AEMPSconn is developed to make use of it with [CIMA REST API v1.23](https://cima.aemps.es/cima/resources/docs/CIMA_REST_API.pdf).*


## Testing
**Unit-tests for this new version are under development.**


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install aempsconn.

```bash
pip install aempsconn
```

## Usage
Each module has embedded in it the only type of filter it supports.
The filters are created dynamically so depending on the type of data you want to obtain, it will ask for the type of value required for it.

If you want to filter by more than one value, simply concatenate all the desired filters, the query-builder will create the necessary query.

```python
from aempsconn.aemps import AempsConn
from aempsconn.filter import (
    MedicamentoFilter,
    MedicamentosFilter,
    PresentacionesFilter,
    VmppFilter,
)

aemps = AempsConn()

for med in aemps.medicamento.get(
    filter=MedicamentoFilter().nregistro.equals(value="62121")
):
    print(med.nombre)

for med in aemps.medicamentos.get(
    filter=MedicamentosFilter().nombre.startswith(value="meto")
):
    print(med.nombre)

for med in aemps.presentaciones.get(
    filter=PresentacionesFilter().vmp.equals("270671000140106")
):
    print(med.nombre)

for desc_cli in aemps.vmpp.get(filter=VmppFilter().nombre.contains("metotrexato")):
    print(desc_cli.vmpDesc)

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Disclaimer

The use of Spanish words or descriptions **is intended** to facilitate consistency between the official CIMA API and this library, so that the programmer does not hesitate with the name of each of the filters or data received.

This library is not official.
