# Projeto 10 - Buscador de Repositórios 🐙

**Objetivo**: Consumir dados reais da API do GitHub usando Retrofit.

## O Desafio
1.  Configure o **Retrofit** com o conversor Gson.
2.  Crie a interface `GitHubService` para buscar repositórios de um usuário:
    `GET users/{user}/repos`
3.  Crie uma Data Class `Repo` para mapear o nome e as estrelas (`stargazers_count`).
4.  Exiba os nomes dos repositórios no Logcat ou em uma lista simples na tela.

## Nota Importante
Não esqueça da permissão de Internet no `AndroidManifest.xml`! 🌐