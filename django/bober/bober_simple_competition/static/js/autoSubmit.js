window.onload=function(){
	var val = document.getElementByID("id_access_code").value();

	if(val.length > 0)
	{
		function submitform(){
		  document.getElementById("competition_registration").submit();
		}
	}
}
