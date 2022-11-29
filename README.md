# Maths2svg

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Marty42780/Maths2SVG/docker_build?logo=Github)

## Graphs

- [Circular graphs](Maths2SVG/README.md)

-----------------

# Installation

### Installing Python venv

- Make sure `pip` is installed and up-to-date
- Clone the repo and execute: 
```bash
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Launching Flask (for development)

- Execute: 
```bash
flask --debug run
```
- Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Launching Gunicorn (for production)

- Execute:
```bash
gunicorn app:app -w 2 --threads 3 
```
- Go to [http://127.0.0.1:5000](http://127.0.0.1:8000)

# Credits

Founders of this project : [CameliaMallus](https://github.com/CameliaMallus) and [Marty42780](https://github.com/Marty42780).

-----------------

2022
