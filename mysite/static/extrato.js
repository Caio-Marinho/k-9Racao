function selecionar(uf)
{
	var combo = document.getElementById("combo");
	
	for (var i = 0; i < combo.options.length; i++)
	{
		if (combo.options[i].value == uf)
		{
			combo.options[i].selected = "true";
			break;
		}
	}
}