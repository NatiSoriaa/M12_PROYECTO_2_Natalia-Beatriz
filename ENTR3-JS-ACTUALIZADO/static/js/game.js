window.onload = ()=>{
    main();
    
    const botonPausa = document.querySelector('.pause-btn');
    botonPausa.addEventListener('click', pausarJuego);

    // const botonRetry = document.querySelector('.retry-btn');
    // botonRetry.addEventListener('click', retryJuego);
}

//variables

let pausa = false; //importante aqui arriba
let intervaloJuego;
let caerInterval
let moverIntervalX; 
let intervaloContador60; 
let intervaloContador5; 
let bloqueEnCaida;
let bloquesCorrectos; //variable global que cuenta los bloques cque caen correctamente
let listaBloques = [];
let bloquesGanados = []; 

// function apilarbL
function juego(){//funcion que controla el inicio de juego
    if(pausa){
        return; //cuando el juego esta pausado, se detiene la ejecucion
    }
    console.log("juego en ejecucion");
}

//simulador que inicia el juego cada segundo

// function retryJuego(){
//     console.log('Reiniciando juego');

//     //limpiamos los intervalos activos
//     // clearInterval(intervaloJuego);
//     clearInterval(caerInterval);
//     clearInterval(moverIntervalX);
//     clearInterval(intervaloContador60);
//     clearInterval(intervaloContador5);
    
//     localStorage.removeItem('bloquesCorrectos');

//     //borramos los bloques del DOM
//     const bloques = document.querySelectorAll('.Bloque');
//     bloques.forEach(bloque => bloque.remove());

//         //limpiamos listas y estado
//         // listaBloques = [];
//         bloquesGanados = [];
//         bloquesPerdidos = [];

//     actualizarContadorBloques(0);
//     actualizarContadorBloques(bloquesGanados.length);

//     //detenemos los contadores y reiniciamos el juego
//     pausa = false;
//     if(intervaloContador60){
//         clearInterval(intervaloContador60); //limpiamos el contador 60
//     }
//     setTimeout(() => {
//         main();
//         // contadorInicio();


//     }, 100);

//}
function pausarJuego(){ //permite pausar y reanudar
    // pausa = !pausa; //Cambiar estado de juego
    
    if (pausa){
        console.log("juego pausado");
        clearInterval(intervaloCaer);
        clearInterval(intervaloMover);
        clearInterval(intervaloContador60);
        clearInterval(intervaloContador5);
    } else{
        // caerInterval = setInterval(crearBloquesAuto, 1000);  // Asegúrate de que esto esté habilitado al reanudar
        intervaloContador60 = setInterval(contador60sec, 1000); // Intervalo para contador de 60 segundos
        intervaloContador5 = setInterval(contador5sec, 1000);
        // contador60sec(() => {});
        // contador5sec(()=> {});
        console.log("reanudado.");
    }
    pausa = !pausa;
}
function crearBloquesAuto() {
    intervaloJuego = setInterval(() => {
        if (!pausa) crearBloques();
    }, 1000); // Cambia el tiempo según lo que desees
}


// intervaloJuego = setInterval(juego, 1000); 
// function reanudarJuego(){

//     if(pausa){
//         pausa = false;
//         setInterval(juego, 1000);
//     }
// }

// setInterval(()=> {
//     if(!pausa){
//         juego();
//     }
// }, 1000);

//JUEGO

//FUNCIONES

function crearBloques(){ //CREAR Y GUARDAR EN LISTA 
    if (bloqueEnCaida) {
        return; //evita crear nuevos bloques si ya existe uno 
    }
    let gameSection = document.querySelector('.game-container');
    let bloque = document.createElement('div');
    
    bloque.style.position = 'absolute';
    bloque.className = 'Bloque';
    //hacer random para el ancho y alto de los bloques
    bloque.style.width =`${intervalAleatorio(30,80)}px`;
    bloque.style.height = `${intervalAleatorio(30,80)}px`
    bloque.style.background = `rgb(${intervalAleatorio(100, 255)}, ${intervalAleatorio(100, 255)}, ${intervalAleatorio(100, 255)})`;
    // bloque.style.border = '1px solid black';
    bloque.style.margin = '1px';
    bloque.style.top = '0px';
    bloqueEnCaida = true;

    listaBloques.push(bloque);
    gameSection.appendChild(bloque);
    
    movidaHorizontal(bloque).then(() => { //CREA BLOQUES AUTOMATICAMENTE DESPUES DE CAER
        caidaBloques(bloque).then(() => {
            bloqueEnCaida = false;
            crearBloques();
        });
    });
}

function intervalAleatorio(min, max){ 
    return Math.random() * (max-min)+min;
}



