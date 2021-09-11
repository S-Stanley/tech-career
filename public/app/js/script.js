console.log("hello word");

function show_or_hide_menu_mobile(){
	menu_mobile = document.getElementById("menu_mobile");
	if (getComputedStyle(menu_mobile).visibility == "hidden"){
		menu_mobile.style.visibility = "visible";
		menu_mobile.style.position = "relative"
		return ;
	}
	menu_mobile.style.visibility = "hidden";
	menu_mobile.style.position = "absolute"
}