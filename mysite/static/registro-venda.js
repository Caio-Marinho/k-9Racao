const items2 = document.querySelectorAll("[name='btn']");

for (let i = 0; i<items2.length; i++){
    if (items2[i].id == 'plus'){
        items2[i].addEventListener('click', plus.bind(items2[i]))
    }else if (items2[i].id == 'minus'){
        items2[i].addEventListener('click', minus.bind(items2[i]))
    }
}

function plus(element) {
    const elements = element.target.parentNode.childNodes
    for (let i = 0; i < elements.length; i++) {
        if (elements[i].id == 'value'){
            elements[i].innerHTML = parseInt(elements[i].innerHTML) + 1
            const total = elements[i].parentNode.parentNode.childNodes
            for (let j = 0; j < total.length; j++) {
                const element = total[j];
                if (element.tagName == 'P' && element.id != ''){
                    element.innerHTML = parseFloat(parseInt(elements[i].innerHTML) * parseFloat(element.id.replace(',', '.'))).toFixed(2)
                }
            }
        }
    }
}

function minus(element) {
    const elements = element.target.parentNode.childNodes
    for (let i = 0; i < elements.length; i++) {
        if (elements[i].id == 'value'){
            let minus = parseInt(elements[i].innerHTML)
            if (!(minus - 1 < 0)){
                elements[i].innerHTML =  minus - 1
            }
            const total = elements[i].parentNode.parentNode.childNodes
            for (let j = 0; j < total.length; j++) {
                const element = total[j];
                if (element.tagName == 'P' && element.id != ''){
                    element.innerHTML = parseFloat(parseInt(elements[i].innerHTML) * parseFloat(element.id.replace(',', '.'))).toFixed(2)
                }
            }
        }
    }
}