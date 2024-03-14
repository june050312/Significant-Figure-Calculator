window.onload = function() {
    console.log(pyscript.interpreter);
    setTimeout(() => {
        calculate = pyscript.interpreter.globals.get('calculate')
    }, 2000)
};

function getResult() {
    var a = document.getElementById("f-1").value;
    var b = document.getElementById("f-2").value;
    var op = document.getElementById("op").value;

    document.getElementById("result").innerText = calculate(a, b, op);
};