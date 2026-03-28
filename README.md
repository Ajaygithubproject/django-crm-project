# ✈ ImmigrateCRM — Django Project

Immigration & Multi-Domain CRM System  
Built with Django + SQLite + openpyxl

---

## ⚡ Quick Start (3 Steps)

### Step 1 — Install requirements
```bash
pip install -r requirements.txt
```

### Step 2 — Setup database & admin user
```bash
python setup.py
```
This creates the database and the **admin** user automatically.

### Step 3 — Run the server
```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000** in your browser.  
Login: `admin` / `admin`

---

## 📁 Project Structure

```
immigratecrm/
│
├── manage.py               ← Django management
├── setup.py                ← One-click setup script
├── requirements.txt        ← pip packages
├── db.sqlite3              ← Database (auto-created)
│
├── immigratecrm/           ← Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── crm/                    ← Main CRM app
    ├── models.py           ← Database tables
    ├── views.py            ← All page logic
    ├── urls.py             ← URL routes
    ├── forms.py            ← Form definitions
    ├── admin.py            ← Django admin config
    │
    ├── templates/crm/      ← HTML templates
    │   ├── base.html
    │   ├── login.html
    │   ├── dashboard.html
    │   ├── candidates.html
    │   ├── candidate_view.html
    │   ├── candidate_edit.html
    │   ├── applications.html
    │   ├── payments.html
    │   ├── invoices.html
    │   ├── documents.html
    │   ├── courier.html
    │   ├── legal.html
    │   └── b2b.html
    │
    ├── static/crm/css/
    │   └── style.css       ← All styles
    │
    └── migrations/         ← Auto-generated DB migrations
```

---

## 🧩 Modules

| Module | URL | Description |
|--------|-----|-------------|
| Dashboard | `/` | Stats, recent applications |
| Candidates | `/candidates/` | 20-field candidate master |
| Applications | `/applications/` | Status pipeline tracking |
| Documents | `/documents/` | Document checklist & compliance |
| Courier | `/courier/` | Inward/outward register |
| Payments | `/payments/` | Payment ledger |
| Invoices | `/invoices/` | Multi-domain invoice management |
| Legal | `/legal/` | Agreements, refunds, cancellations |
| B2B Clients | `/b2b/` | Corporate client management |

---

## 📊 Excel Export / Import

- **Export**: Click **⬇ Export Excel** in the top bar → downloads `.xlsx` with all 8 sheets
- **Import**: Click **⬆ Import Excel** → upload a formatted `.xlsx` to bulk-import candidates

---

## 👤 Candidate Fields (All 20)

1. Candidate Name  
2. Phone  
3. Passport Number  
4. Country (Destination)  
5. Position / Job Role  
6. Experience  
7. Status  
8. Medical Status  
9. Visa Status  
10. Ticket Status  
11. Payment (₹)  
12. Resume  
13. Passport Copy  
14. Offer Letter  
15. Travel Date  
16. Reference  
17. Remarks  
18. Follow-up Date  
19. Staff Name  
20. Registration Date  

---

## 🔧 Change Database to MySQL (Optional)

In `immigratecrm/settings.py`, replace the DATABASES block:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'immigratecrm_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Then run:
```bash
pip install mysqlclient
python setup.py
```

---

## 🔐 Default Login
- **Username**: `admin`  
- **Password**: `admin`  

Change your password at: `http://127.0.0.1:8000/admin/`
