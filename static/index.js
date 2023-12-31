const fileInput = document.querySelector(".help")
previewImg = document.querySelector(".preview-img img");
chooseImgBtn = document.querySelector(".choose-btn")
let blur = 0;
let crooper = null;


/* Previsualizacion de Archivo */
const loadImage = () => {
    let file = fileInput.files[0];
    if(!file) return;
    previewImg.src = URL.createObjectURL(file)
    setTimeout(() => {
        let myImg = document.querySelector("#image");
        let realWidth = myImg.naturalWidth;
        let realHeight = myImg.naturalHeight;
        document.getElementById("stats").textContent= "Dimensiones Actuales: " + realWidth + "x" + realHeight;
      }, 500);
}

fileInput.addEventListener("change",loadImage);
chooseImgBtn.addEventListener("click", () => fileInput.click())

/* Inicializacion del menu de opciones */

document.getElementById("crop").addEventListener("click", function() {
    var div = document.getElementById("crop-content");
    if (div.style.display === "none") {
        div.style.display = "block";
        const image = document.getElementById('image');
        cropper = new Cropper(image, {
        aspectRatio: 0,
        viewMode: 1,
        dragMode: 1,
        scalable: false,
        responsive: false,
        crop(event) {
            document.getElementById('x').value = event.detail.x.toFixed(2);
            document.getElementById('y').value = event.detail.y.toFixed(2);
            document.getElementById('ancho').value = event.detail.width.toFixed(2);
            document.getElementById('alto').value = event.detail.height.toFixed(2);
        },
        });
    } else {
        div.style.display = "none";
        document.getElementById('x').value = ''
        document.getElementById('y').value = ''
        document.getElementById('ancho').value = ''
        document.getElementById('alto').value = ''
        cropper.destroy()
    }
    
});

/* Deteccion boton Scale + Reinicio de valor */

document.getElementById("scale").addEventListener("click", function() {
    var div = document.getElementById("scale-content");
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
        document.getElementById('dimensiones').value = ''
    }
});

/* Deteccion boton detector + Reinicio de valor */

document.getElementById("deblur").addEventListener("click", function() {
    var div = document.getElementById("object-content");
    if (div.style.display === "none") {
        document.getElementById("object-detector").value = "1";
        div.style.display = "block";
    } else {
        document.getElementById("object-detector").value = "";
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

