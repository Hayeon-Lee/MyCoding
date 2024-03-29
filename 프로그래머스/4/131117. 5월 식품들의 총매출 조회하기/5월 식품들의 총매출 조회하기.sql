-- 코드를 입력하세요
SELECT 
    A.PRODUCT_ID AS 'PRODUCT_ID',
    A.PRODUCT_NAME AS 'PRODUCT_NAME',
    SUM((A.PRICE * B.AMOUNT))AS 'TOTAL_SALES'
FROM FOOD_PRODUCT AS A
LEFT JOIN FOOD_ORDER AS B
ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE YEAR(B.PRODUCE_DATE) = 2022 AND MONTH(B.PRODUCE_DATE) = 5
GROUP BY PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID ASC;