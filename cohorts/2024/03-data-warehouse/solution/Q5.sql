SELECT
  COUNT(DISTINCT PULocationID)
FROM
  `data-enginnering-course.data_enginnering_course_demo_dataset.native_green_tripdata_2022`
WHERE
  DATE(lpep_pickup_datetime) BETWEEN PARSE_DATE('%m/%d/%Y','06/01/2022')
  AND PARSE_DATE('%m/%d/%Y','06/30/2022')