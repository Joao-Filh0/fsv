# Flutter Super Version


## MacOs
### Para installar basta rodar o comando :
`brew tap joao-filh0/homebrew-fsv` 
#### em seguida:

`brew install fsv ` 

### Para remover:

`brew untap joao-filh0/homebrew-fsv ` 

#### em seguida:

`brew uninstall fsv `   


# Comandos Básicos

### Para adicionar o caminho onde esta a pasta flutter lembre de por o `/` no final do path

`fsv -p /Users/your-flutter-path/`  ou `fsv -path /Users/your-flutter-path/`

### Para listar todas as versões do Flutter
 `fsv -l`    ou  `fsv -list`
 
### Mudar versão 

 `fsv -c 3.7.7`    ou  `fsv -change 3.7.7`
 
### Rodar o pub get em todo app e todos micro apps

`fsv -pg`    ou  `fsv --pub-get`
#### pode passar na ordem crescente ou decrescente

`fsv -pg asc`    ou  `fsv --pub-get desc`







