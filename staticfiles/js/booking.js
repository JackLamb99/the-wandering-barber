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

// Initialises total variables
let totalPrice = 45; // Starts with the haircut price as minimum service
let totalDuration = 90; // Starts with the haircut duration as minimum service

function toggleServiceCheckbox(checkbox) {
    const servicePrice = parseFloat(checkbox.getAttribute('data-price'));
    const serviceDuration = parseInt(checkbox.getAttribute('data-duration'));

    // Updates the total when a service checkbox is checked or unchecked
    if (checkbox.checked) {
        totalPrice += servicePrice;
        totalDuration += serviceDuration;
    } else {
        totalPrice -= servicePrice;
        totalDuration -= serviceDuration;
    }

    // Updates the hidden input fields with the new totals
    $('#total_price').val(totalPrice);
    $('#total_duration').val(totalDuration);

    // Styles the service checkboxes to reflect the selected state
    if (checkbox.checked) {
        checkbox.parentElement.classList.add('service-selected');
        checkbox.parentElement.classList.remove('service-unselected');
    } else {
        checkbox.parentElement.classList.remove('service-selected');
        checkbox.parentElement.classList.add('service-unselected');
    }
}

// Initialises total values based on initial selections when the page loads
function initialiseTotals() {
    totalPrice = 45; // Haircut price
    totalDuration = 90; // Haircut duration

    // Calculates totals for initially selected optional services (excluding default haircut)
    $('input[name="selected_services"]:checked:not([disabled])').each(function() {
        totalPrice += parseFloat($(this).attr('data-price'));
        totalDuration += parseInt($(this).attr('data-duration'));
    });

    // Set the values in the hidden inputs
    $('#total_price').val(totalPrice);
    $('#total_duration').val(totalDuration);
}

// Displays "New Booking" section as default
window.onload = function() {
    toggleSection('new-booking');
}

$(document).ready(function() {
    // Calls initialiseTotals function when page loads
    initialiseTotals();

    $('#datepicker').datepicker({
        format: 'dd-mm-yyyy',
        startDate: '0d',  // Disables past dates
        todayHighlight: true,
        autoclose: true
    }).on('changeDate', function(e) {
        // Saves the selected date to the hidden input field
        let selectedDate = $('#datepicker').datepicker('getFormattedDate');
        $('#appointment-date').val(selectedDate);

        // AJAX call to check available time slots
        $.get('/book/', { appointment_date: selectedDate }, function(response) {
            $('select[name="selected_time"]').html('');

            // Add available time slots (clickable)
            response.available_time_slots.forEach(function(time) {
                $('select[name="selected_time"]').append(`<option value="${time}">${time}</option>`);
            });

            // Disables booked time slots
            response.booked_time_slots.forEach(function(time) {
                $('select[name="selected_time"]').append(`<option value="${time}" disabled style="color: red;">${time} (Unavailable)</option>`);
            });

            // Provides feedback if there are no available time slots
            if (response.available_time_slots.length === 0) {
                $('select[name="selected_time"]').append(`<option value="" disabled>No available time slots for this date</option>`);
            }
        });
    });

    // Handles Confirm Details button click
    $('#confirm-details-btn').click(function(event) {
        event.preventDefault(); // Prevents automatic form submission

        // Gathers appointment details
        const address1 = $('input[name="address"]').val();
        const address2 = $('input[name="address2"]').val();
        const city = $('input[name="city"]').val();
        const postcode = $('input[name="postcode"]').val();

        // Creates address string, including optional Address 2 if added
        const addressString = address2 ? `${address1}, ${address2}, ${city}, ${postcode}` : `${address1}, ${city}, ${postcode}`;

        // Gets total price and duration from hidden inputs
        const totalPrice = $('#total_price').val();
        const totalDuration = $('#total_duration').val();

        const appointmentDetails = `
        <li>Date: ${$('#appointment-date').val()}</li>
        <li>Time: ${$('select[name="selected_time"]').val()}</li>
        <li>Services: ${Array.from($('input[name="selected_services"]:checked'))
            .map(el => $(el).parent().text().trim())
            .join(', ')}
        </li>
        <li>Address: ${addressString}</li>
        <li>Total Price: £${totalPrice}</li>
        <li>Total Duration: ${totalDuration} mins</li>
        `;

        // Populates the appointment details in the modal
        $('#appointment-details').html(appointmentDetails);

        // Shows the modal
        $('#confirmationModal').modal('show');
    });

    // Resets the booking form, called when the Cancel Booking button is clicked on the modal
    function resetBookingForm() {
        // Resets the entire form
        $('form')[0].reset();

        // Resets services to default Haircut and removes selected states from optional services
        $('input[name="selected_services"]').each(function() {
            if (!this.disabled) { // Excludes the disabled haircut service
                this.checked = false;
                $(this).parent().removeClass('service-selected').addClass('service-unselected');
            }
        });

        // Resets total price and duration
        totalPrice = 45;
        totalDuration = 90;

        // Updates the hidden total fields
        $('#total_price').val(totalPrice);
        $('#total_duration').val(totalDuration);

        // Clears the date and time selections
        $('#appointment-date').val('');
        $('select[name="selected_time"]').val('');

        // Resets the datepicker
        $('#datepicker').datepicker('clearDates');
    }

    // Cancel Booking button functionality to close the modal and clear the booking form
    $('#cancel-booking').click(function() {
        resetBookingForm();
        $('#confirmationModal').modal('hide');
    });

    // Confirm Booking button functionality to submit the appointment
    $('#confirm-booking').click(function() {
        $('#booking-form').off('submit').submit();
    });

    // Edit Details button functionality to close the modal and allow users to edit details
    $('#edit-details').click(function() {
        $('#confirmationModal').modal('hide');
    });
});
