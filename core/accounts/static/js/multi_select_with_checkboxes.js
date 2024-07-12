// reminders/static/js/multi_select_with_checkboxes.js
document.addEventListener('DOMContentLoaded', function () {
    var dropdowns = document.querySelectorAll('.dropdown-multiselect');

    dropdowns.forEach(function (dropdown) {
        var select = dropdown.querySelector('select');
        var checkboxes = dropdown.querySelectorAll('input[type="checkbox"]');
        var dropbtn = dropdown.querySelector('.dropbtn');
        var dropdownContent = dropdown.querySelector('.dropdown-content');

        // Toggle dropdown content visibility on button click
        dropbtn.addEventListener('click', function (event) {
            event.stopPropagation(); // Prevent dropdown from closing on button click
            dropdownContent.classList.toggle('show');
        });

        // Close dropdown content if clicked outside
        document.addEventListener('click', function (event) {
            if (!dropdown.contains(event.target)) {
                dropdownContent.classList.remove('show');
            }
        });

        // Initialize checkboxes based on select's initial state
        checkboxes.forEach(function (checkbox) {
            var option = select.querySelector('option[value="' + checkbox.value + '"]');
            checkbox.checked = option.selected;
        });

        // Update select based on checkbox changes
        checkboxes.forEach(function (checkbox) {
            checkbox.addEventListener('change', function () {
                var option = select.querySelector('option[value="' + checkbox.value + '"]');
                option.selected = checkbox.checked;
            });
        });

        // Update checkboxes based on select changes
        select.addEventListener('change', function () {
            checkboxes.forEach(function (checkbox) {
                var option = select.querySelector('option[value="' + checkbox.value + '"]');
                checkbox.checked = option.selected;
            });
        });
    });
});
