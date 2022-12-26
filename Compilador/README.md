
## Crear iamgen (pagina)
```commandline
    docker build -t olc2back:latest .
```

## Ver imagenes creadas de docker
```commandline
    docker images
```

## Correr el contenedor
```commandline
    docker container run -dit -p 5000:5000 olc2back
```