-- Creates stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and stores the average weighted score for all
-- students
DELIMITER $
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE student_id INT;
    DECLARE students_flag INT DEFAULT FALSE;
    DECLARE students_cursor CURSOR FOR (
        SELECT id from users);
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET students_flag = TRUE;
    OPEN students_cursor;
    students_loop:
    LOOP
        FETCH students_cursor INTO student_id;
        IF students_flag THEN LEAVE students_loop;
        END IF;
        BEGIN
            DECLARE total_weight_score FLOAT;
            DECLARE average_weight_score FLOAT;
            DECLARE project_weight INT;
            DECLARE project_score FLOAT;
            DECLARE scores_flag INT DEFAULT FALSE;
            DECLARE scores_cursor CURSOR FOR (
                SELECT score, projects.weight FROM corrections
                LEFT JOIN projects ON project_id = projects.id
                WHERE corrections.user_id = student_id);
            DECLARE CONTINUE HANDLER FOR NOT FOUND SET scores_flag = TRUE;
            SET total_weight_score = 0;
            OPEN scores_cursor;
            weighted_scores_loop:
            LOOP
                FETCH scores_cursor INTO project_score, project_weight;
                IF scores_flag THEN LEAVE weighted_scores_loop;
                END IF;
                SET @project_weight_score = project_score * project_weight;
                SET total_weight_score = total_weight_score + @project_weight_score;
            END LOOP weighted_scores_loop;
            CLOSE scores_cursor;
            SELECT SUM(projects.weight) INTO @total_projects_weight FROM projects;
            SET average_weight_score = total_weight_score / @total_projects_weight;
            UPDATE users SET average_score = average_weight_score WHERE id = student_id;
        END;
    END LOOP students_loop;
END$
DELIMITER ;
