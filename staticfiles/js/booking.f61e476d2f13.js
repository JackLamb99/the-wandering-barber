// Toggles the selected button class
function toggleButton(button) {
    const isRadio = button.querySelector('input[type="radio"]');
    if (isRadio) {
        // For radio buttons, unselect other buttons in the same group
        const btnGroup = button.closest('.btn-group-toggle');
        btnGroup.querySelectorAll('.btn').forEach(function(btn) {
            btn.classList.remove('selected');
        });
    }

    // Toggles the 'selected' class on the clicked button
    if (!button.classList.contains('selected')) {
        button.classList.add('selected');
    } else {
        button.classList.remove('selected');
    }
}

// Toggles between "New Booking" and "My Bookings" sections
function toggleSection(section) {
    const newBooking = document.getElementById('new-booking');
    const myBookings = document.getElementById('my-bookings');

    if (section === 'new-booking') {
        newBooking.style.display = 'block';
        myBookings.style.display = 'none';
        document.getElementById('new-booking-btn').classList.add('btn-selected');
        document.getElementById('my-bookings-btn').classList.remove('btn-selected');
        document.getElementById('my-bookings-btn').classList.add('btn-unselected');
        document.getElementById('new-booking-btn').classList.remove('btn-unselected');
    } else {
        newBooking.style.display = 'none';
        myBookings.style.display = 'block';
        document.getElementById('my-bookings-btn').classList.add('btn-selected');
        document.getElementById('new-booking-btn').classList.remove('btn-selected');
        document.getElementById('new-booking-btn').classList.add('btn-unselected');
        document.getElementById('my-bookings-btn').classList.remove('btn-unselected');
    }
}

// Displays "New Booking" section as default
window.onload = function() {
    toggleSection('new-booking');
}

// Initialise Bootstrap Datepicker
$(document).ready(function() {
    $('#appointment-date').datepicker({
        format: 'dd-mm-yyyy',
        startDate: '0d',  // Disables past dates
        autoclose: true,
        todayHighlight: true
    });
});

// Initialises Bootstrap Datepicker
$(document).ready(function() {
    $('#datepicker').datepicker({
        format: 'dd-mm-yyyy',
        startDate: '0d',  // Disables past dates
        todayHighlight: true,
        autoclose: true
    }).on('changeDate', function(e) {
        // Saves the selected date to the hidden input field
        $('#appointment-date').val(
            $('#datepicker').datepicker('getFormattedDate')
        );
    });

    // Triggers the selection of the current date as default if necessary
    // var currentDate = $('#datepicker').datepicker('getFormattedDate');
    // if (currentDate) {
    //     $('#appointment-date').val(currentDate);
    // }
});