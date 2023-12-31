# AEMPSconn
Library designed for interacting with the CIMA REST API ([AEMPS](https://cima.aemps.es/cima/publico/home.html)).  
More information related to the official REST API can be found [here](https://cima.aemps.es/cima/resources/docs/CIMA_REST_API.pdf).  

*Note: AEMPSconn is developed to make use of it with [CIMA REST API v1.23](https://cima.aemps.es/cima/resources/docs/CIMA_REST_API.pdf).*

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install aempsconn.

```bash
pip install aempsconn
```

## Custom Logger
The use of the `logger` in the library **is not mandatory**.  

A *custom logger* has been created in order to offer the possibility to use it in an integrated way with the library and it allows you to set the logging level. 

However, as the `logger` argument requires a Logger type, it is fully customizable so that the programmer can set it according to his own preferences.  

**To not use any logger, simply leave it blank.**

## Building queries
It has developed a easy-use query builder for the most important endpoints: `/medicamento` & `/medicamentos`.  
Each endpoint has its own custom filters so you can find and add them to the request by:

```python
import aempsconn

aemps = aempsconn.Orchestrate(logger=aempsconn.CustomLogger(level=50))

filter_med  = aemps.filter_medicamento.<FILTER_CONDITION_MED>.equals(value=<VALUE>)
filter_meds = aemps.filter_medicamentos.<FILTER_CONDITION_MEDS>.equals(value=<VALUE>)
```

This query builder supports as many conditions/filters as you want.  
Be noted that the the first endpoint (`/medicamento`) **will only make use of the last condition set**, since it only admits a single condition.

## Handling errors  
The library comes with custom exceptions for error handling.  
This exceptions are the following:

- _aempsconn.errors.HTTPFailure_  
Custom exception related to the HTTP requests.

- _aempsconn.errors.JSONDecodeFailure_  
Custom exception related to JSON decode.

- _aempsconn.errors.JSONKeyFailure_  
Custom exception related to JSON dict's keys.

- _aempsconn.errors.ProxyFailure_  
Custom exception related to the proxy configuration.

- _aempsconn.errors.RequestFailure_  
Custom exception related to the Python3 request module.

- _aempsconn.errors.TimeoutFailure_  
Custom exception related to the timeout.

- _aempsconn.errors.UnhandledError_  
Custom exception related to unhandled exceptions.

## Usage
```python
import aempsconn

# Initialize all the modules with the same configuration.
aemps = aempsconn.Orchestrate(logger=aempsconn.CustomLogger(level=50))
# or initialize all the modules without the Logger or any other custom settings
aemps = aempsconn.Orchestrate()

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

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.  

Please make sure to update tests as appropriate.


## Disclaimer

The use of Spanish words or descriptions **is intended** to facilitate consistency between the official CIMA API and this library, so that the programmer does not hesitate with the name of each of the filters or data received.

This library is not official.
