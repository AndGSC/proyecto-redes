# Proyecto Redes 2026
**EIF-208 Comunicaciones y Redes — I Ciclo 2026**

Implementación de infraestructura en la nube con Azure, dividida en dos partes: un sitio web seguro con autenticación via Active Directory, y una aplicación contenerizada con pipeline de CI/CD automatizado.

---

## Estructura del repositorio

```
proyecto-redes/
├── Codigo_Terraform_Linux/    # Parte 1 — infraestructura con Terraform
│   └── RedesProject/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       └── terraform.tfvars
├── ansible-nginx-ad/          # Parte 1 — configuración de servidores con Ansible
│   ├── playbook.yml
│   ├── inventory.ini
│   ├── files/
│   └── templates/
└── parte2/                    # Parte 2 — app contenerizada con CI/CD
    ├── app/
    │   ├── app.py
    │   └── templates/
    ├── requirements.txt
    ├── Dockerfile
    └── k8s/
```

---

## Parte 1 — Sitio web seguro con Active Directory

### Descripción
Tres máquinas virtuales en Azure: dos servidores web Linux con NGINX y una VM Windows Server con Active Directory. El tráfico se balancea entre los dos servidores web mediante Azure Load Balancer. El acceso es únicamente por HTTPS con certificado digital.

### Requisitos
- Terraform >= 1.0
- Ansible >= 2.9
- Azure CLI
- Cuenta de Azure for Students activa

### Cómo ejecutar

**1. Iniciar sesión en Azure**
```bash
az login
```

**2. Desplegar la infraestructura con Terraform**
```bash
cd Codigo_Terraform_Linux/RedesProject
terraform init
terraform plan
terraform apply
```

Esto crea las 3 VMs, el Load Balancer, la red virtual y los grupos de seguridad.

**3. Configurar los servidores web con Ansible**

Actualiza las IPs en `ansible-nginx-ad/inventory.ini` con las IPs públicas que generó Terraform, luego:
```bash
cd ansible-nginx-ad
ansible-playbook -i inventory.ini playbook.yml
```

Esto instala NGINX, Flask, configura HTTPS y conecta la app con Active Directory.

**4. Acceder al sitio**
```
https://<IP_PUBLICA_LOAD_BALANCER>
```

---

## Parte 2 — Aplicación contenerizada con CI/CD

### Descripción
Aplicación web Flask empaquetada en Docker, publicada en Azure Container Registry y desplegada en Azure Container Instances. El pipeline de GitHub Actions construye y despliega automáticamente con cada push a `main`.

### Requisitos
- Python 3.11+
- Docker Desktop
- Azure CLI

### Cómo ejecutar localmente

```bash
cd parte2
python -m venv venv

# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
python app/app.py
```

Abrir en el navegador: `http://localhost:5000`

### Cómo ejecutar con Docker

```bash
cd parte2
docker build -t mi-app:local .
docker run -p 5000:5000 mi-app:local
```

Abrir en el navegador: `http://localhost:5000`

### App en producción

La aplicación está desplegada en Azure y accesible en:
```
http://mi-app-mariela2026.eastus.azurecontainer.io:5000
```

### Pipeline CI/CD

Cada push a `main` con cambios en `parte2/` activa automáticamente el pipeline que:
1. Construye la imagen Docker
2. La publica en Azure Container Registry
3. Redespliega el contenedor en Azure Container Instances

Ver el historial de ejecuciones en: **GitHub → Actions**
