-- 코드를 입력하세요
SELECT ANIMAL_TYPE, IF(NAME IS NOT NULL, NAME, "No name") as "NAME", SEX_UPON_INTAKE
FROM ANIMAL_INS