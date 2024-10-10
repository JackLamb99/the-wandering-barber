# The Wandering Barber

'The Wandering Barber' is an online booking system that allows users to book appointments for various grooming services, manage their existing appointments, and contact the barber shop for inquiries. The system supports user and staff accounts with features like appointment booking, editing, and cancellation. Users can also update their account details or delete their accounts.

## Features

### Site Wide

#### Navbar

The navigation menu contains links to the 'Bookings', 'My Account', and 'Contact' pages. It is responsive and collapses into a hamburger menu on smaller devices.
Users can easily navigate between pages and see clear indicators for their current page.

![Navbar](docs\readme_images\navbar-large.jpg)

![Navbar - Mobile](docs\readme_images\navbar-mobile.jpg)

### Bookings Page

#### Booking Form

- Users can select a date, time, and optional services to book an appointment. The form also collects address details.
- Time slots that have been booked are visually disabled and unclickable to prevent double booking.

![Booking Form](docs\readme_images\booking-form.jpg)

#### My Bookings Section

- Users can view, edit, and cancel their upcoming appointments.
- Staff users can see all future appointments across users.
- Canceled appointments free up time slots for future bookings.

![My Bookings](docs\readme_images\my-bookings.jpg)

### My Account Page

- Users can view their personal details and update their first name and last name.
- Users can delete their account with a confirmation prompt. If they delete their account, it is marked as inactive in the backend.

![My Account](docs\readme_images\my-account.jpg)

### Contact Page

- Users can fill out a form to send inquiries to the owner.
- Logged-in users have their name and email auto-filled. Non-logged-in users must manually input their details.

![Contact](docs\readme_images\contact.jpg)

## Design

### Typography

The website uses the 'Libre Baskerville' font for headers and 'Open Sans' for body text, ensuring readability and a clean, modern look.

### Colour Palette

The site's colour palette is based on muted tones of green and gray, with vibrants elements of dark gold, providing a calming and professional feel.

![Colour Palette](docs\readme_images\colour-pallett.png)

## Technologies

- Django: Used to develop the backend and user authentication system.
- HTML/CSS/JavaScript: Used for the structure and styling of the front end.
- Bootstrap: Integrated for responsive design and UI elements.
- jQuery: Used to handle modal and form submissions.
- SQLite: Database for storing user and appointment data during development.

## Testing

### Manual Testing

#### Booking Form

Test: Select a date, time, and services to book an appointment.

Steps:
1. Open the bookings page.
2. Select a date.
3. Choose an available time slot.
4. Add any optional services.
5. Fill in the address details and submit.

Expected Result: Appointment is created, and the confirmation modal shows.

Actual Result: The system behaves as expected.

#### Appointment Editing and Cancellation

Test: Edit an appointment.

Steps:
1. Open 'My Bookings'.
2. Click 'Edit' on an appointment.
3. Change the optional services and save.

Expected Result: The appointment is updated.

Actual Result: The system behaves as expected.

Test: Cancel an appointment.

Steps:
1. Open 'My Bookings'.
2. Click 'Cancel' on an appointment.
3. Confirm cancellation in the modal.

Expected Result: Appointment is removed from the list and marked as canceled in the database.

Actual Result: The system behaves as expected.

#### Account Details Editing

Test: Edit first name and last name on the account page.

Steps:
1. Open 'My Account'.
2. Change the first name and/or last name and click save.

Expected Result: The account details are updated.

Actual Result: The system behaves as expected.

Test: Delete the account.

Steps:
Click the 'Delete Account' button.
Confirm the deletion in the modal.
Expected Result: The account is deactivated, and the user is logged out.
Actual Result: The system behaves as expected.

#### Contact Form

Test: Submit an inquiry.

Steps:
1. Open the contact page.
2. Fill in the form with valid data and submit.

Expected Result: An email is sent to the shop.

Actual Result: The system behaves as expected.

#### Functional Testing

Navigation Links

- Test all navigation links to ensure they direct to the correct pages.
  - Expected: All links function as expected.

Form Validation

- Test form validation for the booking and contact forms.
  - Expected: Forms do not submit if required fields are missing.

### Validator Testing

#### HTML

No errors were found when running the HTML files through the W3C validator.

#### CSS

The CSS files passed through the W3C CSS validator with no errors.

## Deployment

### Version Control

- The project was developed using Git for version control and GitHub as the repository.
- Git commands used: git add, git commit, git push.

### Deployment Steps
- Push the code to GitHub.
- Set up Django’s production settings.
- Deploy to Heroku.

## Credits

### Content

- User authentication system based on the Django documentation.

### Media

- Images for the site were sourced from Unsplash.