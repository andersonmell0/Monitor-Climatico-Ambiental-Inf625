# Monitor-Climatico-Ambiental-Inf625
Projeto para monitoramento de condições climáticas e ambientais.

-O diretório "help" contem instruções para ligação dos sensores ao raspberry.

-O diretorio "raspberry-python" contem a biblioteca DHT, o arquivo executável é o "raspberry-python\examples\jsonDHT11.py" ele é responsável
por capturar dados do sensor e gerar um arquivo json.

-O diretorio "site-monitor-ambiental-climatico" contem uma aplicação web em javascript que ler os dados em json e exibe na tela,
o site é completamentamente responsivo.

-O diretório "ecoifba" contem uma aplicação mobile em Qt com uma webview do site.
