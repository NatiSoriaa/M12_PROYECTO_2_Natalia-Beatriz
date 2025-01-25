document.addEventListener('DOMContentLoaded', () => {
    //estado del sonido en localStorage
    const soundKey = 'towerBlocksSound';
    let soundInstance; 
    let secondSoundInstance; 

    //asociamos un audio según la página
    const page = document.body.getAttribute('data-page');
    const soundSrc = {
        index: "../static/audio/start-sound.mp3",
        final: "../static/audio/death-sound.mp3",
        game: {
            countdown: "../static/audio/countdown.mp3",
            game: "../static/audio/retro-sound.mp3",
        },
    };

    //recuperamos el estado guardado en localStorage
    const savedState = JSON.parse(localStorage.getItem(`${soundKey}_${page}`)) || {
        isPlaying: true, 
        currentTime: 0,
    };

    const initializeSound = () => {
        //configuración para la página de "game"
        if (page === 'game') {
            soundInstance = new Howl({
                src: [soundSrc.game.countdown],
                loop: false, 
                volume: 0.5,
                onplay: () => console.log('reproduciendo countdown...'),
                onend: () => {
                    playSecondSound();
                },
            });

            //configuración del sonido principal del juego
            secondSoundInstance = new Howl({
                src: [soundSrc.game.game],
                loop: false, 
                volume: 0.5,
            });

            //retraso de 1.5 segundos para el countdown
            setTimeout(() => {
                soundInstance.play();
            }, 1500);

        } else if (soundSrc[page]) { 
            soundInstance = new Howl({
                src: [soundSrc[page]],
                loop: false,
                volume: 0.5,
                onplay: () => {
                    console.log(`reproduciendo sonido en ${page}`);
                    saveState(); 
                },
            });

            soundInstance.play();
        }
    };

    //función para reproducir el segundo sonido (sonido principal del juego)
    const playSecondSound = () => {
        if (secondSoundInstance) {
            secondSoundInstance.play();
        }
    };

    //guardar el estado en localStorage
    const saveState = () => {
        if (soundInstance) {
            savedState.currentTime = soundInstance.seek() || 0;
            localStorage.setItem(`${soundKey}_${page}`, JSON.stringify(savedState));
        }
    };

    //configurar botones de control
    const setupControlButtons = () => {
        const playButton = document.getElementById('playMusic');
        const pauseButton = document.getElementById('pauseMusic');

        if (playButton) {
            playButton.addEventListener('click', () => {
                if (soundInstance) {
                    soundInstance.play();
                }
            });
        }

        if (pauseButton) {
            pauseButton.addEventListener('click', () => {
                if (soundInstance) {
                    soundInstance.pause();
                }
                if (secondSoundInstance) {
                    secondSoundInstance.pause();
                }
            });
        }
    };

    //solo inicializa si la página tiene configurado el sonido
    if (soundSrc[page]) {
        initializeSound();
        setupControlButtons();

        //guardar el estado del audio al cerrar o recargar la página
        window.addEventListener('beforeunload', saveState);
    }
});
