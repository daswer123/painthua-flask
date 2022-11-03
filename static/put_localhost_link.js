const oldLink = window.localStorage.getItem("HUA_V1_CONFIG");
const newLink = ""

window.localStorage.setItem("HUA_V1_CONFIG", newLink)

if(window.localStorage.getItem("HUA_V1_CONFIG") != newLink){
  window.location.reload();
}
