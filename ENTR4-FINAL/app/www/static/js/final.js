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

                //inicia un array vacío si no hay nada
                const scores = JSON.parse(localStorage.getItem('scores')) || [];
                scores.push({ name: username, score: parseInt(bloquesCorrectos) || 0 });
                localStorage.setItem('scores', JSON.stringify(scores));
                
                //Descarga del archivo
                try {
                    
                    const fileContent = `Username: ${username}\nScore: ${bloquesCorrectos}`;
                    const blob = new Blob([fileContent], { type: 'text/plain' });
            
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(blob);
                    link.download = 'tower_blocks_user_data.txt';
                    document.body.appendChild(link);
                    link.click();
            
                    userForm.reset(); 

            
                } catch (error) {
                    //error de descarga    
                    alert('No se puede descargar');
                }
            } else {
                alert('Introduzca su nombre de usuario.');
            }
        });
    }
});
