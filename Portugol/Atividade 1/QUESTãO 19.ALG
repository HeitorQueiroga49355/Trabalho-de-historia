Algoritmo "Quest�o 19"
// Disciplina  : FLA
// Professor   : Raphael Muniz
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Heitor Queiroga Duarte
// Data atual  : 19/08/2020
Var
n, d: real
Inicio
escreva("Digite a dist�ncia: Km")
leia(n)
escreva("Digite o pre�o da gasolina: R$")
leia(d)
n <- n / 12
d <- d * n
escreval("O carro consumiu", n, " litros de combust�vel.")
escreva("Tudo custou R$", d)
Fimalgoritmo