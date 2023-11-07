const fileInput = document.querySelector(".help")
previewImg = document.querySelector(".preview-img img");
chooseImgBtn = document.querySelector(".choose-btn")

/* Previsualizacion de Archivo */
const loadImage = () => {
    let file = fileInput.files[0];
    if(!file) return;
    previewImg.src = URL.createObjectURL(file)
}

fileInput.addEventListener("change",loadImage);
chooseImgBtn.addEventListener("click", () => fileInput.click())

/* Inicializacion del menu de opciones */

document.getElementById("crop").addEventListener("click", function() {
    var div = document.getElementById("crop-content");
    if (div.style.display === "none") {
        div.style.display = "block";
        const image = document.getElementById('image');
        const cropper = new Cropper(image, {
        aspectRatio: 0,
        viewMode: 1,
        dragMode: 1,
        scalable: false,
        crop(event) {
            document.getElementById('x').value = event.detail.x.toFixed(2);
            document.getElementById('y').value = event.detail.x.toFixed(2);
            document.getElementById('ancho').value = event.detail.width.toFixed(2);
            document.getElementById('alto').value = event.detail.height.toFixed(2);
        },
        });
    } else {
        div.style.display = "none";
    }
    
});


document.getElementById("scale").addEventListener("click", function() {
    var div = document.getElementById("scale-content");
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
});

/* Funcionalidad Boton: Cambio de Clase */

const btnElList =  document.querySelectorAll(".button-18")

btnElList.forEach(btnEl => {
    btnEl.addEventListener('click', () => {
        if (btnEl.classList.contains( 'special' )) {
            btnEl.classList.remove('special');
        } else {
            btnEl.classList.add('special');
        }
        
    })
})

