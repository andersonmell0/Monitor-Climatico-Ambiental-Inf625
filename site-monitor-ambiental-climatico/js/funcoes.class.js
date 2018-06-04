// Classe para chamar o Json.
function json(){
	var qtd;
	var retorno;

	// Resgatar valores.
	json.prototype.resgatarValores = function(){
		$('#temperatura').html('Carregando dados...');
		$('#umidade').html('Carregando dados...');
		
		// Estrutura de temperatura e umidade.

		$.getJSON('dados.json', function(data){
			this.qtdTemp = data.coletaTemperatura.length;
			this.retorno = '';
			
			//For para temperatura
			for (i = 0; i < this.qtdTemp; i++){
				this.retorno += data.coletaTemperatura[i].data +'	'+ data.coletaTemperatura[i].hora +'	'+ data.coletaTemperatura[i].temperatura + '<br/>';
			}
			$('#temperatura').html(this.retorno);
		});
		
		$.getJSON('dados.json', function(data){
			this.qtdUmid = data.coletaUmidade.length;
			this.retorno = '';
			
			//For para umidade
			for (i = 0; i < this.qtdUmid; i++){
				this.retorno += data.coletaUmidade[i].data +'	'+ data.coletaUmidade[i].hora +'	'+ data.coletaUmidade[i].umidade + '<br/>';
			}
			$('#umidade').html(this.retorno);
		});
	}
}

// Objeto.
var obj = new json();
obj.resgatarValores();
