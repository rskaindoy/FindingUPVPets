# Finding UPV Pets

## Setup Guide

1. Install Flask (one-time setup only) by running the following command in the terminal:

   ```bash
   pip install flask
   ```

   or

   ```bash
   python3 -m pip install flask
   ```

2. Run the application using the terminal:

   ```bash
   python app.py
   ```

3. Once the server starts successfully, open the generated localhost link in a web browser (e.g., `http://127.0.0.1:5000`).

---

## Site Walkthrough

1. Upon opening the application, the user is directed to the landing page where two options are available:

   * **Report a Sighting**
   * **Find a Pet**

2. Selecting **Report a Sighting** redirects the user to the reporting page.

   * The user selects the pet seen, the location of the sighting, and the corresponding time range before submitting the report.

3. Selecting **Find a Pet** redirects the user to the search page.

   * The user selects a pet and a preferred time range to begin searching.
   * After submission, the system processes the available sighting reports and displays the results — a ranked list of locations where the selected pet is most likely to be found — within the same page.

4. The results section presents the predicted locations in order of likelihood, allowing users to quickly identify the areas where the pet has been most frequently reported.
