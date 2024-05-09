function guardarDatos() {
    let nombres = document.getElementById("nombre");
    let apellidos = document.getElementById("apellido");
    

    axios
    .post(
        '/fronted/guardar', //NOMBRE DEL 'API' "BANCKEND PYTHON" 
    {
        nombre: nombres.value,
        apellido: apellidos.value,
    },)
    .then((res) => {
        console.log(res.data)

        if (res.data == "usuario existente"){
            alert("usuario ya existe")
    
        }else{
            alert("dato guardado")
        }
           
      
        
    })
    .catch((error) => {
        console.error(error);
    });
  }
