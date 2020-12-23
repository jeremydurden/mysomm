const UserHelpEls = document.getElementsByClassName('helptext');
const PasswordEl = document.getElementById('id_password1');
const PasswordHelpEl = PasswordEl.parentElement.nextSibling;
const Pass1El = document.getElementById('id_password1');
const Pass2El = document.getElementById('id_password2');

for (let i = 0; i < UserHelpEls.length; i++) {
    UserHelpEls.item(i).classList.add('hidden');
}
PasswordHelpEl.classList.add('hidden');
Pass1El.classList.add('form-control');
Pass2El.classList.add('form-control');
