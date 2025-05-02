function mudarPagina(idNovaPagina) {
    const paginas = document.querySelectorAll('.wrapper, .wrapper-ativo');
    paginas.forEach(pagina => {
        pagina.classList.remove('wrapper-ativo');
        pagina.classList.add('wrapper');
    });

    const novaPagina = document.getElementById(idNovaPagina);
    novaPagina.classList.remove('wrapper');
    novaPagina.classList.add('wrapper-ativo');
}