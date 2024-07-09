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
document.addEventListener("DOMContentLoaded", function() {
    const checkinInput = document.getElementById('checkin');
    const checkoutInput = document.getElementById('checkout');
    const today = new Date().toISOString().split('T')[0];
    
    // Disable past dates for checkin
    checkinInput.setAttribute('min', today);
    // Ensure checkout date is not earlier than tomorrow if selected first
    checkoutInput.setAttribute('min', new Date(new Date().setDate(new Date().getDate() + 1)).toISOString().split('T')[0]);
    
    checkinInput.addEventListener('change', function() {
        // Ensure checkout date is not earlier than checkin date
        if (checkoutInput.value < this.value) {
            checkoutInput.value = '';
        }
        checkoutInput.setAttribute('min', this.value);
    });
    
    checkoutInput.addEventListener('change', function() {
        // Ensure checkin date is not after checkout date
        if (checkinInput.value > this.value) {
            checkinInput.value = '';
        }
        checkinInput.setAttribute('max', this.value);
    });

});