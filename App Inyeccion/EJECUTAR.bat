@echo off
title Lanzador Calculadora Nanoburbujas
echo Actualizando librerias necesarias...
pip install streamlit pandas numpy

echo.
echo Iniciando Servidor Local...
streamlit run calculo_INYECCION.py
pause