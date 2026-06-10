# Agri_shop: Agricultural E-Commerce Platform

## Overview
Agri_shop is a dual-user web application built with Django that bridges the gap between farmers and consumers. It provides a secure, role-based platform where farmers can directly list their agricultural products, and public users can browse, purchase, and track their orders.

## Tech Stack
* **Backend:** Python, Django
* **Database:** SQLite
* **Frontend:** HTML, Bootstrap 5 (Crispy Forms)

## Key Features
* **Role-Based Authentication:** Distinct login and dashboard routing for Farmers and Public Users.
* **Farmer Dashboard:** Full CRUD (Create, Read, Update, Delete) functionality for farmers to manage their product inventory and track incoming orders.
* **Secure Checkout System:** Integrated order processing with dynamic Order ID generation (UUID) and multiple simulated payment methods (UPI, Netbanking, Credit Card, Cash on Delivery).
* **Automated Image Handling:** Backend logic utilizing Pillow (PIL) to automatically resize user and product image uploads to optimize database storage.
* **Custom Data Validation:** Robust backend form validation to ensure unique usernames, emails, phone numbers, and correct payment formatting.
