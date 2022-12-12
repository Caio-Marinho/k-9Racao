function selecionar(uf)
{
	var mes = document.getElementById("mes");
	
	for (var i = 0; i <= mes.options.length; i++)
	{
		if (mes.options[i].value == uf)
		{
			mes.options[i].selected = "selected" ;
			break;
		}
	}
}