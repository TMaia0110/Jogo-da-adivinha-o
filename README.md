## Jogo-da-adivinhacao

Este é um programa simples onde o computador escolhe um número aleatório entre 1 e 50, e o usuário tem 3 chances para adivinhar o número correto. O programa também valida a entrada do usuário, garantindo que somente números entre 1 e 50 sejam aceitos.

## Funcionalidades
- O computador escolhe um número aleatório entre 1 e 50 usando a biblioteca `random`.
- O usuário tem 3 tentativas para adivinhar o número.
- Entradas inválidas (números fora do intervalo de 1 a 50) são rejeitadas e uma mensagem de erro é exibida.
- A biblioteca `time` é utilizada para adicionar pequenos intervalos de tempo para melhorar a experiência do usuário.

## Requisitos
Para executar este programa, você precisa de:
- Python 3.6 ou superior

## Como executar o programa
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Navegue até o diretório do programa:
   ```bash
   cd nome-do-repositorio
   ```

3. Execute o programa:
   ```bash
   python3 number_guessing_game.py
   ```

## Como jogar
1. Ao iniciar o programa, o computador escolhe um número aleatório entre 1 e 50.
2. Você será solicitado a digitar um número.
3. Se sua entrada for inválida (fora do intervalo de 1 a 50), o programa pedirá para você tentar novamente sem perder uma chance.
4. Você tem até 3 tentativas para acertar o número.
5. O programa informa se sua tentativa foi alta, baixa ou correta.

## Exemplo de Saída
```
O computador escolheu um número entre 1 e 50. Tente adivinhar!
Digite seu palpite: 25
Muito alto! Tente novamente.
Digite seu palpite: 10
Muito baixo! Tente novamente.
Digite seu palpite: 15
Parabéns! Você acertou o número!
```

Se você não acertar o número após 3 tentativas, o programa revelará o número correto.

## Bibliotecas utilizadas
- `random`: Para gerar o número aleatório.
- `time`: Para adicionar pausas no fluxo do programa, melhorando a experiência do usuário.

## Contribuições
Contribuições são bem-vindas! Siga os passos abaixo para colaborar:
1. Faça um fork deste repositório.
2. Crie um branch para suas modificações:
   ```bash
   git checkout -b minha-modificacao
   ```
3. Submeta um Pull Request explicando suas alterações.

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.


