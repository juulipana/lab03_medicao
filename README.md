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

Pull Requests (PRs) maiores tendem a levar mais tempo para serem concluídas, apresentam um número maior de revisões e têm menores chances de serem fechadas com sucesso. Por outro lado, PRs menores geralmente são encerradas mais rapidamente e passam por menos ciclos de revisão.

## RQ02 – Tempo de análise x Feedback

PRs com maior tempo de análise costumam ter mais revisões, o que pode indicar maior complexidade nas alterações propostas ou mais dificuldade em aprová-las e finalizá-las.

## RQ03 – Descrição do PR x Feedback

PRs que incluem uma descrição clara e detalhada tendem a reduzir o tempo de revisão, pois facilitam a compreensão do código e das modificações realizadas. Isso ajuda a evitar mal-entendidos e revisões desnecessárias, contribuindo para um fechamento mais rápido da PR.

## RQ04 – Interações nos PRs x Feedback

Um grande número de interações em uma PR pode indicar discussões mais extensas e um maior volume de revisões, refletindo um processo de análise mais detalhado e possivelmente mais demorado.

## Tabela Comparativa
| Fator Analisado      | Impacto no Tempo de Revisão                      | Impacto no Nº de Revisões                    | Impacto nas Chances de Fechamento                      | Observação Geral                                                 |
| -------------------- | ------------------------------------------------ | -------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------- |
| **Tamanho da PR**    |  Aumenta (PRs maiores demoram mais)            |  Aumenta (mais pontos a revisar)           |  Diminui (maior complexidade dificulta o fechamento) | PRs menores são revisadas e aprovadas mais rapidamente.          |
| **Tempo de Análise** |  Aumenta (indica revisão longa ou travada)     |  Aumenta (mais ciclos de correção)         |  Diminui (dificuldade em concluir mudanças)          | PRs com análise longa sugerem alto esforço de revisão.           |
| **Descrição da PR**  |  Diminui (melhora entendimento do revisor)     |  Diminui (menos necessidade de retrabalho) |  Aumenta (clareza favorece aprovação)                | Descrições completas facilitam revisões e aceleram o fechamento. |
| **Interações na PR** |  Aumenta (mais discussões estendem o processo) |  Aumenta (mais revisões e debates)         |  Diminui (processo mais demorado para aprovação)     | Muitas interações indicam revisões complexas ou divergências.    |

---

# Conclusão

// TO-DO

# Trabalhos Relacionados

// TO-DO

# Referências

// TO-DO

