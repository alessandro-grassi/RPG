document.addEventListener("DOMContentLoaded", async () => {
    // Richiedo le classi al backend
    const response = await fetch("http://localhost:8080/mariuzzo/classi");
    const data = await response.json();
    const classi = data["classi"];
    document.getElementById("classi").innerHTML = classi.map((classe, index) => `<h1>${index + 1}) ${classe}</h1>`).join("");
});