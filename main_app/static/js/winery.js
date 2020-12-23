const ColorSelectEl = document.getElementById('id_color');
console.log('he');
//Set initial class of dropdown
console.log(ColorSelectEl);
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