// Atualiza Titulo da Lista
$("button.action-edit").click(function () {
    var data_id = $(this).attr("data-title");
    
    $("form#form-title" + data_id).removeClass('d-none')
    $("div#title" + data_id).addClass('d-none')
    
    $('button#edit' + data_id).on("click", function (e) {
        e.preventDefault();
        
        title = $('input#inputText'+ data_id).val();

        $.ajax({
            type: 'GET',
            url: 'http://localhost:8000/update_item',
            data: {'data_id': data_id,'title': title,},
            datatype: "json",
            success: function (data) {
                if (data.status == "update-item") {
                    $("form#form-title" + data_id).addClass('d-none');
                    $("div#title" + data_id).removeClass('d-none'); 
                    $("#title" + data_id).html(data.title); 
                }  
            }
        }); 

    });
});

$("button.expand-detalhs").click(function () {
    var data_id = $(this).attr("data-detal");

    // Toggle classes nos elementos correspondentes
    $("tr#line_ocult" + data_id).toggleClass('d-none');
    $("tr#line_ocult" + data_id).toggleClass('line-ocult');
    $("i#desativado" + data_id).toggleClass('d-none');
    $("i#ativado" + data_id).toggleClass('d-none');
});

// Muda Status do Item da Lista
$("div.SelDiv select").on('change', function () {

var data_id = this.id;
var status_id = $(this).find('option').filter(':selected').val();

console.log("data_id: ", data_id, "status_id: ", status_id)

$.ajax({
    type: 'GET',
    url: 'http://localhost:8000/update_status',
    data: {
        'data_id': data_id,
        'status_id': status_id,
    },
    datatype: "json",

    success: function (data) {
        console.log(data)

        if (data.status == '3') {
            $("div#title" + data_id).addClass('check-status')
        } else {
            $("div#title" + data_id).removeClass('check-status')
        }
    }
});
});

// Deleta um Item da Lista
$("a#btn-delete").on("click", function (e) {
    e.preventDefault();

    var todo_id = $(this).attr("data-delete");
    console.log(todo_id);

    $.ajax({
        type: 'GET',
        url: 'http://localhost:8000/delete',
        data: { 'todo_id': todo_id },
        datatype: "json",
        success: function (data) {

            if (data.status == "delete") {
                $("tbody tr#" + todo_id).fadeOut("slow", function () {
                    $("tbody tr#" + todo_id).remove();
                });
            } else {
                // faz alguma coisa
            }

        }
    });
})