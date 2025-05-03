const carteC = document.getElementById('carte');
const punteggio = document.getElementById('punteggio');
const tempo = document.getElementById('timer');

let carte = [];
let primaCarta = null;
let secondaCarta = null;
let score = 0;
let timer = 0;
let interval;
let match = 0;
let inizioGioco = true;

const images = [
    '/drago1',
    '/drago2',
    '/drago3',
    '/drago4',
    '/drago5',
    '/drago6',
    '/drago7',
    '/drago8'
];

const generaCarte = () => {
    carte = [...images, ...images]; // Duplicazione delle immagini
    carte.sort(() => Math.random() - 0.5);
};

const creaCarta = () => {
    carteC.innerHTML = '';
    generaCarte();
    carte.forEach((img) => {
        const carta = document.createElement('div');
        carta.classList.add('carte');

        const fronte = document.createElement('div');
        fronte.classList.add('fronte');
        
        const immagine = document.createElement('img');
        immagine.src = img;
        fronte.appendChild(immagine);

        const retro = document.createElement('div');
        retro.classList.add('retro');
        
        carta.appendChild(fronte);
        carta.appendChild(retro);

        carta.addEventListener('click', rotazione);
        carteC.appendChild(carta);
    });
    CreaTimer();
};

const rotazione = (event) => {
    if (!inizioGioco) return;
    const clickCarta = event.target.closest('.carte');

    if (!clickCarta || clickCarta === primaCarta || clickCarta.classList.contains('rotazione')) {
        return;
    }
    
    clickCarta.classList.add('rotazione');

    if (!primaCarta) {
        primaCarta = clickCarta;
    } else {
        secondaCarta = clickCarta;
        setTimeout(VerificaMatch, 500);
    }
};

const VerificaMatch = () => {
    if (primaCarta && secondaCarta) {
        const img1 = primaCarta.querySelector('.fronte img').src;
        const img2 = secondaCarta.querySelector('.fronte img').src;
        
        if (img1 === img2) {
            score++;
            match += 2;
            punteggio.textContent = score;
            resetCarte();
            checkVittoria();
        } else {
            setTimeout(() => {
                primaCarta.classList.remove('rotazione');
                secondaCarta.classList.remove('rotazione');
                resetCarte();
            }, 300);
        }
    }
};

const resetCarte = () => {
    primaCarta = null;
    secondaCarta = null;
};

const CreaTimer = () => {
    clearInterval(interval);
    timer = 0;
    tempo.textContent = timer;
    interval = setInterval(() => {
        timer++;
        tempo.textContent = timer;
        if(timer==60){
            window.location.href="../../Missione_Finale/pagina_boss_finale/sconfitta.html";//bisogna mettere l'indirizzo corretto
        }
    }, 1000);
};

const checkVittoria = () => {
    if (match === carte.length) {
        clearInterval(interval);
        alert('Missione superata');
        window.location.href="../../Missione_Finale/pagina_boss_finale/prog.html";// dovrebbe essere il collegamento con il boss finale però bisognerà vedere 
    }
};

creaCarta();
