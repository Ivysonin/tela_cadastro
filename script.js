document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    /* Pegando os valores digitados pelo usuário nos campos de e-mail e senha no HTML */
    const email = document.getElementById("email").value.trim();
    const senha = document.getElementById("senha").value.trim();

    /* Pegamos os elementos do HTML onde as mensagens de erro serão mostradas. */
    const emailError = document.getElementById("emailError");
    const senhaError = document.getElementById("senhaError");

    /* variaval inicia como false para indicar que não há erros no formulário. Se tiver erro é alterada para true.*/
    let hasError = false;

    /* Deixando mensagem de erro 'invisível'*/
    emailError.style.visibility = "hidden";
    senhaError.style.visibility = "hidden";

    // Fazendo a verificação do e-mail
    if (!email) {
        emailError.textContent = "Por favor, insira seu e-mail."; /* se estiver vazio a caixa de email*/
        emailError.style.visibility = "visible";
        hasError = true; /* indica que tem um erro no formulario */
    } else if (!/\S+@\S+\.\S+/.test(email)) {
        emailError.textContent = "Por favor, insira um e-mail válido."; /* Não digitou um email válido*/
        emailError.style.visibility = "visible";
        hasError = true; /* indica que tem um erro no formulario */
    }

    // Fazendo a verificação da senha
    if (!senha) {
        senhaError.textContent = "Por favor, insira sua senha."; /* Se estiver vazio a caixa de senha */
        senhaError.style.visibility = "visible";
        hasError = true; /* indica que tem um erro no formulario */
    } else if (senha.length <= 8) {
        senhaError.textContent = "A senha deve ter mais de 8 caracteres."; /* Se a senha for menor que 8 caracteres */
        senhaError.style.visibility = "visible";
        hasError = true; /* indica que tem um erro no formulario */
    }

    // Se não acontecer nenhum erro, durante os teste de erro.
    if (!hasError) {
        alert("Login realizado com sucesso!");
    }
});