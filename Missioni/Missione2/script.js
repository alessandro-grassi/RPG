// Configurazione
const cfg = { vite:3, puntiPasso:1 };
let g = {x:9,y:0}, vite=cfg.vite, punti=0, fuoriPercorso=false;

// Crea mappa
const mappa = Array(10).fill().map(()=>Array(10).fill('C'));
mappa[9][0]='S'; mappa[0][9]='P';

// Percorso e messaggi
const percorso = [{x:9,y:0},{x:8,y:0},{x:7,y:0},{x:7,y:1},{x:7,y:2},{x:6,y:2},{x:5,y:2},{x:5,y:3},{x:5,y:4},{x:4,y:4},{x:3,y:4},{x:3,y:5},{x:3,y:6},{x:2,y:6},{x:1,y:6},{x:1,y:7},{x:1,y:8},{x:0,y:8},{x:0,y:9}];
const msg = {
  '9-0':"Vai su!", '8-0':"Continua su", '7-0':"Gira a destra", 
  '7-1':"Vai est", '7-2':"Ora su", '6-2':"Tieni sinistra",
  '5-2':"Gira destra", '5-3':"Vai est", '5-4':"Ora su",
  '4-4':"Attenzione!", '3-4':"Gira destra", '3-5':"Vai est",
  '3-6':"Ci sei quasi!", '2-6':"Continua", '1-6':"Ultima svolta",
  '1-7':"Mancano pochi passi", '1-8':"Ora su!", '0-9':"Hai vinto!"
};

// Trappole casuali
const trappole = [];
for(let i=0; i<5; i++) {
  let x,y;
  do {
    x=Math.floor(Math.random()*10);
    y=Math.floor(Math.random()*10);
  } while(mappa[x][y]!=='C' || percorso.some(p=>p.x===x&&p.y===y));
  trappole.push({x,y});
}

function disegnaMappa() {
  let html = '';
  for(let i=0; i<10; i++) {
    for(let j=0; j<10; j++) {
      let cls = 'cella ';
      if(i===g.x && j===g.y) cls += 'giocatore';
      else if(mappa[i][j]==='C') cls += 'cespuglio';
      else if(mappa[i][j]==='P') cls += 'porta';
      else if(mappa[i][j]==='S') cls += 'partenza';
      
      html += `<div class="${cls}">${mappa[i][j]}</div>`;
    }
  }
  document.getElementById('mappa').innerHTML = html;

  // Mostra messaggio se sul cespuglio
  const key = `${g.x}-${g.y}`;
  if(msg[key]) document.getElementById('messaggio').textContent = msg[key];
  
  // Controlla trappole
  if(trappole.some(t=>t.x===g.x&&t.y===g.y)) {
    vite--;
    document.getElementById('vite').textContent = vite;
    document.getElementById('messaggio').textContent = "TRAPPOLA! Hai perso una vita!";
    if(vite <= 0) document.getElementById('messaggio').textContent = "GAME OVER!";
  }
}

function muovi(dx, dy) {
  if(vite <= 0) return;
  
  const nx = g.x + dx, ny = g.y + dy;
  if(nx>=0 && nx<10 && ny>=0 && ny<10) {
    g.x = nx; 
    g.y = ny;
    punti += cfg.puntiPasso;
    document.getElementById('punti').textContent = punti;
    
    // Controlla percorso
    const sulPercorso = percorso.some(p=>p.x===g.x&&p.y===g.y);
    if(!sulPercorso) fuoriPercorso = true;
    else if(fuoriPercorso && g.x===9 && g.y===0) fuoriPercorso = false;
    
    // Controlla vittoria
    if(g.x===0 && g.y===9 && !fuoriPercorso) {
      document.getElementById('messaggio').textContent = "HAI VINTO! Punti: " + punti;
    }
    
    disegnaMappa();
  }
}

// Inizializza
disegnaMappa();
document.onkeydown = e => {
  if(e.key === 'ArrowUp') muovi(-1,0);
  if(e.key === 'ArrowDown') muovi(1,0);
  if(e.key === 'ArrowLeft') muovi(0,-1);
  if(e.key === 'ArrowRight') muovi(0,1);
};
