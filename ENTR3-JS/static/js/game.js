window.onload = ()=>{
    //creación de bloques
    contador5sec();
    contadorGeneral()
}

//FUNCIONES

function inicioJuego(){

    let mensajeInicioJuego = document.createElement('div');
    mensajeInicioJuego.classList.add('mensaje');

    let blockCountdown = document.createElement('h2');
    mensajeInicioJuego.appendChild(blockCountdown);

    document.body.appendChild(mensajeInicioJuego);
    let tiempoRestante = 3;

    let interval = setInterval(()=>{
        blockCountdown.textContent = `${tiempoRestante}`;
        tiempoRestante--;

        if(tiempoRestante<0){
            clearInterval(interval);
            blockCountdown.textContent = "Empieza el juego!";
        }
    },1000);
}

function jugada(){

}

function contadorGeneral(){ //FUNCION ASINCRONA
    let countdown = document.getElementById('countdown');
    let tiempoRestante = 60;

    let interval = setInterval(()=>{
        
        countdown.textContent = `${tiempoRestante}s`; 
        tiempoRestante--;

        if(tiempoRestante <0){
            clearInterval(interval);
            countdown.textContent = "Se acabó!"; //redirige al final
        }
    },1000);
}

function contadorBloques(){

}

function crearBloques(){
    let gameSection = document.querySelector('.game-container');
    const max = 50;

    for(let i=0; i < max;i++)
    {
        let bloque = document.createElement('div');
        //hacer random para el ancho y alto de los bloques
        bloque.style.width = '30px';
        bloque.style.height = '30px';
		bloque.style.background = 'blue';
		bloque.style.border = '1px solid white';
        bloque.style.margin = '1px';
        gameSection.appendChild(bloque);
        // let randomWidth = Math.floor(Math.random()*10);
        // let randomHeight = Math.floor(Math.random()*10);
    }
}

function contador5sec() {
    let cont5 = 5; 
    for (let i = 0; i < cont5; i++) {
        setTimeout(() => {
            crearBloques();
        }, i * 5000); 
    }
}




