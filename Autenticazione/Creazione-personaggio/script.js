function cambiaImmagine() {
    var selezione = document.getElementById("choice").value;
    var class_image = document.getElementById("class-image");
    var image_1 = "https://imgs.search.brave.com/eSRV0IQbqKs4sxfOJFQXt5Hik-bre6joGUeCTVevnRA/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMud2lraWEubm9j/b29raWUubmV0L2Zp/bmFsZmFudGFzeS9p/bWFnZXMvMC8wNS9G/RkVfTWFnb19ibHUu/cG5nL3JldmlzaW9u/L2xhdGVzdC9zY2Fs/ZS10by13aWR0aC1k/b3duLzIyNT9jYj0y/MDE0MTIyMTE0NDEz/NiZwYXRoLXByZWZp/eD1pdA.jpeg"
    var image_2 = "https://imgs.search.brave.com/fwN_Z1DiB1K1QTH_NYIegRtMl1sfkezPuJuu03m9Pv0/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMud2lraWEubm9j/b29raWUubmV0L2Zp/bmFsZmFudGFzeS9p/bWFnZXMvNC80Ni9G/RkVfTWFnb19yb3Nz/by5wbmcvcmV2aXNp/b24vbGF0ZXN0L3Nj/YWxlLXRvLXdpZHRo/LWRvd24vMjUwP2Ni/PTIwMTQxMDIxMjIx/OTA2JnBhdGgtcHJl/Zml4PWl0.jpeg"
    var default_image = "https://cdn.pixabay.com/photo/2016/09/28/02/14/user-1699635_1280.png"

    if (selezione == "opzione1") {
        class_image.src = image_1;
    } else if (selezione == "opzione2") {
        class_image.src = image_2;
    } else {
        class_image.src = default_image;  // Non mostrare nulla altrimenti
    }
}