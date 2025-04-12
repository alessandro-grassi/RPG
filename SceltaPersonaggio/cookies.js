function get_personaggio(){
    return getCookie("personaggio");
}
function get_utente(){
    return getCookie("utente");
}
function getCookie(name) {
    const cookies = document.cookie.split(';');
    console.log(cookies);
    for (let cookie of cookies) {
        const [k, v] = cookie.trim().split('=');
        if (k === name) {
            return v;
        }
    }
    return null; // Cookie non trovato
}