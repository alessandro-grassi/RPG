var k=0;
var j=0;

function changeVisibility(){
  if(k == 0){
    document.getElementById("scegli").style.visibility = 'visible';
    document.getElementById("crea").style.visibility = "hidden";
    k=1;
  }else if(k == 1){
    document.getElementById("scegli").style.visibility = 'hidden';
    document.getElementById("crea").style.visibility = "visible";
    k=0;
  }
}

function crea_personaggio(){
    const name = document.getElementById("name");
    const classe = document.getElementById("classe");
    const ab1 = documentgetElementById("ab1");
    const ab2 = documentgetElementById("ab2");
    const ab3 = documentgetElementById("ab3");
}

function cambiaImmagine() {
    var selezione = document.getElementById("choice").value;
    var class_image = document.getElementById("class-image");
    var image_1 = "http://localhost:8080/personaggio/magoblu"
    var image_2 = "http://localhost:8080/personaggio/magorosso"
    var default_image = "https://cdn.pixabay.com/photo/2016/09/28/02/14/user-1699635_1280.png"

    if (selezione == "opzione1") {
        class_image.src = image_1;
    } else if (selezione == "opzione2") {
        class_image.src = image_2;
    } else {
        class_image.src = default_image;  // Non mostrare nulla altrimenti
    }
}


function listaClassi(){
  fetch('http://localhost:8080/personaggio/listaClassi')
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json(); // Decodifica la risposta JSON
    })
    .then(data => {
      // Mostra il messaggio nella pagina
      let classi = data;
      let select = document.getElementById("choice");

      classi.forEach((classe)=> {
        let option = document.createElement("option");
        option.textContent=classe;
        option.value=classe;
        select.appendChild(option);
        });
    })
    .catch(error => {
      console.error("Errore durante la chiamata REST:", error);
      alert("Errore di connesione, riprova più tardi!");
    });

}

/*function cerca_personaggi(){
  fetch('http://localhost:8080/personaggio/listaPersonaggi')
	  .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json(); // Decodifica la risposta JSON
    })
}*/

function mostraAbilita(){
  document.getElementById("ab1").style.visibility = 'visible';
  document.getElementById("ab2").style.visibility = 'visible';
  document.getElementById("ab3").style.visibility = 'visible';
  j=1;

}

function listaAbilità(){
if(j!=0){
  let classe = document.getElementById("choice").value;
  const message={
    class : classe
  };
  fetch('http://localhost:8080/personaggio/listaAbilita', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(message)
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Errore nella risposta del server.');
    }
    return response.json();
  })
  .then(data => {
    if (data.error) {
      alert("Errore di connessione, riprova più tardi!")
    } else {
      if (data=="errore") alert("Errore Client")
        else alert("Registrazione effettuata con successo");
    }
  })
  .catch(error => {
    console.error("Errore:", error);

  });
}
j=0;
  
}