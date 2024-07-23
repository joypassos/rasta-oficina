output "vcn_id" {
  value = oci_core_vcn.my_vcn.id
}

output "subnet_id" {
  value = oci_core_subnet.my_subnet.id
}

output "instance_public_ip" {
  value = oci_core_instance.my_instance.public_ip
}

output "autonomous_db_id" {
  value = oci_database_autonomous_database.my_autonomous_db.id
}

output "bucket_name" {
  value = oci_objectstorage_bucket.my_bucket.name
}

output "load_balancer_id" {
  value = oci_load_balancer_load_balancer.my_load_balancer.id
}
