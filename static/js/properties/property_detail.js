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

    if (!checkinInput || !checkoutInput) {
        console.error('Checkin or checkout input not found');
        return;
    }

    // Log initial state
    console.log('Initial checkin min:', checkinInput.getAttribute('min'));
    console.log('Initial checkout min:', checkoutInput.getAttribute('min'));

    // Disable past dates for checkin
    checkinInput.setAttribute('min', today);

    checkinInput.addEventListener('change', function() {
        // Ensure checkout date is not earlier than checkin date
        console.log('Checkin date changed:', this.value);
        checkoutInput.setAttribute('min', this.value);
    });

    checkoutInput.addEventListener('change', function() {
        // Ensure checkin date is not after checkout date
        console.log('Checkout date changed:', this.value);
        checkinInput.setAttribute('max', this.value);
    });

    // Log after setting attributes
    console.log('Checkin min set to:', checkinInput.getAttribute('min'));
    console.log('Checkout min set to:', checkoutInput.getAttribute('min'));
});