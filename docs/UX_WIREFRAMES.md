# UX Wireframes (Text-based)

This document describes the high-level layout and key controls for each page of the MVP.

## Global Layout
- **Sidebar (Left)**: Navigation links for Dashboard, Users, Licenses, MFA, Teams, Mailbox.
- **Topbar (Top)**: Application title, logged-in user display.
- **Content Area (Center)**: Main view for the selected page.

## Pages

### 1. Dashboard
- A grid of 5 small "stat cards".
- Each card is a placeholder for a key metric (e.g., "Total Users," "Licenses Assigned").
- No interactive elements on the cards for MVP.

### 2. Users Page
- A `<DataTable />` component displaying a list of users.
- Columns: Display Name, User Principal Name, Status.
- Controls:
    - "Add User" button (opens a modal/form - out of MVP scope).
    - "Delete User" button (actions on selected table row).

### 3. Licenses Page
- A `<DataTable />` component displaying users and their assigned licenses.
- Columns: User Principal Name, Assigned Licenses.
- Controls:
    - "Change License" dropdown/button (actions on selected table row).

### 4. MFA Page
- A `<DataTable />` component displaying users and their MFA status.
- Columns: User Principal Name, MFA Status.
- Controls:
    - "Show only disabled" filter (checkbox or toggle switch).

### 5. Teams Page
- A simple list or `<DataTable />` showing users active in Teams in the last 7 days.
- Columns: Display Name, Last Activity Date.

### 6. Mailbox Page
- A placeholder for a bar chart.
- The chart will show the Top 10 users by mailbox size.
- No actual charting library will be implemented in MVP; a static image or placeholder text is sufficient.
