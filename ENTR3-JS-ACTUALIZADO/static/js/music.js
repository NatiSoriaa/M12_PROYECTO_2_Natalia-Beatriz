document.addEventListener('DOMContentLoaded', () => {
    // clave para almacenar el estado del sonido en localStorage
    const soundKey = 'towerBlocksSound';
    let soundInstance;

    // recuperar el estado guardado del sonido (si existe) o establecer valores predeterminados
    const savedState = JSON.parse(localStorage.getItem(soundKey)) || {
        isPlaying: false, // indica si el sonido está reproduciéndose
        currentTime: 0,   // guarda la posición actual de la pista
    };

    // función para inicializar el sonido y reproducirlo si es necesario
    const initializeSound = () => {
        if (!soundInstance) {
            soundInstance = new Howl({
                src: ["../static/audio/ground-theme.mp3"], // archivo de audio
                loop: true,  // hacer que el audio se repita
                volume: 0.5, // ajustar volumen (de 0 a 1)
                onplay: () => {
                    // cuando el sonido empiece a reproducirse, actualizar el estado
                    savedState.isPlaying = true;
                    saveState();  // guardar el estado actual
                },
                onpause: () => {
                    // cuando el sonido se pause, actualizar el estado
                    savedState.isPlaying = false;
                    saveState();  // guardar el estado actual
                },
            });

            // restablecer la posición del sonido si ya estaba pausado
            soundInstance.seek(savedState.currentTime);
            // si el sonido estaba reproduciéndose, iniciar la reproducción
            if (savedState.isPlaying) {
                soundInstance.play();
            }
        }
    };

    // función para guardar el estado actual del sonido en localStorage
    const saveState = () => {
        savedState.currentTime = soundInstance.seek() || 0; // obtener la posición actual de la pista
        // guardar el estado en localStorage
        localStorage.setItem(soundKey, JSON.stringify(savedState));
    };

    // función para configurar los botones de control de audio (reproducir/pausar)
    const setupControlButtons = () => {
        const playButton = document.getElementById('playMusic'); // obtener el botón de reproducción
        const pauseButton = document.getElementById('pauseMusic'); // obtener el botón de pausa

        // agregar evento al botón de "reproducir"
        if (playButton) {
            playButton.addEventListener('click', () => {
                if (soundInstance) {
                    soundInstance.play();  // reproducir el sonido
                }
            });
        }

        // agregar evento al botón de "pausar"
        if (pauseButton) {
            pauseButton.addEventListener('click', () => {
                if (soundInstance) {
                    soundInstance.pause();  // pausar el sonido
                }
            });
        }
    };

    // inicializar el sonido cuando la página cargue
    initializeSound();
    // configurar los botones de control
    setupControlButtons();

    // guardar el estado del sonido cuando la página se cierre o recargue
    window.addEventListener('beforeunload', saveState);
});
