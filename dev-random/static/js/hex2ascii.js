
window.hex2ascii = {};
window.hex2ascii.init = function() {
    var els = document.getElementsByClassName('hex'),
        hex, text,
        i, j, e;

    for(i=0; i < els.length; i++) {
        e = els[i];
        hex = e.innerHTML.split(' ');
        text = "";

        for(j=0; j < hex.length; j++) {
            text += String.fromCharCode(parseInt(hex[j], 16));
        }

        e.innerHTML = text;
        e.className = e.className.replace('hex','');
    }
};
