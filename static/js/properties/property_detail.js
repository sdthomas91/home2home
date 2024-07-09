// Property detail map script
function initMap() {
    let latitude = parseFloat(document.getElementById('latitude').innerText);
    let longitude = parseFloat(document.getElementById('longitude').innerText);
    const location = { lat: latitude, lng: longitude };

    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 14,
        center: location
    });

    new google.maps.Marker({
        position: location,
        map: map,
        title: '{{ property.title }}'
    });
}

// Property detail booking form script
$(document).ready(function() {
    // initialise date picker - users can book from today
    $('.input-daterange').datepicker({
        format: 'yyyy-mm-dd',
        startDate: '0d',
        autoclose: true,
        changeMonth: true,
        changeYear: true,
        beforeShowDay: function(date) {
            let YearMonthDay = date.getFullYear() +  "-" + ('0' + (date.getMonth() + 1)).slice(-2) + "-" + ('0' + date.getDate()).slice(-2);
            if ($.inArray(YearMonthDay, unavailableDates) != -1) {
                return false;
            } else {
                return true;
            }
        }
    });

    var $start = $('#startDate');
    var $end = $('#endDate');

    $start.datepicker('setDate', null);
    $end.datepicker('setDate', null);

    $start.on('change', function() {
        var startDate = new Date($start.val());
        startDate.setDate(startDate.getDate());
        $end.datepicker('setDate', startDate);

        $('#checkin').val($start.val());
    });

    $end.on('change', function() {
        $('#checkout').val($end.val());
    });
});