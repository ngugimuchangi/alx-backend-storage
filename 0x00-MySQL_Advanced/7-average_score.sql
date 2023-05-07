-- Creates procedure ComputeAverageScoreForUser
-- that computes and stores the average score of
-- a student
DELIMITER $
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    SET @average_score = (SELECT AVG(score) AS average FROM corrections
    WHERE user_id = user_id);
    UPDATE users SET average_score = @average_score WHERE id=user_id;
END$
DELIMITER ;
