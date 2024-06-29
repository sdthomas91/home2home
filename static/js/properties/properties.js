

document.addEventListener('DOMContentLoaded', function () {
    var moreAmenitiesButton = document.getElementById('show-more-amenities');
    if (moreAmenitiesButton) {
        moreAmenitiesButton.addEventListener('click', function () {
            var moreAmenities = document.getElementById('more-amenities');
            if (moreAmenities.style.display === 'none') {
                moreAmenities.style.display = 'block';
                this.textContent = 'Show less';
            } else {
                moreAmenities.style.display = 'none';
                this.textContent = 'Show more';
            }
        });
    }
});
