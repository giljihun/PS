-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, SUM(TOTAL_ORDER) as TOTAL_ORDER
FROM FIRST_HALF as i, ICECREAM_INFO as j
WHERE i.FLAVOR = j.FLAVOR
GROUP BY INGREDIENT_TYPE
ORDER BY TOTAL_ORDER ASC