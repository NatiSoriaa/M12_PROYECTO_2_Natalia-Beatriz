document.addEventListener('DOMContentLoaded', () => {
    // clave para almacenar el estado del sonido en localStorage
    const soundKey = 'towerBlocksSound';
    let soundInstance;


    const savedState = JSON.parse(localStorage.getItem(soundKey)) || {
        isPlaying: false, 
        currentTime: 0,   
    };

    // función para inicializar el sonido y reproducirlo si es necesario
    const initializeSound = () => {
        if (!soundInstance) {
            soundInstance = new Howl({
                src: ["../static/audio/ground-theme.mp3"], 
                loop: true,  
                volume: 0.5, 
                onplay: () => {
                    
                    savedState.isPlaying = true;
                    saveState();  
                },
                onpause: () => {
                    savedState.isPlaying = false;
                    saveState();  
                },
            });

            // restablecer la posición del sonido si ya estaba pausado
            soundInstance.seek(savedState.currentTime);
            
            if (savedState.isPlaying) {
                soundInstance.play();
            }
        }
    };

    // función para guardar el estado actual del sonido en localStorage
    const saveState = () => {
        savedState.currentTime = soundInstance.seek() || 0; 
        // guardar el estado en localStorage
        localStorage.setItem(soundKey, JSON.stringify(savedState));
    };

    // función para configurar los botones de control de audio (reproducir/pausar)
    const setupControlButtons = () => {
        const playButton = document.getElementById('playMusic'); 
        const pauseButton = document.getElementById('pauseMusic'); 

        // agregar evento al botón de "reproducir"
        if (playButton) {
            playButton.addEventListener('click', () => {
                if (soundInstance) {
                    soundInstance.play();  
                }
            });
        }

        // agregar evento al botón de "pausar"
        if (pauseButton) {
            pauseButton.addEventListener('click', () => {
                if (soundInstance) {
                    soundInstance.pause();  
                }
            });
        }
    };

    initializeSound();
    // configurar los botones de control
    setupControlButtons();
    // guardar el estado del sonido cuando la página se cierre o recargue
    window.addEventListener('beforeunload', saveState);
});
