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

# Sumário

* [Objetivo](#objetivo)
* [Metodologia](#metodologia)

  * [Criação do Dataset](#criação-do-dataset)
  * [Filtragem dos PRs](#filtragem-dos-prs)
  * [Exclusão de Revisões Automáticas](#exclusão-de-revisões-automáticas)
* [Hipóteses](#hipóteses)
* [Desafios](#desafios)
* [Análise dos Resultados](#análise-dos-resultados)
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

## RQ01 – Tamanho dos PRs x Feedback

- Hipótese 1a: PRs maiores têm menor probabilidade de serem fechadas com sucesso devido à maior complexidade.  
- Hipótese 1b: PRs menores tendem a ser aprovadas mais rapidamente e com menos revisões.  

## RQ02 – Tempo de análise x Feedback

- Hipótese 2a: PRs que permanecem mais tempo em análise têm menor probabilidade de fechamento bem-sucedido.  
- Hipótese 2b: Maior tempo de análise está associado a PRs mais complexas ou com necessidade de mais ajustes.  

## RQ03 – Descrição do PR x Feedback

- Hipótese 3a: PRs com descrições claras e detalhadas têm maior chance de serem aprovadas.  
- Hipótese 3b: PRs com descrições incompletas ou confusas têm maior probabilidade de gerar revisões adicionais e atrasos no fechamento.  

## RQ04 – Interações nos PRs x Feedback

- Hipótese 4a: PRs com muitas interações (comentários, discussões) tendem a ter fechamento mais demorado.  
- Hipótese 4b: Maior número de interações pode indicar divergências ou revisões complexas, reduzindo as chances de fechamento rápido.  

## RQ05 – Tamanho dos PRs x Número de revisões

- Hipótese 5: PRs maiores tendem a passar por mais revisões antes de serem aprovadas.  

## RQ06 – Tempo de análise x Número de revisões

- Hipótese 6: PRs que permanecem mais tempo em análise tendem a acumular mais revisões.  

## RQ07 – Descrição do PR x Número de revisões

- Hipótese 7: PRs com descrições claras e detalhadas tendem a necessitar de menos revisões.  
- Hipótese 7b: PRs com descrições pobres exigem mais revisões para clarificação e correção.  

## RQ08 – Interações nos PRs x Número de revisões

- Hipótese 8: PRs com maior número de interações tendem a ter mais revisões antes de serem concluídas.  

## Tabela Comparativa
| Fator Analisado      | Impacto no Tempo de Revisão                      | Impacto no Nº de Revisões                    | Impacto nas Chances de Fechamento                      | Observação Geral                                                 |
| -------------------- | ------------------------------------------------ | -------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------- |
| **Tamanho da PR**    | Aumenta (PRs maiores demoram mais)             | Aumenta (mais pontos a revisar)             | Diminui (maior complexidade dificulta o fechamento)   | PRs menores são revisadas e aprovadas mais rapidamente.          |
| **Tempo de Análise** | Aumenta (indica revisão longa ou travada)      | Aumenta (mais ciclos de correção)          | Diminui (dificuldade em concluir mudanças)           | PRs com análise longa sugerem alto esforço de revisão.           |
| **Descrição da PR**  | Diminui (melhora entendimento do revisor)      | Diminui (menos necessidade de retrabalho)  | Aumenta (clareza favorece aprovação)                 | Descrições completas facilitam revisões e aceleram o fechamento. |
| **Interações na PR** | Aumenta (mais discussões estendem o processo)  | Aumenta (mais revisões e debates)          | Diminui (processo mais demorado para aprovação)      | Muitas interações indicam revisões complexas ou divergências.    |

# Desafios

// TO-DO

# Análise dos Resultados - Grupo A - Feedback Final das Revisões

## RQ01 – Qual a relação entre o tamanho dos PRs e o feedback final das revisões?

O gráfico de pontos abaixo representa a relação entre o tamanho das pull requests e a quantidade do feedback. Pelo gráfico, podemos observar que a correlação entre o tamanho das pull requests e a quantidade de feedback é baixa: independentemente de serem grandes ou pequenas, o número de feedbacks tende a permanecer relativamente o mesmo com a excessão de alguns outliers.

Isso significa que as PRs analisadas possuem maior qualidade?

**Não necessariamente!**

Muitos fatores podem influenciar esse resultado, e para obter conclusões mais precisas seria necessário um estudo maior. Entre os possíveis fatores, destacam-se:

* Diferenças no nível de experiência dos revisores;
* Prioridades e carga de trabalho da equipe;
* Complexidade do código não necessariamente relacionada ao tamanho da PR;
* Preferência por revisar apenas trechos específicos do código;

<img width="2087" height="1407" alt="image" src="https://github.com/user-attachments/assets/4d506742-2ea1-49d9-b381-415d0ef191b0" />

## RQ02 – Qual a relação entre o tempo de análise dos PRs e o feedback final das revisões?

A partir da coleta de dados, geramos o gráfico abaixo, que representa a relação entre o tempo de análise e a quantidade de feedback recebido. No geral, observa-se valores constantes para PRs com mais ou menos feedbacks. No entanto, alguns casos se destacam como visto no início do gráfico: PRs com maior número de revisões tendem a demandar mais tempo de análise.

Isso é esperado, visto que quanto mais comentários ou solicitações de alteração uma PR recebe, maior é o esforço necessário para revisar, discutir e validar as mudanças propostas.

<img width="2087" height="1411" alt="image" src="https://github.com/user-attachments/assets/8705ec53-2cfa-4789-9813-7f5cb977e88a" />

## RQ03 – Qual a relação entre a descrição dos PRs e o feedback final das revisões?

O gráfico abaixo mostra a relação entre a extensão da descrição das PRs e a quantidade de feedback recebido. 

Observa-se que PRs com descrições muito longas costumam receber menos feedback. Alguns motivos para isso podem ser:

* Mais clareza: Descrições detalhadas ajudam o revisor a entender melhor o projeto, tirando dúvidas e evitando comentários desnecessários.
* Código mais consolidado: PRs longas podem indicar que o código já foi discutido antes e está mais pronto, precisando de menos revisões.

Já PRs com descrições curtas ou médias tendem a receber mais feedback, possivelmente por:

* Menos clareza: Descrições curtas podem deixar o revisor perdido ou confuso sobre o que foi feito.
* Mais perguntas: Revisores precisam fazer mais comentários para entender a PR completamente.

<img width="2087" height="1408" alt="image" src="https://github.com/user-attachments/assets/0804ed66-8314-459e-a1e8-cf6987eaac6c" />

## RQ04 – Qual a relação entre as interações nos PRs e o feedback final das revisões?

PRs que chegam ao estado final de revisão tendem a apresentar um maior número de interações, incluindo comentários, revisões e commits. Como mostra o gráfico abaixo, essa relação é crescente e progressiva:

* PRs com menos feedback têm menos interações;
* PRs com mais feedback recebem mais ajustes e modificações.

<img width="2060" height="1408" alt="image" src="https://github.com/user-attachments/assets/d2973f2d-642a-4754-ae73-445cb7c2e871" />

# Análise dos Resultados - Grupo B - Número de Revisões

## RQ05 – Qual a relação entre o tamanho das PRs e o número de revisões realizadas?

De acordo com os dados analisados, PRs maiores tendem a receber menos revisões, com exceção de alguns outliers. Por outro lado, PRs de tamanho pequeno e médio geralmente recebem um número médio a alto de revisões.

Alguns fatores que podem explicar esse comportamento incluem:

* Complexidade percebida: PRs maiores podem ser mais complexas, fazendo com que revisores dividam a revisão em diversas etapas menores.
* Processos de revisão: PRs grandes podem já ter passado por discussões prévias ou estarem mais consolidadas, enquanto PRs menores e médias recebem revisões mais ativas.

<img width="2060" height="1407" alt="image" src="https://github.com/user-attachments/assets/b9e05057-feb2-4749-b6c6-dcbfbc71fa47" />

## RQ06 – Qual a relação entre o tempo de análise dos PRs e o número de revisões realizadas? (// REVIEW)

O boxplot abaixo mostra a relação entre o tempo de análise das PRs e o número de revisões:

* PRs analisadas rapidamente (<3 dias) ou muito lentamente (>30 dias) apresentam mais variação no número de revisões.
* Na maioria dos casos, as PRs recebem poucas revisões (mediana de 0 a 2), independentemente do tempo de análise.
* Alguns outliers indicam que certas PRs podem exigir muitas revisões, mesmo em análises curtas ou longas.
  
<img width="2060" height="1411" alt="image" src="https://github.com/user-attachments/assets/6cfe47e5-238f-42ae-83ba-326644a11ba9" />

## RQ07 – Qual a relação entre a descrição dos PRs e o número de revisões realizadas? (// REVIEW)

O tamanho da descrição da PR quase não influencia o número de revisões, ou seja, apreseta uma orrelação fraca (r = 0,12).

* A maioria dos PRs recebe poucas revisões (0 a 5), independentemente do tamanho da descrição.
* Alguns PRs têm muitas revisões (até 30), mas sem relação clara com o tamanho da descrição.

Mesmo descrições longas não garantem menos revisões.

<img width="2060" height="1410" alt="image" src="https://github.com/user-attachments/assets/ee10e3ad-0b80-4739-98ea-4c8174ba77fa" />

## RQ08 – Qual a relação entre as interações nos PRs e o número de revisões realizadas?

O gráfico abaixo mostra que há pouca ou nenhuma correlação entre o número de interações em uma PR e o número de revisões realizadas, com um coeficiente de correlação próximo de zero (r = 0.02). Isso indica que a quantidade de comentários ou discussões não parece influenciar significativamente o número de ciclos de revisão necessários.

<img width="1828" height="1408" alt="image" src="https://github.com/user-attachments/assets/46e9b6d4-a2ab-4259-9d05-a4295117805c" />

# Conclusão

A análise dos dados de code review em repositórios populares do GitHub mostra que nem sempre as hipóteses iniciais se confirmam. Por exemplo, embora se esperasse que PRs maiores fossem revisadas mais vezes, os dados indicam que, na prática, o tamanho da PR não garante um número maior de revisões. Da mesma forma, a clareza das descrições ajuda a reduzir dúvidas e acelerar o fechamento, mas não necessariamente diminui a quantidade de revisões. Em resumo, fatores como complexidade do código, experiência dos revisores e políticas do repositório influenciam tanto quanto as variáveis observadas.

Um aprendizado importante é que processos de revisão são mais dinâmicos e dependem de múltiplas dimensões, não apenas de métricas objetivas como tamanho ou número de interações. A quantidade de feedback ou de revisões não é previsível apenas por essas variáveis, mas a clareza na comunicação e a organização do código ajudam a tornar a revisão mais eficiente. Para equipes e desenvolvedores, isso reforça a importância de escrever boas descrições, revisar código de forma incremental e manter interações construtivas, mesmo que nem sempre reduzam a quantidade de revisões.

## Tabela comparativa: Hipóteses vs. Resultados

| Hipótese | Resultado Observado | Aceitamos/Negamos |
|----------|-------------------|-----------------|
| H1 | PRs maiores não mostraram relação clara com fechamento | Negado |
| H2 | Parcialmente confirmado: PRs menores geralmente recebem menos feedback | Aceito Parcial |
| H3 | Tempo de análise longo não garante menor fechamento | Negado |
| H4 | PRs maiores tendem a receber menos revisões (com outliers) | Negado |
| H5 | Correlação fraca entre tamanho da descrição e número de revisões | Negado |
| H6 | Confirmado: descrições longas ajudam na aprovação | Aceito |
| H7 | Pouca ou nenhuma correlação entre interações e número de revisões | Negado |
| H8 | Correlação próxima de zero (r = 0.02) | Negado |

# Trabalhos Relacionados

## Beyond the Code: Investigating the Effects of Pull Request Conversations on Design Decay

**Contexto**
O desenvolvimento colaborativo de software, em plataformas como GitHub e GitLab, ocorre com base em pull requests, onde desenvolvedores discutem mudanças e compartilham conhecimento. Essas conversas são influenciadas por fatores sociais — como a forma de comunicação, o conteúdo das discussões e a organização da equipe. Embora já se saiba que aspectos sociais afetam a qualidade do software, ainda não está claro como e quanto eles influenciam a degradação de design (ou design decay), isto é, o enfraquecimento da estrutura e manutenibilidade do código ao longo do tempo.

**Objetivo:**
Investigar como aspectos sociais das conversas em pull requests afetam a degradação de design.

**Método:**
O estudo analisou 10.746 conversas de pull requests em 11 sistemas de código aberto, considerando três dimensões sociais:

* Conteúdo das discussões – o que é falado nas mensagens.
* Dinâmicas de comunicação – duração, frequência e engajamento.
* Dinâmicas organizacionais – tamanho da equipe e diversidade de gênero.

Foram aplicadas 18 métricas sociais e modelos estatísticos (como regressão logística) para avaliar a relação de cada métrica com o design decay.

**Resultados:**
Os autores descobriram que:

* Fatores como tamanho e duração das discussões, presença de termos relacionados a design, tamanho da equipe e diversidade de gênero ajudam a distinguir pull requests que impactam o design daquelas que não impactam.
* Crescimento organizacional e diversidade de gênero estão associados à redução da degradação de design.
* Cada comunidade tem suas próprias características que influenciam a manutenção da qualidade de design.
* Feedback rápido, comunicação ativa e discussões focadas em design com participação variada melhoram a estrutura do software.

**Conclusão:**
Os aspectos sociais das conversas em pull requests são indicadores úteis da degradação de design. Melhorar a comunicação e promover equipes diversas pode ajudar a evitar ou reduzir problemas estruturais no código.

# Referências

C. Barbosa, A. Uchôa, D. Coutinho, W. K. G. Assunção, A. Oliveira, A. Garcia, B. Fonseca, M. Rabelo, J. E. Coelho, E. Carvalho, e H. Santos, “Beyond the Code: Investigating the Effects of Pull Request Conversations on Design Decay,” 2023 IEEE/ACM 17th International Symposium on Empirical Software Engineering and Measurement (ESEM), New Orleans, LA, USA, 2023. Disponível em: https://ieeexplore.ieee.org/document/10304805
. Acesso em: [data de acesso].

