# Monitor-Climatico-Ambiental-Inf625

Projeto para monitoramento de condições climáticas e ambientais através de um raspberry ligado a sensores, o acesso as informações pode ser feita acessando um website ou um app para android.

-O diretório "help" contem instruções para ligação dos sensores ao raspberry.

-O diretorio "raspberry-python" contem a biblioteca DHT, o arquivo executável é o "raspberry-python\examples\jsonDHT11.py" ele é responsável por capturar dados do sensor e gerar um arquivo json. Este diretorio deve ser colocado no raspberry.

-O diretorio "site-monitor-ambiental-climatico" contem uma aplicação web em Html e Javascript que ler os dados do json e exibe na tela,
o site é completamentamente responsivo. Essa aplicação foi testada instalando o servidor web diretamente no raspberry. 
Para instalar o servidor web no raspberry rode o seguinte comando:
#apt-get install apache2

-O diretório "ecoifba" contem uma aplicação mobile em Qt com uma Webview do site que exibe os dados dos sensores. Essa aplicação deve ser rodada em um smartphone com Android e antes de ser compilada deve ser configurado o endereço do servidor web.
