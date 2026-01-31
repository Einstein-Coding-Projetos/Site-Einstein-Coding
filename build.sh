#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar as dependências
pip install -r requirements.txt

# Coletar arquivos estáticos (CSS, Imagens do sistema)
python manage.py collectstatic --no-input

# Aplicar migrações no banco de dados
python manage.py migrate