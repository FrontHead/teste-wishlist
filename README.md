# Project Desafio Wishlist

API for a wishlist and a CRUD operations for a client database using django framework with djongo. 


It will load two pages. One for the products to be added and another for the clients CRUD operations. 

## Installation

- Download the project by using 'git clone' or just download it. 


## Dependences

Python 3.0 must be installed.

```bash
python -m pip install –upgrade pip
pip install django==3.0
```

## Usage
- start the virtual environamnet with a command in the project path using a terminal
    PowerShell: start\Scripts\Activate.ps1
    cmd.exe: start\Scripts\activate.bat
    git bash and linux: source start/Script/activate

- In teste-wishlist, using terminal still, type the following:
    python manage.py runserver

- Open the browser and paste the localhost urls (the <page_number> should be a number)
    Client list: http://localhost:8000/client-list
    Products view: http://localhost:8000/produtos/<page_numer>



## License
None at the moment
