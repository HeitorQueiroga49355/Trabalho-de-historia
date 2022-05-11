Algoritmo "Questão 19"
// Disciplina  : FLA
// Professor   : Raphael Muniz
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Heitor Queiroga Duarte
// Data atual  : 19/08/2020
Var
n, d: real
Inicio
escreva("Digite a distância: Km")
leia(n)
escreva("Digite o preço da gasolina: R$")
leia(d)
n <- n / 12
d <- d * n
escreval("O carro consumiu", n, " litros de combustível.")
escreva("Tudo custou R$", d)
Fimalgoritmo