function horizontalBloque(bloque) {
    return new Promise((resolve) => { 
        let posX = 0; 
        let direccion = 1;
        const velocidadX = 30; 
        const intervaloX = 50; 
        const containerWidth = document.querySelector('.game-container').offsetWidth; // Ancho del contenedor
        const bloqueWidth = bloque.offsetWidth; 

        // Asegurarse de que el bloque tiene la propiedad 'position: absolute'
        bloque.style.position = 'absolute'; 

        // Mover horizontalmente
        let moverIntervalX = setInterval(() => {
            if (pausa) {
                clearInterval(moverIntervalX); // Si el juego está pausado, detenemos el movimiento
                return;
            }
            posX += velocidadX * direccion; // Incrementar la posición hacia la derecha

            // Si el bloque llega al borde del contenedor, lo detenemos
            if (posX + bloqueWidth >= containerWidth) {
                direccion = -1;
                posX = containerWidth - bloqueWidth; // Aseguramos que el bloque no pase el borde
            }
            if (posX <= 0) {
                direccion = 1; // Cambiar dirección a derecha
                posX = 0; // Asegurar que no sobrepase el borde
            }
    
            bloque.style.left = `${posX}px`; // Actualizar la posición del bloque   
        }, intervaloX);
        
        const gameContainer = document.querySelector('.game-container');

        gameContainer.addEventListener('click', function handler() {
            clearInterval(moverIntervalX); 
            resolve();
        }, 
        { once: true }
    );
        
    });
}

function movidaHorizontal(bloque) {
    return horizontalBloque(bloque);
}


function caerBloque(bloque) {
    return new Promise((resolve) => { 
        let pos = parseInt(bloque.style.top) || 0;
        const velocidad = 30; 
        const intervalo = 50; 

        // Seleccionamos el largo del contenedor y ademas el hijo base
        const gameContainer = document.querySelector('.game-container').offsetHeight;
        const base = document.querySelector('.base');
        const baseTop = base.offsetTop;
        const bloqueHeight = bloque.offsetHeight;
        
        // Altura por defecto: la base del contenedor
        let alturaFinal = baseTop
        let limiteIzquierdo = 0;
        let limiteDerecho = gameContainer.offsetWidth;

        if (listaBloques.length > 1) {
            // Calculamos el ultimo bloque en la lista
            const ultimoBloque = listaBloques[listaBloques.length - 2]; 
            const alturaUltimoBloque = parseInt(ultimoBloque.style.top) || 0; 
            
            // Se determina la altura del ultimo bloque
            alturaFinal = alturaUltimoBloque;
            
            const anchoUltimoBloque = ultimoBloque.offsetWidth;
            const posicionHorizontalUltimoBloque = parseInt(ultimoBloque.style.left) || 0;

            // Creamos los limites disponibles en los que puede caer el bloque
            limiteIzquierdo = posicionHorizontalUltimoBloque;
            limiteDerecho = posicionHorizontalUltimoBloque + anchoUltimoBloque;
        }
        const bloqueWidth = bloque.offsetWidth;

        caerInterval = setInterval(() => {
            if (pausa) {
                // Si el juego está pausado, detenemos la caída
                clearInterval(caerInterval); 
                return;
            }
            pos += velocidad; 
            bloque.style.top = `${pos}px`; 

            if (pos + bloqueHeight >= alturaFinal) {
                clearInterval(caerInterval); 

                // Verificar si está dentro de los límites horizontales
                const posicionHorizontalBloque = parseInt(bloque.style.left) || 0;

                // Se crea una condicion si el bloque cae a la izquierda o la derecha de la torre
                if (posicionHorizontalBloque + bloqueWidth <= limiteIzquierdo || posicionHorizontalBloque >= limiteDerecho) 
                {   
                    listaBloques.push(bloque);
                    // bloquesGanados.push(bloque); //solo push si lo hace bien
                    console.log("puntuaje guardado")
                    actualizarContadorBloques(bloquesGanados.length);

                    localStorage.setItem('bloquesCorrectos', bloquesGanados.length);
                    window.location.href = "./final.html";
                } 
                // Sino se va apilando al ultimo bloque de la torre y agregando a la lista
                else 
                {
                    bloque.style.top = `${alturaFinal - bloqueHeight}px`;
                    listaBloques.push(bloque);
                    bloquesGanados.push(bloque);
                    actualizarContadorBloques(bloquesGanados.length);
                    // Cuando la torre llegue a 4 bloques, se va dezlizando para abajo. 
                    // De esta manera evitamos que colapsen los bloques en la parte superior del container
                    if (listaBloques.length > 4) {
                        bajarTorre();
                    }
                    resolve(); 
                }
            }
        }, intervalo);
    });
}

