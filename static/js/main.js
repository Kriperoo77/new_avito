async function postData (url = '', data={}){
    const response = await fetch(url, {
        method: 'POST',
        credentials : 'same-origin',
        headers : {
                'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    return await response.json();
}

// слайдер изображений товара
const currentImage = document.querySelector('.gallery__item_current img');
const galleryItems = document.querySelectorAll('.gallery__preview');

galleryItems.forEach(function(element) {
    element.addEventListener('click', function(event) {
        const img = element.querySelector('img');
        if (!element.classList.contains('gallery__preview_active')) {
            currentImage.src = img.src;
            galleryItems.forEach(function(e) {
                e.classList.remove('gallery__preview_active');
            })
            element.classList.add('gallery__preview_active');
        }
    })
})


const addBtns = document.querySelectorAll('.product__add')
const headerCardCout = document.getElementById('header_cart_count')
if (addBtns){
    addBtns.forEach(function(element)
    {
        element.addEventListener('click', function(event){
            event.preventDefault()
            const id = element.detaset['id']
            const url = element.datset['url']
            const count = 1
            const data = {
                'id' : id,
                'count': count
            }
            postData(url, data)
                .then (data => {
                    headerCardCount.innerText = data.card_count
            })
        })
    })
    
}