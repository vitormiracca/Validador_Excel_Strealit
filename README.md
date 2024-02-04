# Validador de Excel - Pydantic + Streamlit

Projeto para aprender e testar ferramentas úteis no dia a dia da engenheria de dados.
Neste projeto pretendo utilizar ferramentas para validação de integridade e qualidade dos dados, como o PyDantic; ferramentas para testar toda a aplicação antes de realizar um deploy (pytest); tecnologias para adaptar de forma simples uma interface para o usuário (streamlit); além de ferramentas para outros cenários, como manipulação de dados, observabilidade, CI/CD, documentação de projeto...

### Estado Atual

Desenvolvemos um contrato, para servir com validação do schema do excel, de acordo com os requisitos do negócio. Em seguida, criamos um frontend no Streamlit, simples, para o upload do arquivo excel e validação do mesmo.
No backend desenvovlemos a leitura deste excel e a validação do mesmo, usando o contrato (classe Compras) como os requisítos.
Ao fazer o upload de um arquivo que não está dentro do específicado no contrato, os erros são mostrados ao usuário. Foi usado uma iteração dentre as linhas do arquivo, para que em cada linha, um erro seja lançado na tela e consegquentemente facilitar a leitura dos erros pelo usuário.

Ainda há muito para melhorar nessa lógica inicial. Mas pretendo seguir com ela no momento, para conseguir avançar para um protótipo do que poderia ser feito com esse arquivo.

OBS: já foram realizados alguns testes para este projeto, como os testes do contrato e alguns testes simples para deploy da aplicação Streamlit.