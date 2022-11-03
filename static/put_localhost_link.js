const oldLink = window.localStorage.getItem("HUA_V1_CONFIG");
let newLink = ""

const toLocalStorage = JSON.stringify(newLink)

window.localStorage.setItem("HUA_V1_CONFIG", toLocalStorage)

if(window.localStorage.getItem("HUA_V1_CONFIG") != toLocalStorage){
  window.location.reload();
}
