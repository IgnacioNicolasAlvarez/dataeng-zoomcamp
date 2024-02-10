CREATE TABLE
  `data-enginnering-course.data_enginnering_course_demo_dataset.native_partitioned_green_tripdata_2022`
PARTITION BY
  DATE(lpep_pickup_datetime)
CLUSTER BY
  PUlocationID AS
SELECT
  *
FROM
  `data-enginnering-course.data_enginnering_course_demo_dataset.native_green_tripdata_2022`