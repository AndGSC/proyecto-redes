variable "subscription_id" {
  type = string
}

variable "location" {
  default = "West US"
}

variable "resource_group" {
  default = "RedesProject"
}

variable "admin_user" {
  default = "RedesProject"
}

variable "ssh_key" {
  type = string
}
