# Caracterizando a atividade de code review no GitHub – Laboratório 03

A prática de code review tornou-se uma constante nos processos de desenvolvimento ágil. Em linhas gerais, ela consiste na interação entre desenvolvedores e revisores visando inspecionar o código produzido antes de integrá-lo à base principal, garantindo sua qualidade e evitando a inclusão de defeitos.

No contexto de sistemas open source, especialmente no GitHub, as atividades de code review acontecem por meio de Pull Requests (PRs). Para integrar um código na branch principal, é necessário submeter um PR, que será avaliado e discutido por colaboradores do projeto. Ao final, o merge pode ser aprovado ou rejeitado. Ferramentas de verificação estática podem realizar uma primeira análise, avaliando padrões de estilo ou requisitos definidos pelo projeto.

O objetivo deste laboratório é analisar a atividade de code review em repositórios populares do GitHub, identificando variáveis que influenciam o merge de um PR, sob a perspectiva de desenvolvedores que submetem código.

---

# Alunos

* Juliana Parreiras Guimarães da Cunha
* Pedro Henrique Marques de Oliveira

# Professor

* Danilo de Quadros Maia Filho

---

# Índice

* [Objetivo](#objetivo)
* [Metodologia](#metodologia)

  * [Criação do Dataset](#criação-do-dataset)
  * [Filtragem dos PRs](#filtragem-dos-prs)
  * [Exclusão de Revisões Automáticas](#exclusão-de-revisões-automáticas)
* [Hipóteses](#hipóteses)
* [Desafios](#desafios)
* [Análise dos Resultados](#análise-dos-resultados)
  * [RQ01 – Tamanho dos PRs x Feedback](#rq01---tamanho-dos-prs-x-feedback)
  * [RQ02 – Tempo de análise x Feedback](#rq02---tempo-de-análise-x-feedback)
  * [RQ03 – Descrição do PR x Feedback](#rq03---descrição-do-pr-x-feedback)
  * [RQ04 – Interações nos PRs x Feedback](#rq04---interações-nos-prs-x-feedback)
* [Conclusão](#conclusão)
* [Trabalhos Relacionados](#trabalhos-relacionados)
* [Referências](#referências)

---

# Objetivo

Analisar a atividade de code review desenvolvida em repositórios populares do GitHub, identificando variáveis que influenciam no merge de um PR, sob a perspectiva de desenvolvedores que submetem código aos repositórios selecionados.

---

# Metodologia

## Criação do Dataset

* Seleção de PRs de **repositórios populares** do GitHub (top 200).
* Incluídos apenas repositórios com **≥ 100 PRs** (MERGED + CLOSED).

## Filtragem dos PRs

* Apenas PRs com **status MERGED ou CLOSED**.
* PRs com **pelo menos uma revisão** registrada.

## Exclusão de Revisões Automáticas

* Considerados somente PRs cuja **revisão levou mais de uma hora**, eliminando interações automáticas de bots ou CI/CD.

---

# Hipóteses

// TO-DO

# Desafios

// TO-DO

# Análise dos Resultados

## RQ01 – Tamanho dos PRs x Feedback

// TO-DO

## RQ02 – Tempo de análise x Feedback

// TO-DO

## RQ03 – Descrição do PR x Feedback

// TO-DO

## RQ04 – Interações nos PRs x Feedback

// TO-DO

---

# Conclusão

// TO-DO

# Trabalhos Relacionados

// TO-DO

# Referências

// TO-DO

