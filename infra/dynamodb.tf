resource "aws_dynamodb_table" "dynamodb-task-table" {
  name           = "Tasks"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "Id"
  range_key      = "Title"

  attribute {
    name = "Id"
    type = "S"
  }

  attribute {
    name = "Title"
    type = "S"
  }

  tags = {
    Name        = "dynamodb-tasks-table"
    Environment = "dev"
  }
}
