function selecionar(valor)
{
	var mes = document.getElementById("mes");

	for (var i = 0; i <= mes.options.length; i++)
	{
		if (mes.options[i].value == valor)
		{
			mes.options[i].selected = "selected" ;
			break;
		}
	}
}