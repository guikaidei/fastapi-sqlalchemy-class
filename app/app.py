from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import glob
from importlib import import_module

app = FastAPI(
    title="Documentação da API de livros e autores da Trilha da Insper Jr",
    description="Essa é uma API para gerenciar livros e autores, permitindo operações CRUD e o gerenciamento do relacionamento entre eles.",
    version="1.0.0",
    contact={
        "name": "Guilherme Kaidei",
        "url": "https://blablabla.com",
        "email": "guik@insperjr.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)


@app.get("/")
def test():
    return {"status": "OK v2 (3)"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


working_directory = os.path.dirname(os.path.abspath(__file__))
use_cases_directory = os.path.join(working_directory, "use_cases")
routes = glob.glob(os.path.join(use_cases_directory, "**/index.py"), recursive=True)

for route in routes:
    relative_path = os.path.relpath(route, working_directory)
    module_name = os.path.splitext(relative_path)[0].replace(os.path.sep, '.')

    try:
        print(f"Importing module: {module_name}")
        module = import_module(module_name)
        if hasattr(module, 'router'):
            app.include_router(module.router)
    except ModuleNotFoundError as e:
        print(f"Erro ao importar módulo {module_name}: {e}")

