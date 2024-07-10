/* jshint esversion: 6 */
/* global google, flatpickr */

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


// Flatpickr Date picker - used for style and functionality
document.addEventListener("DOMContentLoaded", function() {
    const checkinInput = document.getElementById('checkin');
    const checkoutInput = document.getElementById('checkout');
    
    // Initialize Flatpickr
    flatpickr(checkinInput, {
        minDate: "today",
        onChange: function(selectedDates, dateStr, instance) {
            checkoutInput._flatpickr.set('minDate', dateStr);
        }
    });
    
    flatpickr(checkoutInput, {
        minDate: new Date().fp_incr(1), // tomorrow
        onChange: function(selectedDates, dateStr, instance) {
            checkinInput._flatpickr.set('maxDate', dateStr);
        }
    });
});