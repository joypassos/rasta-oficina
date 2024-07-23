variable "tenancy_ocid" {}
variable "user_ocid" {}
variable "fingerprint" {}
variable "private_key_path" {}
variable "region" {
  default = "us-ashburn-1"
}
variable "compartment_ocid" {}

# VCN Variables
variable "vcn_cidr" {
  default = "10.0.0.0/16"
}
variable "subnet_cidr" {
  default = "10.0.1.0/24"
}

# Compute Variables
variable "compute_shape" {
  default = "VM.Standard2.1"
}
variable "compute_image" {
  default = "ocid1.image.oc1.iad.aaaaaaaaexample"
}

# Autonomous Database Variables
variable "autonomous_db_name" {
  default = "myadb"
}
variable "autonomous_db_password" {
  default = "MyDBPassword123"
}

# Load Balancer Variables
variable "load_balancer_shape" {
  default = "100Mbps"
}
