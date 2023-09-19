# netTime API Client - \*Development Phase
Python API client for netTime (SPEC, SA).

- Repository: [https://github.com/lucaslucyk/nettime-py](https://github.com/lucaslucyk/nettime-py)
- Documentation: Coming soon.


## Project Status
:warning: **Warning**: This project is currently in development phase.


## Why use `nettime-py`?
- :zap: __Fast to code__: Increase the speed to develop integrations features.
- :x: __Fewer bugs__: Reduce human (developer) induced errors.
- :bulb: __Intuitive__: Great editor support. Completion everywhere. Less time debugging.
- :nerd_face: __Easy__: Designed to be easy to use and learn. Less time reading docs.
- :part_alternation_mark: __Short__: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.


## Install on editable mode with Pipenv
```bash
...$ git clone git@github.com:lucaslucyk/nettime-py.git
...$ cd nettime-py/
.../nettime-py$ mkdir .venv
.../nettime-py$ pipenv install && pipenv install -d
.../nettime-py$ source .venv/bin/activate
(nettime-py) ./nettime-py/$ pip install -e .
```


## Quickstart

```python
from nettime_py import NetTimeAPI

# Initialize the client with the URL, username, and password
with NetTimeAPI(url='<HOST>', username='<USERNAME>', password='<PASSWORD>') as client:
    
    # Get and iter paginator
    employees = list(client.employees.all())

print(employees)
```


## License
This project is licensed under the terms of the GNU GPLv3 license.