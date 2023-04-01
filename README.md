# Flutter Super Version

O Flutter Super Version é um gerenciador de versões para o Flutter que permite facilmente alternar entre 
diferentes versões,  como funçao extra  também é possivel executar o `pub get` em todos os micro apps presentes no projeto.

## Instalação

Para instalar o Flutter Super Version, siga os seguintes passos:

### MacOs
Para installar basta rodar o comando :

`brew tap joao-filh0/homebrew-fsv` 

em seguida:

`brew install fsv ` 

Para remover:

`brew untap joao-filh0/homebrew-fsv ` 

em seguida:

`brew uninstall fsv `   


## Comandos Básicos

Adicionar o caminho do flutter :

`fsv -p /Users/your-flutter-path/`  ou `fsv -path /Users/your-flutter-path/`

Para listar todas as versões do Flutter

 `fsv -l`    ou  `fsv -list`
 
Mudar versão 

 `fsv -c 3.7.7`    ou  `fsv -change 3.7.7`
 
Para executar o comando `pub get` no app principal e em todos os micro apps.

`fsv -pg`    ou  `fsv --pub-get`
 
Também é possível executar o comando pub get em ordem crescente ou decrescente.

`fsv -pg asc`    ou  `fsv --pub-get desc`

### Windowns

Baixe o arquivo [fsv.exe](https://github.com/Joao-Filh0/fsv/raw/main/dist/fsv.exe)

Adicione nas variavéis de ambiente ex:. `C:\fsv`


## Contribuindo

Se você encontrar um problema com o Flutter Super Version ou quiser sugerir uma melhoria, sinta-se à vontade para abrir uma issue ou enviar uma pull request no repositório do [Flutter Super Version](https://github.com/Joao-Filh0/fsv).

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.







