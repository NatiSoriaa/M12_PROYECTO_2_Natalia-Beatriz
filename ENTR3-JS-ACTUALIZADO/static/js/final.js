document.addEventListener('DOMContentLoaded', () => {

    //cogemos los bloques que han caido correctamente y los mostramos en score
    const bloquesCorrectos = localStorage.getItem('bloquesCorrectos') || 0; 
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
        record.textContent = `${recordMaximo}`; 
    }
    }

    const userForm = document.getElementById('userForm');

    if (userForm) {
        userForm.addEventListener('submit', (event) => {
            event.preventDefault(); 

            const username = document.getElementById('username').value;

            if (username) {

                //si existe el username, inicia un array vacío si no hay nada
                const scores = JSON.parse(localStorage.getItem('scores')) || [];
                scores.push({ name: username, score: parseInt(bloquesCorrectos) || 0 });
                localStorage.setItem('scores', JSON.stringify(scores));


                //CREACION Y DESCARGA DEL ARCHIVO TXT

                const fileContent = `Username: ${username}\nScore: ${bloquesCorrectos}`;
                const blob = new Blob([fileContent], { type: 'text/plain' });

                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = 'tower_blocks_user_data.txt';

                link.click();

                userForm.reset(); 
                
                alert('Se ha descargado el archivo correctamente.');
            } else {
                alert('Introduzca su nombre de usuario.');
            }
        });
    }
});
