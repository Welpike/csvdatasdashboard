const url = new URL(window.location);
//initialization
let current_map = url.searchParams.get("map"),
    maps = ["public", "private"],
    hidden_map;

if(current_map==maps[0]){
    hidden_map = maps[1];
}else if(current_map==null){
    hidden_map = maps[1];
}else{
    hidden_map = maps[0];
}

// update iframe src (change map)
document.querySelector("#map_iframe").setAttribute("src", "./embed/"+current_map+".html");

// btn
document.querySelector("#change_map_btn").textContent = hidden_map;
document.querySelector("#change_map_btn").setAttribute("href", url.pathname+"?map="+hidden_map);

// informations popup
 // initialization
document.querySelector("#popup_"+current_map).querySelector("h3").textContent=current_map;

 // toggle view
document.querySelector("#informations_popup").addEventListener("click",()=>{
  document.querySelector("#popup").classList.toggle("show");
  document.querySelector("#popup_"+current_map).classList.toggle("show");
});
