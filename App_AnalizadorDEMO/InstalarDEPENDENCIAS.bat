@echo off
title Instalador - Analizador de LODOyPECES (DEMO)-ETI Patagonia (Python 3.10)
color 0A

echo ===============================================
echo  Analizador de LODOyPECES (DEMO)-ETI Patagonia
echo  Instalador Python 3.10
echo ===============================================
echo.

:: Buscar Python 3.10
py -3.10 --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo ❌ Python 3.10 NO encontrado.
    echo 👉 Instalar desde https://www.python.org/downloads/release/python-310/
    pause
    exit /b
)

echo ✔ Python 3.10 detectado
echo.

:: Crear entorno virtual
IF NOT EXIST venv (
    echo 📦 Creando entorno virtual (Python 3.10)...
    py -3.10 -m venv venv
) ELSE (
    echo ✔ Entorno virtual ya existe
)

echo.

:: Activar entorno virtual
call venv\Scripts\activate

echo ✔ Entorno virtual activado
echo.

:: Actualizar pip
echo 🔄 Actualizando pip...
python -m pip install --upgrade pip

echo.

:: Instalar dependencias
echo 📥 Instalando dependencias...
pip install opencv-python numpy pandas ultralytics

echo.
echo ===============================================
echo ✅ INSTALACION COMPLETADA CORRECTAMENTE
echo ===============================================
echo.
echo Para ejecutar la aplicacion:
echo.
echo   venv\Scripts\activate
echo   python main.py
echo.
pause
