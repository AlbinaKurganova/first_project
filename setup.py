from setuptools import setup, find_packages

setup(
    name="first-project",
    version="0.1.0",
    description="Проект для загрузки и обработки данных из Oracle",
    author="Albina Kurganova",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "sqlalchemy",
        "cx_Oracle",
        "oracledb",
        "python-dotenv",
    ],
    python_requires=">=3.8",
)
