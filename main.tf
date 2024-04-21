terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws" 
            version = "5.31.0"
        }
    }
}

provider "aws" {
    region = "us-west-1"
}

resource "aws_s3_bucket" "grasshopper-cdn" {
    bucket = "grasshopper-cdn"
}

resource "aws_s3_bucket_cors_configuration" "grasshopper-cdn" {
    bucket = aws_s3_bucket.grasshopper-cdn.id
    
    cors_rule {
        allowed_headers = ["*"]
        allowed_methods = ["PUT", "GET"]
        allowed_origins = ["*"]
    }
}

