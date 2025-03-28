/*var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function currentDiv(n) {
  showDivs(slideIndex = n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" w3-white", "");
  }
  x[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " w3-white";
} */

  function registrazione(){
    const username= document.getElementById('n_username').value;
    const password= document.getElementById('n_password').value;
    const email= document.getElementById('n_email').value;
    const immagine= document.getElementById('n_image').value;
    
    if(username=="" || password == "" || email == ""){
      alert("Non hai compilato tutti i campi")
    }else{
      const message={
        user : username, 
        pw : password,
        mail : email
      };
      fetch('http://localhost:8080/login/registrazione', {
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
          alert(data);
        }
      })
      .catch(error => {
        console.error("Errore:", error);
  
      });
    }
  
  }
  
  function accedi(){
    const username= document.getElementById('username').value;
    const password= document.getElementById('password').value;
    if(username == "" || password == ""){
      alert("Non hai compilato tutti i campi")
    }else{
      const message={
        user : username, 
        pw : password
      };
      fetch('http://localhost:8080/login/accesso', {
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
          alert("Accesso effettuato con successo");
        }
      })
      .catch(error => {
        console.error("Errore:", error);
  
      });
    }
  }


