# Create VCN
resource "oci_core_vcn" "my_vcn" {
  cidr_block     = var.vcn_cidr
  display_name   = "my_vcn"
  compartment_id = var.compartment_ocid
}

# Create Subnet
resource "oci_core_subnet" "my_subnet" {
  cidr_block       = var.subnet_cidr
  vcn_id           = oci_core_vcn.my_vcn.id
  display_name     = "my_subnet"
  compartment_id   = var.compartment_ocid
  prohibit_public_ip_on_vnic = false
}

# Create Compute Instance
resource "oci_core_instance" "my_instance" {
  availability_domain = data.oci_identity_availability_domains.ads.availability_domains[0].name
  compartment_id      = var.compartment_ocid
  display_name        = "my_instance"
  shape               = var.compute_shape

  source_details {
    source_type = "image"
    source_id   = var.compute_image
  }

  create_vnic_details {
    subnet_id        = oci_core_subnet.my_subnet.id
    assign_public_ip = true
  }

  metadata = {
    ssh_authorized_keys = file("~/.ssh/id_rsa.pub")
  }
}

# Create Autonomous Database
resource "oci_database_autonomous_database" "my_autonomous_db" {
  compartment_id = var.compartment_ocid
  db_name        = var.autonomous_db_name
  admin_password = var.autonomous_db_password
  cpu_core_count = 1
  data_storage_size_in_tbs = 1
  display_name   = "my_autonomous_db"
  db_workload    = "OLTP"
}

# Create Object Storage Bucket
resource "oci_objectstorage_bucket" "my_bucket" {
  compartment_id = var.compartment_ocid
  name           = "my_bucket"
  storage_tier   = "Standard"
}

# Create Load Balancer
resource "oci_load_balancer_load_balancer" "my_load_balancer" {
  compartment_id = var.compartment_ocid
  display_name   = "my_load_balancer"
  shape_name     = var.load_balancer_shape

  subnet_ids = [oci_core_subnet.my_subnet.id]

  backend_sets {
    name = "backend_set_1"
    policy = "ROUND_ROBIN"

    backends {
      ip_address = oci_core_instance.my_instance.public_ip
      port = 80
    }

    health_checker {
      protocol = "HTTP"
      url_path = "/"
      retries = 3
      timeout_in_ms = 3000
      interval_in_ms = 10000
      port = 80
    }
  }

  listeners {
    name           = "listener_1"
    default_backend_set_name = "backend_set_1"
    protocol       = "HTTP"
    port           = 80
  }
}
