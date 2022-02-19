var tblProducts;
var vents = {
    items: {//lo  que se manda a la vista
        cli: '',
        pay: '',
        date_joined: '',
        subtotal: 0.00,
        //cant: 0.00,
        iva: 0.00,
        total: 0.00,
        products: []//el detalle es un array en el cual hay varios productos
    },
    //calcular factura
    calculate_invoice: function () {
        var subtotal = 0.00;
        var iva = $('input[name="iva"]').val();
        $.each(this.items.products, function (pos, dict) {
            dict.subtotal = dict.cant * parseFloat(dict.pvp);//cantidad por precio venta
            subtotal += dict.subtotal;
        });
        this.items.subtotal = subtotal;
        this.items.iva = (this.items.subtotal * iva);
        this.items.total = this.items.subtotal;

        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));
        $('input[name="ivacalc"]').val(this.items.iva.toFixed(2));
        $('input[name="total"]').val(this.items.total.toFixed(2));
    },
    add: function (item) {
        this.items.products.push(item);//recibe el item y lo coloco dentro del item de productos
        this.list();
    },
    list: function () {
        this.calculate_invoice();

        tblProducts = $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.products,//mandar colección dediccionarios
            columns: [
                {"data": "id"},//eliminar
                {"data": "name"},
                {"data": "cate.name"},
                {"data": "pvp"},
                {"data": "cant"},
                {"data": "subtotal"},
            ],
            columnDefs: [
                {
                    //eliminar
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat" style="color:white;"><i class="fas fa-trash-alt"></i></a>';
                    }
                },
                {
                    //precio venta
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return 'Gs.' + parseFloat(data).toFixed(2);
                    }
                },
                {
                    //cantidad
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cant" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.cant + '">';
                    }
                },
                {
                    //subtotal
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return 'Gs.' + parseFloat(data).toFixed(2);
                    }
                },
            ],
            //Para las cantidades
            //a medida que se va creando un nuevo registro en la tabla (datatable), se pueden modificar ciertos valores de la tabla
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {
                $(row).find('input[name="cant"]').TouchSpin({//buscar el componente llamado cantidad
                    min: 0,
                    max: 100,
                    step: 0.1,//como se incrementa
                    decimals: 2,//los decimales
                });

            },
            initComplete: function (settings, json) {

            }
        });
    },
};

$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#date_joined').datetimepicker({
        format: 'YYYY-MM-DD', //el formato de la fecha
        date: moment().format("YYYY-MM-DD"), //la fecha del momento, pordefecto
        locale: 'es',  //idioma del componente
        //minDate: moment().format("YYYY-MM-DD") //para los limites de la fecha minDate o maxDate
    });

    $("input[name='iva']").TouchSpin({
        min: 0,
        max: 100,
        step: 0.1,//como se incrementa
        decimals: 2,//los decimales
        boostat: 5,
        maxboostedstep: 10,
        postfix: '%' //etiqueta
    }).on('change', function () {//wn caso de cambiar el iva que se sume sin tener que reiniciar
        vents.calculate_invoice();
    })
        .val(0.11); //valor predeterminado del IVA


// busqueda de productos

    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products', //el key para hacer el autocomplete
                    'term': request.term
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {

            });
        },
        delay: 250,
        minLength: 1,
        select: function (event, ui) {
            event.preventDefault();
            console.clear();
            ui.item.cant = 1;
            ui.item.subtotal = 0.00;
            console.log(vents.items);
            vents.add(ui.item);
            $(this).val('');//para limpiar el buscador
        }
    });

    //Remover todos los items
    $('.btnRemoveAll').on('click', function () {
        if (vents.items.products.length === 0) return false; //es para que la alerta no aparezca si no hay productos
        //alert_action, control que  esta en static/js/functions
        alert_action('Notificación', '¿Estas seguro de eliminar todos los items de tu detalle?', function () {
            vents.items.products = [];
            vents.list();
        });
    });

    $('#tblProducts tbody')

        //boton eliminar
        .on('click', 'a[rel="remove"]', function () {//en evento click con etiqueta a se crea un evento
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            alert_action('Notificación', '¿Estas seguro de eliminar el producto de tu detalle?', function () {
                vents.items.products.splice(tr.row, 1);//splice es el metodo para borra
                vents.list();//refrescar el listado
            });

            // cantidad
        })
        .on('change', 'input[name="cant"]', function () {
            console.clear();
            var cant = parseFloat($(this).val());//converitr a valor decimal
            console.log('x')
            var tr = tblProducts.cell($(this).closest('td, li')).index();//obtenemos un diccionario con la posición de la cantidad para lueg usar lo que tiene
            vents.items.products[tr.row].cant = cant;//voy al array de vetas, itams, products [posición que  se modifica] y accedo al key  de cantidad y lo asigno a una variable
            vents.calculate_invoice();//metodo para calcular la factura
            $('td:eq(5)', tblProducts.row(tr.row).node()).html('Gs.' + vents.items.products[tr.row].subtotal.toFixed(2)); //en la primera parte se encuentra la columna a modificar y en la segunda se  coloca el subtotal nuevo
            //eq(5) es la posición
            //node devuelve el tr completo
            //vents.items.products[tr.row].subtotal.toFixed(2) vamos a la posición
        });

    //Boton X del buscador
    $('.btnClearSearch').on('click', function () {
        $('input[name="search"]').val('').focus();//que limpie lo que tiene el buscador
    });

    // evento guardar
    $('form').on('submit', function (e) {
        e.preventDefault();

        //validaciónes para los items
        if (vents.items.products.length === 0) {
            message_error('Debe al menos tener un item en su detalle de venta');
            return false;
        }

        vents.items.date_joined = $('input[name="date_joined"]').val();//mi fecha
        vents.items.pay = $('select[name="pay"]').val();//id del cliente

        var parameters = new FormData();

        parameters.append('action', $('input[name="action"]').val());//el valor lo recupero del input llamado action
        parameters.append('vents', JSON.stringify(vents.items));//va en forma tipo string para después transformarlo en la vista
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            location.href = '/erp/sale/list/';
        });
    });

    vents.list(); //para que se liste sin pdtos
});
