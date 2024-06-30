Title: Airflow: do básico à implementação do Factory Design Pattern
Date: 2024-07-06 08:40
Category: horarios
Tags: horarios
Slug: palestra1
Author: Rafael Jacobs Kehl



Uma breve introdução ao Airflow, começando dos conceitos básicos e casos de uso até a criação de um DAG.<br>
Analisaremos a estrutura dos DAGs e como temos muito código repetido, que muitas vezes é copiado e colado, o que pode causar alguns erros comuns.<br>
Todo esse código comum entre os DAGs pode ser simplificado através do Factory Design Pattern, que provê uma interface para criar objetos em uma superclasse, com a possibilidade de ser estendido e modificado por subclasses.<br>
Mostrarei uma implementação desse Design Pattern para a criação de DAGs no Airflow e citarei os prós e contras dessa abordagem.