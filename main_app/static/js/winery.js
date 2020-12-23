const ColorSelectEl = document.getElementById('id_color');

//Set initial class of dropdown
if(ColorSelectEl.value !== ""){
    ColorSelectEl.classList.remove('form-placeholder');
}

ColorSelectEl.addEventListener('change', function(e){
    if(e.target.value === ""){
        e.target.classList.add('form-placeholder');
    } else {
        e.target.classList.remove('form-placeholder');
    }
})