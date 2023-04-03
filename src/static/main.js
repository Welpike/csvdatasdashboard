


//initialization
let current_map = url.searchParams.get("map"),
    maps = ["public", "private"],
    hidden_map;

if(current_map==maps[0]){
    hidden_map = maps[1];
}else{
    hidden_map = maps[0];
}

// update iframe src (change map)
const url = new URL(window.location);
document.querySelector("#map_iframe").addAttribute("src", "./embed/"+current_map+".html");

// btn
document.querySelector("#change_map_btn").textContent = hidden_map;
document.querySelector("#change_map_btn").addAttribute("href", url.searchParams.set("map", hidden_map));
