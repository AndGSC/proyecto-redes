output "vm_private_ips" {
  value = [
    azurerm_network_interface.nic1.private_ip_address,
    azurerm_network_interface.nic2.private_ip_address
  ]
}

output "lb_public_ip" {
  value = azurerm_public_ip.lb_ip.ip_address
}

output "vm1_public_ip" {
  value = azurerm_public_ip.vm1_ip.ip_address
}

output "vm2_public_ip" {
  value = azurerm_public_ip.vm2_ip.ip_address
}
