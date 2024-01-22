variable "bq_dataset_name" {
  type    = string
  default = "demo-dataset"
}

variable "bq_dataset_location" {
  type    = string
  default = "US"
}

variable "gcs_bucket_class" {
  type    = string
  default = "STANDARD"
}

variable "gcs_bucket_location" {
  type    = string
  default = "US"
}

variable "gcs_bucket_name" {
  type    = string
  default = "demo-bucket"
}

variable "project_id" {
  type    = string
  default = "data-enginnering-course"
}

variable "region" {
  type    = string
  default = "us-central1"
}

variable "credentials" {
  type    = string
  default = "./data-enginnering-course-e9aae39eaf45.json"
}