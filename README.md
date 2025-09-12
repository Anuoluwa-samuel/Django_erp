# ERP 

ERP is a modular Enterprise Resource Planning (ERP) system built with Django and PostgreSQL.  
It is designed to unify organizational operations across multiple modules while maintaining flexibility, synchronization, and scalability.  

## 🚀 Features
- **Purchases Module**
  - Staff can create purchase requests.
  - Vendors can submit quotations.
  - Automatic creation of Purchase Orders from approved quotations.
  - Approve/Decline workflow with edit/delete functionality.

- **Inventory Module**
  - Manage products, categories, and stock levels.
  - Track staff and their assigned roles.
  - Create and monitor orders.
  - Role-based access control for staff and orders.
  - Sidebar navigation with modular templates.

- **Multi-Tenant Support**
  - Each organization runs in isolated tenant schemas.
  - Load sample data per tenant for testing.

- **Developer Friendly**
  - Dockerized setup for consistency.
  - Fixtures provided for sample data.
  - Organized module structure for scalability.

---

## 🛠️ Tech Stack
- **Backend:** Django (Python 3.12+)
- **Database:** PostgreSQL
- **Containerization:** Docker + Docker Compose
- **Frontend:** Django Templates + Bootstrap
- **Version Control:** GitHub

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/HeteroGenius01/erp_1_0/tree/Ayomide
cd erp_1_0


-------------------------------------------------------------------------------
🧪 Running Locally (without Docker)

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

-----------------------------------------------------------
📂 Project Structure


erp_1_0/
│── erp_1_0/            # Core Django project
│── purchases/          # Purchases module
│── inventory/          # Inventory module
│── templates/          # HTML templates
│── fixtures/           # Sample/test data
│── docker-compose.yml  # Docker setup
│── requirements.txt    # Dependencies
│── .env.example        # Environment variables template


-----------------------------------------------------