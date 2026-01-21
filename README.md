# SDLC-of-a-movie-theatre
This **README** is designed to document the full SDLC and architectural specifications of the **Cinema Booking System (CBS)**. To maintain technical integrity, all nomenclatures defined in the design phase are mirrored exactly in the implementation.

---

# Cinema Booking System (CBS) - Project Report

## 1. SDLC Phase 1: Requirements Analysis

The goal of the **CBS** is to manage movie screenings and seat inventory.

* **Stakeholders:** Cinema Managers and Customers.
* **Constraints:** Prevent overbooking; maintain a clear link between a specific movie and its scheduled time.

## 2. SDLC Phase 2: System Design

The system uses a modular, Object-Oriented approach. The following **Nomenclatures** are defined for the architecture:

* **`Movie`**: Data object containing `title` and `genre`.
* **`ShowTime`**: The core engine that manages `available_seats` for a specific `Movie` at a specific `time`.
* **`CinemaBookingSystem`**: The controller class that handles the `movies_catalog` and `scheduled_shows`.
* **`process_booking`**: The primary method responsible for seat validation and deduction.

---

## 3. SDLC Phase 3: Implementation
./movie.py

## 4. SDLC Phase 4: Testing

Verification was performed using the following test cases:

1. **Positive Case:** `process_booking(4)` on a capacity of 100 correctly returns `True` and leaves 96 seats.
2. **Negative Case:** Requesting more seats than `available_seats` correctly returns `False`.
3. **Integrity Check:** The `movie` object inside `ShowTime` correctly references the `Movie` instance title.

## 5. SDLC Phase 5: Deployment & Maintenance

* **Deployment:** This system is ready to be wrapped in a CLI or a Flask-based Web API.
* **Maintenance:** Future updates will include a `SeatMap` nomenclature to track specific seat coordinates (e.g., Row A, Seat 5).

---

### Project Metadata

* **Version:** 1.0.0
* **Model:** Waterfall SDLC
* **Status:** Implementation Complete
