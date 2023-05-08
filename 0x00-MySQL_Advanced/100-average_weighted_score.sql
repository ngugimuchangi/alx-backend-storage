-- Creates stored procedure ComputeAverageWeightedScoreForUser
-- that computes and stores the average weighted score for a
-- student
DELIMITER $
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weight_score FLOAT;
    DECLARE average_weight_score FLOAT;
    DECLARE project_weight INT;
    DECLARE project_score FLOAT;
    DECLARE flag INT;
    DECLARE scores_cursor CURSOR FOR (
        SELECT score, projects.weight FROM corrections
        LEFT JOIN projects ON project_id = projects.id
        WHERE corrections.user_id = user_id);
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET flag = 1;
    SET total_weight_score = 0;
    OPEN scores_cursor;
    weighted_scores_loop:
    LOOP
        FETCH scores_cursor INTO project_score, project_weight;
        IF flag = 1 THEN LEAVE weighted_scores_loop;
        END IF;
        SET @project_weight_score = project_score * project_weight;
        SET total_weight_score = total_weight_score + @project_weight_score;
    END LOOP weighted_scores_loop;
    CLOSE scores_cursor;
    SELECT SUM(projects.weight) INTO @total_projects_weight FROM projects;
    SET average_weight_score = total_weight_score / @total_projects_weight;
    UPDATE users SET average_score = average_weight_score WHERE id = user_id;
END$
DELIMITER ;
