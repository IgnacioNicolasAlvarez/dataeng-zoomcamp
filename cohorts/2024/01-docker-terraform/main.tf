terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.12.0"
    }
  }
}

provider "google" {
  project     = var.project_id
  region      = var.region
  credentials = file(var.credentials)
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "data_enginnering_course_demo_bucket"
  location      = var.gcs_bucket_location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}


resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id                  = "data_enginnering_course_demo_dataset"
  friendly_name               = var.bq_dataset_name
  location                    = var.bq_dataset_location
  default_table_expiration_ms = 3600000
}