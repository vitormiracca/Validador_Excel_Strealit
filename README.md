# Validador de Excel - Pydantic + Streamlit

Projeto para aprender e testar novas ferramentas úteis no dia a dia da engenheria de dados.
Neste projeto pretendo utilizar ferramentas para validação de integridade e qualidade dos dados, como o PyDantic; ferramentas para testar toda a aplicação antes de realizar um deploy (pytest); tecnologias para adaptar de forma simples uma interface para o usuário (streamlit); além de ferramentas para outros cenários, como manipulação de dados, observabilidade, CI/CD, documentação de projeto...

### Estado Atual

Desenvolvemos um contrato, para servir com validação do schema do excel, de acordo com os requisitos do negócio. 
Este contrato é realizado via pydantic e defini as regras para o schema do excel a ser carregado no Banco de Dados.    

Em seguida, desenvolvemos uma aplicação streamlit, onde o usuário consegue carregar o excel do Tema específico, para rodar a validação do mesmo (utilizando o contrato como base).
Se não validado, foi usado uma iteração dentre as linhas do arquivo, para que em cada linha onde a validação do contrato não passou, um erro seja lançado na tela e consegquentemente facilitar a leitura dos erros pelo usuário.
Se validado, a aplicação habilita o botão de carregar aos database, onde o backend irá inputar os registros do excel no database PostgreSQL que subimos.
    
Foi desenvolvido alguns testes simples para garantir a integridade da aplicação antes de submete-la ao repositório remoto, como testes unitários, testes funcionais e testes de integração.

Também iniciamos um Workflow para CI/CD (entrega contínua), com Github Actions. Esse workflow é startado a partir do Pull Request para a branch master e segue o fluxo de intalação do pyhton, instalação das dependência, execução dos testes. Assim, sendo a branch Master a branch de Produção, garantimos que nenhum Pull Request com códigos com Bugs (bugs cobertos pelos testes, diga-se de passagem) irão conseguir ser mergeados e impactar assim o ambeinte de Produção (usuários).

### toDO

Ainda tem bastante para melhorar, não só nos códigos como também no aprendizado de novas tecnologias (objetivo deste projeto).
Ainda pretendo adicionar documentações utilziando Mkdocs; usar o Sentry como ferramenta de Observabilidade; e quem sabe até adicionar dados mais robustos (como mais modelos de excel, mais validações como por exexmplo a impossibilidade de enviar registros que já estão presentes no database...);