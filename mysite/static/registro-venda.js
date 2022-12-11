function menos() {
    var total = document.querySelector(".m-2")
    console.log(total.textContent)
    if (!total.innerHTML == "0"){
        total.innerHTML = parseInt(total.innerHTML) - 1

    }
    
}


function mais() {
    var total = document.querySelector(".m-2")
    if (!total.innerHTML == "0"){
        total.innerHTML = parseInt(total.innerHTML) + 1

    }

}