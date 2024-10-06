$(document).ready(function() {
    // Ocultar o formulário de recuperação de senha ao carregar a página
    $("#esqueceu-senha").hide();

    // Mostrar o formulário de recuperação de senha ao clicar no link
    $(".esqueceu_senha_link").click(function(event) {
        event.preventDefault(); // Impede o comportamento padrão do link
        $("#esqueceu-senha").show();
    });
});