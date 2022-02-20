$('vender').click(volver);

function volver(){
    $.ajax(
        {
            url:'ventas.html',
            type:'post',
            dataType:'json',
            data:{
                codigo:$('codigo_productos').val(),
                nombre:$('nombre_productos').val(),
                precio:$('precioventa_productos').val(),
                cant:$('cantidad_productos').val(),
            }
        }    
    ).done(
        function(data){
            $('#salida').append(data);
            $('codigo_productos').val(''),
            $('nombre_productos').val(''),
            $('precioventa_productos').val(''),
            $('cantidad_productos').val('');
        }
    );

}