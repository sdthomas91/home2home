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