function caidaBloques(bloque) {
    return caerBloque(bloque);
}

function bajarTorre() {
    const alturaBloque = listaBloques[0].offsetHeight; 

    // Eliminar el bloque más antiguo (el primero de la lista)
    const bloqueInferior = listaBloques.shift(); // Eliminar el primer bloque de la lista
    bloqueInferior.remove(); // Eliminar el bloque del DOM

    // Desplazar el resto de los bloques hacia abajo
    listaBloques.forEach((bloque) => {
        let posicionActual = parseInt(bloque.style.top) || 5;
        bloque.style.top = `${posicionActual + alturaBloque}px`;
    });
}




// function jugada(){

// }

//CONTROL JUEGO

function main() {
    actualizarContadorBloques(0);
    contadorInicio(() => {
        juego(()=> {})
        contador60sec(() => {})
        contador5sec(()=>{})
        // crearBloques(()=>{})
        crearBloquesAuto(()=> {})
        // actualizarContadorBloques(()=>{})
            puntuacion(()=> {})

    })
}



//CONTADORES

function contadorInicio(callback){

    let mensajeInicioJuego = document.createElement('div');
    mensajeInicioJuego.classList.add('mensaje');

    let blockCountdown = document.createElement('h2');
    mensajeInicioJuego.appendChild(blockCountdown);

    document.body.appendChild(mensajeInicioJuego);
	
	mensajeInicioJuego.style.position = 'fixed'; 
    mensajeInicioJuego.style.top = '50%'; 
    mensajeInicioJuego.style.left = '50%';  
    mensajeInicioJuego.style.transform = 'translate(-50%, -50%)'; 
    mensajeInicioJuego.style.fontFamily = "'Press Start', sans-serif"; 
    mensajeInicioJuego.style.textAlign = 'center'; 
    mensajeInicioJuego.style.zIndex = '9999';  
    mensajeInicioJuego.style.color = 'white'; 
    mensajeInicioJuego.style.fontSize = '30px';  
    mensajeInicioJuego.style.padding = '20px'; 
    mensajeInicioJuego.style.borderRadius = '10px';
    let tiempoRestante = 3;

    let interval = setInterval(()=>{
        blockCountdown.textContent = `${tiempoRestante}`;
        tiempoRestante--;

        if(tiempoRestante<0){
            clearInterval(interval);
            blockCountdown.textContent = "Empieza el juego!";

            setTimeout(()=>{
                mensajeInicioJuego.remove(); 
                callback();
            }, 1000);
        }
    },1000);
}

function contador60sec(callback){ //FUNCION ASINCRONA
    let countdown = document.getElementById('countdown');
    let tiempoRestante = 60;

    intervaloContador60 = setInterval(()=>{
        if (pausa){
            clearInterval(intervaloContador60);
            return;
        }
        countdown.textContent = `${tiempoRestante}s`; 
        tiempoRestante--;

        if(tiempoRestante < 0){
            clearInterval(intervaloContador5);
            countdown.textContent = "Se acabó!"; //redirige al final
            setTimeout(()=>{
                if(callback){
                    callback();
                    window.location.href = "./final.html"; //redirigir al final
                }
            }, 1000)
        }
    },1000);
}

function contador5sec(callback) {
    let cincoSec = document.getElementById('time');
    let cont5 = 5;
    const gameContainer = document.querySelector('.game-container');
    intervaloContador5 = setInterval(() => {
        cincoSec.textContent = `${cont5}s click`;
        cont5--;
    
        if(pausa){
            clearInterval(intervaloContador5);
            return;
        }

        if(cont5<0){ //cuando el contador llega a 0 
            clearInterval(intervaloContador5);
            cincoSec.textContent = "KA-BOOM!";
            
            setTimeout(()=> {
                if(callback) {
                    callback();
                    window.location.href = "./final.html";
                } //si hacemos click en la pantalla, vuelve a empezar
            },50);
        } else {
            gameContainer.addEventListener('click', function handler(){
                console.log("has dado click!. volvemos a reiniciar el contador");
                clearInterval(intervaloContador5); //Detenmos el contador
                contador5sec(callback); //volvemos a llamar a la funcion
            }, {once:true});
        }
    },1000); 
}


// contador de bloques que caen correctamente 
function actualizarContadorBloques(bloquesCorrectos){
    const score  = document.getElementById('score');
    score.textContent = bloquesCorrectos;
//funcion que actualiza el record en el dom si el num de bloques supera el record

    const recordMaximo = parseInt(localStorage.getItem('recordMaximo')) || 0;
    if (bloquesCorrectos > recordMaximo) {
        localStorage.setItem('recordMaximo', bloquesCorrectos);
    }
}


