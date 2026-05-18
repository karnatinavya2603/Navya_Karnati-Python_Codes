
const buttons = document.querySelectorAll('button');

buttons.forEach(btn=>{
    btn.addEventListener('click',()=>{
        if(btn.innerText.includes('Cart') || btn.innerText.includes('Add')){
            alert('Product added successfully!');
        }
    });
});
