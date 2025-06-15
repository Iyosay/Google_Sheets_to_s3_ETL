#Create s3 bucket
resource "aws_s3_bucket" "googlesheet_DE_Biodata" {
  bucket = "googlesheet-de-biodata"

  tags = {
    Name        = "Joy"
    Environment = "Production"
  }
}
