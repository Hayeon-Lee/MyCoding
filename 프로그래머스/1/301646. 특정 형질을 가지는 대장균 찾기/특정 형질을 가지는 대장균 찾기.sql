-- 코드를 작성해주세요
SELECT COUNT(DISTINCT ID) AS COUNT FROM ECOLI_DATA
WHERE
    GENOTYPE&5>0 AND
    GENOTYPE&5 = GENOTYPE&7