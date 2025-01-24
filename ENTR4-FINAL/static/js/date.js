function mostrarHoraActual() {
    const fecha = new Date();
    const horas = fecha.getHours().toString().padStart(2, '0');
    const minutos = fecha.getMinutes().toString().padStart(2, '0');

    const horaActual = `${horas}:${minutos}`;
    document.getElementById('currentTime').textContent = `TIME: ${horaActual} `;
}

//se actualiza la hora
setInterval(mostrarHoraActual, 1000);
mostrarHoraActual();
