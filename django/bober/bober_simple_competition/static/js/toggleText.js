function toggle(id) {
var ele = document.getElementById('body'+id);
var text = document.getElementById('display'+id);
if(ele.style.display == 'block') {
	ele.style.display = 'none';
	text.innerHTML = '{% trans "Show More" %}';
}
else {
	ele.style.display = 'block';
	text.innerHTML = '{% trans "Show Less" %}';
}
}
