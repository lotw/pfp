$(document).ready( function() {
});

// click function to show the add location modal
$('#moveBtn').click( function() {
    $('#moveMachine').modal('show');
});

// click function to show the add machine modal
$('#addMachBtn').click( function() {
    $('#addMachine').modal('show');
});

// click function to show the add location modal
$('#addLocBtn').click( function() {
    $('#addLocation').modal('show');
});

$('#locDD li a').click( function() {
    var location = $(this).html();
    var locID = $(this).attr('data-locID');

    $('#locDD .selected').attr('data-locID', locID);
    $('#locDD .selected').html( location );
});

// click function to add a machine
$('#addMach').click( function() {
    // grab the variables needed for the ajax call
    var machName = $('#machName').val();
    var machMfu = $('#manufacturer').val();
    var machYear = $('#year').val();

    $.ajax({
        url: '/ajax/addMachine/',
        data: {
            name: machName,
            mfu: machMfu,
            year: machYear,
        },
    }).done(function(){
        $('#addMachine').modal('hide');
    });

});

// click function to add a location
$('#addLoc').click( function() {
    // grab the variables needed for the ajax call
    var locName = $('#locName').val();
    var locAddr = $('#locAddress').val();
    var locPhone = $('#locPhone').val();

    $.ajax({
        url: '/ajax/addLocation/',
        data: {
            name: locName,
            addr: locAddr,
            phone: locPhone,
        },
    }).done(function(){
        $('#addLocation').modal('hide');
    });
});

$('#assignMach').click( function() {
    // grab the location to assign the machines to
    var location = $('.selected').attr('data-locID');
    // grab the list of machines to add to the location
    var machines = [];
    $('#machList :checked').each( function() {
        machines.push($(this).attr('value'));
    });


    // make the call dogs
    $.ajax({
        url: '/ajax/assignMachine/',
        data: {
            locID: location,
            machines: machines,
        },
    }).done(function(){
        alert('shit added yo');
    });
});