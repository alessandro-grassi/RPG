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