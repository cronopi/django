#!/bin/bash

if command -v pip &> /dev/null; then
	echo "pip está instalado."
else
	echo "pip no está instalado. Instalando..."
	apt-get install python3-pip
	exit 1
fi

echo "Versión de pip:"
pip --version

if  [ -d "../local_lib" ]; then
	echo "El directorio ../local_lib ya existe."
	rm -rf ../local_lib
fi

echo "El directorio ../local_lib no existe. Creándolo..."
mkdir ../local_lib

pip install --target ../local_lib git+https://github.com/jaraco/path.git > ../install.log 2>&1

if [ $? -eq 0 ]; then
	echo "La instalación se completó con éxito."
	PYTHONPATH=../local_lib python3 my_program.py
else
	echo "Hubo un error durante la instalación. Revisa ../install.log para más detalles."
fi
