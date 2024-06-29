// Display and hide filter form on click 
document.getElementById('filter-toggle').addEventListener('click', function() {
    let filterForm = document.getElementById('filter-form');
    if (filterForm.style.display === 'none') {
        filterForm.style.display = 'block';
        this.textContent = 'Hide Filters';
    } else {
        filterForm.style.display = 'none';
        this.textContent = 'Show Filters';
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const amenitiesDropdown = document.getElementById('amenitiesDropdown');
    const amenitiesForm = document.getElementById('filter-form-id');

    amenitiesDropdown.addEventListener('click', function(e) {
        if (e.target.tagName === 'INPUT') {
            e.stopPropagation();
        }
    });

    amenitiesForm.addEventListener('submit', function() {
        const checkboxes = document.querySelectorAll('#amenitiesDropdown .form-check-input');
        const selectedAmenities = [];
        checkboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                selectedAmenities.push(checkbox.value);
            }
        });
        const hiddenField = document.createElement('input');
        hiddenField.type = 'hidden';
        hiddenField.name = 'amenities';
        hiddenField.value = selectedAmenities.join(',');
        amenitiesForm.appendChild(hiddenField);
    });
});