SELECT
  COUNT(*) AS row_count
FROM
  `data-enginnering-course.data_enginnering_course_demo_dataset.native_green_tripdata_2022`
WHERE
  fare_amount = 0