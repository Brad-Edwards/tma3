
function init() {
    var guardian2Button = document.getElementById('button-id-guardian2Button');
    guardian2Button.onclick = toggleDisplay;
}

function toggleDisplay() {
    var registerGuardian2 = document.getElementById('register_guardian2');
    console.log("moo");
    registerGuardian2.classList.toggle('d-none');
}

window.addEventListener('load', init)
