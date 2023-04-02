# Flutter Super Version

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

O Flutter Super Version é um gerenciador de versões para o Flutter que permite facilmente alternar entre
diferentes versões, como funçao extra também é possivel executar o `pub get` em todos os micro apps presentes no
projeto.

## Instalação

Para instalar o Flutter Super Version, siga os seguintes passos:

## MacOs

### Opção 1

Para installar basta rodar o comando :

`brew tap joao-filh0/homebrew-fsv`

em seguida:

`brew install fsv `

Para remover:

`brew untap joao-filh0/homebrew-fsv `

em seguida:

`brew uninstall fsv `

### Opção 2 

Segunda opção é baixar o arquivo [fsv](https://github.com/Joao-Filh0/fsv/raw/main/dist/fsv)

depois por no terminal `nano ~/.bash_profile`

colar o path onde vc salvou o arquivo com um alias `fsv` Ex: `alias fsv="/Users/path_onde_salvou/fsv"`

lembre de adicionar o nome do arquivo no path

Pressione `Control + X` para sair do editor Nano e depois `Y` para confirmar as alterações e salvar o arquivo.

Atualize o arquivo de configuração do shell para aplicar as alterações:

`source ~/.bash_profile`

Agora você pode executar seu aplicativo em qualquer lugar digitando `fsv`

## Windowns

Baixe o arquivo [fsv.exe](https://github.com/Joao-Filh0/fsv/raw/main/dist/fsv.exe)

Adicione o path nas variavéis de ambiente ex:. `C:\fsv`

## Comandos :

Adicionar o caminho do flutter :

`fsv -p /Users/your-flutter-path/`  ou `fsv -path /Users/your-flutter-path/`

Ex: Para windowns

`fsv -path C:\src\`

Para listar todas as versões do Flutter

`fsv -l`    ou  `fsv -list`

Mudar versão

`fsv -c 3.7.7`    ou  `fsv -change 3.7.7`

Para executar o comando `pub get` no app principal e em todos os micro apps.

`fsv -pg`    ou  `fsv --pub-get`

Também é possível executar o comando pub get em ordem crescente ou decrescente.

`fsv -pg asc`    ou  `fsv --pub-get desc`

Ver tamanho da pasta que contém os arquivos flutter

`fsv -m`    ou  `fsv --memory`

Clonar uma nova versão do flutter

`fsv -pl 3.7.7` ou `fsv --pull 3.7.7`

Listar todas as versões stable

`fsv -ls` ou ` fsv --list-stable`

Deletar uma versão

`fsv -rm 3.7.7` ou ` fsv --remove 3.7.7`

## Contribuindo

Se você encontrar um problema com o Flutter Super Version ou quiser sugerir uma melhoria, sinta-se à vontade para abrir
uma issue ou enviar uma pull request no repositório do [Flutter Super Version](https://github.com/Joao-Filh0/fsv).

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.








