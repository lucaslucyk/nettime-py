# netTime API Client - \*Development Phase
Python API client for netTime (SPEC, SA).

- Repository: [https://github.com/lucaslucyk/nettime-py](https://github.com/lucaslucyk/nettime-py)
- PyPi: [https://pypi.org/project/nettime-py](https://pypi.org/project/nettime-py)
- Documentation: Coming soon.


## Project Status
:warning: **Warning**: This project is currently in development phase.

This project is in an early stage of development and may contain bugs. It is not recommended for use in production environments.


## Why use `nettime-py`?
- 🚀 __Fast to code__: Increase the speed to develop integrations features.
- ❌ __Fewer bugs__: Reduce human (developer) induced errors.
- 💡 __Intuitive__: Great editor support. Completion everywhere. Less time debugging.
- 🤓 __Easy__: Designed to be easy to use and learn. Less time reading docs.
- 〽️  __Short__: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.


## Install
```bash
$  pip install nettime-py
```


## Install to dev
```bash
$ git clone git@github.com:lucaslucyk/nettime-py.git
$ cd nettime-py/
/nettime-py$ mkdir .venv
/nettime-py$ pipenv install && pipenv install -d
/nettime-py$ source .venv/bin/activate
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

## Contributions and Feedback
I would love to receive contributions and feedback! If you'd like to get involved, please contact me through one of the contact methods in my [Profile](https://github.com/lucaslucyk).

## License
This project is licensed under the terms of the GNU GPLv3 license.