import hashlib as shreyash
from pyscript import document

    
def sha1_converter(event):      
    pwd = document.getElementById('sha1_input').value
    naveen = shreyash.shake_128(pwd.encode('utf-8'))
    shrey = naveen.digest(10)
    print(shrey)
    output_div = document.getElementById('sha1_output')
    output_div.innerText = shrey
    