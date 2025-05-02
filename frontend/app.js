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

function enviarCadastro() {
    const nome = document.getElementById('name-input').value;
    const email = document.getElementById('email-input').value;
    const senha = document.getElementById('password-input').value;	
    const senhaConfirmacao = document.getElementById('repeat-password-input').value;

    const data = {
        nome: nome,
        email: email,
        senha: senha,
        confirmar_senha: senhaConfirmacao
    };
    alert('Dados do cadastro: ' + JSON.stringify(data)); // Exibe os dados no console para depuração
    fetch('http://127.0.0.1:8000/cadastro', { 
        method: 'POST', 
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Sucesso:', data);
        alert('Cadastro realizado com sucesso!');
        mudarPagina('login');
    })
    .catch((error) => {
        console.error('Erro:', error);
        alert('Erro ao realizar o cadastro. Verifique os dados e tente novamente.');
    });      
}