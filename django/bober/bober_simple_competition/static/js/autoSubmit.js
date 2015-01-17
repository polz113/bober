window.onload=function(){
	var val = document.getElementById("id_access_code").value;

	if(val.length > 0)
	{
		submitform();
	}
	function submitform(){
		document.getElementById("competition_registration").submit();
	}
}
