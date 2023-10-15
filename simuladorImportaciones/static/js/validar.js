// Función para validar campos del formulario AGREGAR CLIENTE
/*1. Se crea una función para validar los campos del formulario antes de ser enviados
2. Se definen las variables y se obtienen los valores actuales ingresados por el usuario al formulario.
3. Se agregan varios if anidados para recorrer el formulario y validar que los campos no estén vacíos y valores superiores a 1*/
function validarCampos() {
    var txt_unitsAmount_validar = document.getElementById("txt_unitsAmount").value;
    var txt_usdUnitPrice_validar = document.getElementById("txt_usdUnitPrice").value;
    var txt_unitName_validar = document.getElementById("txt_unitName").value;
    var txt_unitCodevalidar = document.getElementById("txt_unitCode").value;
    var txt_supplierName_validar = document.getElementById("txt_supplierName").value;
    var txt_usdShippingPrice_validar = document.getElementById("txt_usdShippingPrice").value;

    if (txt_unitsAmount_validar.isEmpty || txt_unitsAmount_validar < 1) {
        alert("Complete la cantidad de unidades con un número válido antes de enviar");
        return;
    }

    if (txt_usdUnitPrice_validar.isEmpty || txt_usdUnitPrice_validar < 0) {
        alert("Complete el precio unitario con un número válido antes de enviar");
        return;
    }
    if (txt_unitName_validar.isEmpty) {
        alert("Complete el nombre antes de enviar el formulario");
        return;
    }
    if (txt_unitCodevalidar.isEmpty) {
        alert("Complete el código antes de enviar el formulario");
        return;
    }
    if (txt_supplierName_validar.isEmpty) {
        alert("Complete el proveedor antes de enviar el formulario");
        return;
    }
    if (txt_usdShippingPrice_validar.isEmpty || txt_usdUnitPrice_validar < 0) {
        alert("Complete el valor del envío con un número válido antes de enviar");
        return;
    }
}
