document.addEventListener('DOMContentLoaded', () => {
    //cogemos los bloques que han caido correctamente y los mostramos en score
    const bloquesCorrectos = localStorage.getItem('bloquesCorrectos') || 0; //inicia en 0 si no hay datos
    const finalScore = document.getElementById('finalScore');
    if (finalScore) {
        finalScore.textContent = `${bloquesCorrectos}`;
    }

    const recordMaximo = parseInt(localStorage.getItem('recordMaximo')) || 0;
    const record = document.getElementById('record');
    if (record) {
        if (bloquesCorrectos > recordMaximo) {
            localStorage.setItem('recordMaximo', bloquesCorrectos);
            record.textContent = `${bloquesCorrectos}`;
    }else{
        record.textContent = `${recordMaximo}`; // Mostramos el récord existente
    }
    
}


    const userForm = document.getElementById('userForm');

    if (userForm) {
        userForm.addEventListener('submit', (event) => {
            event.preventDefault(); //prevenir que se envie el form

            const username = document.getElementById('username').value;

            if (username) {
                //si existe el username, inicia un array vacío si no hay nada
                const scores = JSON.parse(localStorage.getItem('scores')) || [];
                //json con el username y el score 
                scores.push({ name: username, score: parseInt(bloquesCorrectos) || 0 });
                //guardamos en el localStorage
                localStorage.setItem('scores', JSON.stringify(scores));

                //creacion del archivo txt
                const fileContent = `Username: ${username}\nScore: ${bloquesCorrectos}`;
                const blob = new Blob([fileContent], { type: 'text/plain' });

                //descarga del archivo txt
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = 'tower_blocks_user_data.txt';

                link.click();

                userForm.reset(); //reinicio de la descarga
                alert('Se ha descargado el archivo correctamente.');
            } else {
                alert('Introduzca su nombre de usuario.');
            }
        });
    }
});
