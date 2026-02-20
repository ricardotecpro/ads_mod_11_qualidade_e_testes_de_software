# Projeto 07 - Contador MVVM 🏗️

**Objetivo**: Implementar a separação de responsabilidades com LiveData e ViewModel.

## O Desafio
Crie um aplicativo de "Contador de Cliques":
1.  **View**: Um `TextView` mostrando o número e um `Button` (+1).
2.  **ViewModel**: Deve conter um `MutableLiveData<Int>` para o contador.
3.  **Lógica**: Ao clicar no botão, chame uma função no ViewModel que incrementa o valor.
4.  **Observação**: A View deve observar o LiveData e atualizar o texto sempre que o valor mudar.

## O Teste de Ouro
Gire a tela do celular! Se o número se mantiver, seu ViewModel está configurado corretamente. 🔄