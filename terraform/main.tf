terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  # Credentials only needs to be set if you do not have the GOOGLE_APPLICATION_CREDENTIALS set
  # credentials =
  project = "de-zoomcamp-2026-485102"
  region  = "us-central1"
}

resource "google_storage_bucket" "data-lake-bucket" {
  name          = "de-zoomcamp-2026-485102-data-lake"
  location      = "US"

  storage_class = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30
    }
  }

  force_destroy = true
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id = "nyc_taxi"
  project    = "de-zoomcamp-2026-485102"
  location   = "US"
}