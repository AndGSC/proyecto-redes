# Proyecto de Redes - Andrey Solís Carvajal, Javier Garita Granados, ...


# Checklist — Fase 0

- [ ] Definir qué cuenta de Azure manejará la infraestructura principal
- [ ] Definir qué cuenta de Azure manejará la VM de Windows Server 2016 / Active Directory
- [ ] Definir quién será la persona que se certifica
- [ ] Confirmar que ambas cuentas tienen suscripción activa
- [ ] Definir el nombre del resource group principal
- [ ] Definir si habrá colaboradores con acceso al resource group
- [ ] Registrar quién tendrá acceso y con qué rol

- [X] Crear el repositorio en GitHub
- [X] Definir el nombre final del repositorio
- [X] Elegir si el repositorio será privado o público
- [X] Inicializar el repositorio con README
- [X] Agregar colaboradores al repositorio si aplica
- [X] Crear la estructura base de carpetas del proyecto

- [ ] Generar el par de llaves SSH
- [ ] Guardar la clave privada en una ruta segura
- [ ] Verificar la ubicación de la clave pública
- [ ] Confirmar que la clave privada no se subirá al repositorio
- [ ] Documentar qué llave SSH se usará para las VMs

- [ ] Definir el dominio o subdominio que se usará para el login
- [ ] Confirmar acceso al proveedor DNS
- [ ] Confirmar que se pueden crear registros A
- [ ] Confirmar que se pueden crear registros TXT si se usa DNS-01
- [ ] Elegir el método de validación de Let’s Encrypt
- [ ] Documentar el FQDN final del proyecto

- [ ] Definir la convención de nombres para recursos en Azure
- [ ] Definir el nombre del Resource Group
- [ ] Definir el nombre de la VNet
- [ ] Definir el nombre de la Subnet
- [ ] Definir el nombre del NSG
- [ ] Definir el nombre del Load Balancer
- [ ] Definir el nombre de la Public IP
- [ ] Definir el nombre de la VM web 1
- [ ] Definir el nombre de la VM web 2
- [ ] Definir el nombre de la VM de Active Directory
- [ ] Documentar todos los nombres finales

- [ ] Definir desde dónde se ejecutará Ansible
- [ ] Confirmar si se usará laptop local con WSL o una VM de control
- [ ] Confirmar que el entorno de control tendrá acceso SSH a las VMs privadas
- [ ] Confirmar si se usará Azure Bastion
- [ ] Documentar el método de acceso administrativo

- [ ] Crear el archivo de documentación de fase 0
- [ ] Registrar responsables, cuentas y accesos
- [ ] Registrar dominio, método de validación y proveedor DNS
- [ ] Registrar nombres finales de los recursos
- [ ] Registrar la decisión del nodo de control de Ansible
- [ ] Verificar que toda la fase 0 quede escrita antes de iniciar Terraform

### 6. Ansible
- Control node: [ej. WSL Ubuntu local]
- Método de acceso: [Bastion native client]
