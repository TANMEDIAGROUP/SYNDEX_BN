# SYNDEX BACKEND

syndex-bn is a Django REST project that provides APIs for users, news articles, and utilizes machine learning models to ingest data and interact with users.

## Stack

- [django-rest-framework](https://www.django-rest-framework.org)

## Features

- User management APIs
- News article APIs
- Machine learning models functionality

## Getting Started

### 1. Clone the repository:

```bash
git clone https://github.com/TANMEDIAGROUP/S-BN.git
```

### 2. Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```
### 3. Install the required dependencies:
```bash
pip3 install -r requirements.txt
```
### 4. Run the server:
```bash
python3 server.py runserver
```
### 5. Run migrations:
```bash
python3 server.py makemigrations api
```
```bash
python3 server.py migrate api
```
## Project Structure
```tree
root/
├── ML/
├── README.md
├── api/
│   ├── config.py
│   ├── middleware/
│   ├── models/
│   ├── src/
│   │   ├── endpoints.py
│   │   ├── middleware/
│   │   ├── routes/
│   │   └── tests.py
│   ├── urls.py
│   └── wsgi.py
│   └── config.py
├── requirements.txt
├── example.env
├── .gitignore
├── .env
└── server.py
```

## Contributors

If you'd like to contribute to SYNDEX_BN, please follow our [Contribution Guidelines](CONTRIBUTING.md).
A big thank you to all our contributors:

- [@kevin Ishimwe](https://github.com/Kevin-ishimwe/)

If you find any issues or have suggestions for improvement, please feel free to open an [issue](https://github.com/TANMEDIAGROUP/brandz-project/issues) or submit a [pull request](https://github.com/TANMEDIAGROUP/brandz-project/pulls).l request.

Thank you for helping make SYNDEX better!
