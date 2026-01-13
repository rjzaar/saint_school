<?php
// Import quizzes into Moodle
define('CLI_SCRIPT', true);
require_once('/var/www/html/config.php');
require_once($CFG->dirroot . '/question/format.php');
require_once($CFG->dirroot . '/question/format/xml/format.php');
require_once($CFG->dirroot . '/lib/questionlib.php');
require_once($CFG->dirroot . '/mod/quiz/lib.php');

$courseid = 8;
$course = $DB->get_record('course', ['id' => $courseid], '*', MUST_EXIST);
$coursecontext = context_course::instance($courseid);

// Create question category
$qcategory = new stdClass();
$qcategory->name = 'Rosary Course Questions';
$qcategory->contextid = $coursecontext->id;
$qcategory->info = 'Questions for the Rosary course quizzes';
$qcategory->infoformat = FORMAT_HTML;
$qcategory->stamp = make_unique_id_code();
$qcategory->parent = 0;
$qcategory->sortorder = 999;
$qcategory->idnumber = null;

$categoryid = $DB->insert_record('question_categories', $qcategory);
echo "Created question category: $categoryid\n";

// Import questions from XML
$qformat = new qformat_xml();
$qformat->setCategory($DB->get_record('question_categories', ['id' => $categoryid]));
$qformat->setContexts([$coursecontext]);
$qformat->setCourse($course);
$qformat->setFilename('/home/rob/saint_school/rosary_questions.xml');
$qformat->setRealfilename('rosary_questions.xml');
$qformat->setMatchgrades('error');
$qformat->setCatfromfile(0);
$qformat->setContextfromfile(0);
$qformat->setStoponerror(1);

$xmldata = file_get_contents('/home/rob/saint_school/rosary_questions.xml');
if ($qformat->importprocess($xmldata)) {
    echo "Successfully imported questions\n";
} else {
    echo "Failed to import questions\n";
    exit(1);
}

// Get all imported questions
$questions = $DB->get_records('question', ['category' => $categoryid], 'id ASC');
echo "Found " . count($questions) . " questions\n";

// Quiz definitions
$quizzes = [
    [
        'name' => 'Quiz: The Prayers of the Rosary',
        'intro' => '<p>Test your knowledge of the prayers used in the Rosary. You may take this quiz multiple times to help memorize the prayers.</p>',
        'section' => 3,
        'questions' => array_slice(array_values($questions), 0, 8)
    ],
    [
        'name' => 'Quiz: Structure of the Rosary',
        'intro' => '<p>Test your understanding of how the Rosary is structured and how to use rosary beads.</p>',
        'section' => 4,
        'questions' => array_slice(array_values($questions), 8, 6)
    ],
    [
        'name' => 'Quiz: The Mysteries of the Rosary',
        'intro' => '<p>Test your knowledge of the four sets of mysteries and which days they are traditionally prayed.</p>',
        'section' => 5,
        'questions' => array_slice(array_values($questions), 14, 10)
    ],
    [
        'name' => 'Final Quiz: Comprehensive Review',
        'intro' => '<p>This comprehensive quiz covers all aspects of praying the Rosary. A score of 80% or higher demonstrates solid knowledge of this devotion.</p>',
        'section' => 8,
        'questions' => array_slice(array_values($questions), 24, 10)
    ]
];

// Create quizzes
foreach ($quizzes as $quizdata) {
    $quiz = new stdClass();
    $quiz->course = $courseid;
    $quiz->name = $quizdata['name'];
    $quiz->intro = $quizdata['intro'];
    $quiz->introformat = FORMAT_HTML;
    $quiz->timeopen = 0;
    $quiz->timeclose = 0;
    $quiz->timelimit = 0;
    $quiz->overduehandling = 'autosubmit';
    $quiz->graceperiod = 0;
    $quiz->preferredbehaviour = 'deferredfeedback';
    $quiz->canredoquestions = 0;
    $quiz->attempts = 0;
    $quiz->attemptonlast = 0;
    $quiz->grademethod = 1;
    $quiz->decimalpoints = 2;
    $quiz->questiondecimalpoints = -1;
    $quiz->reviewattempt = 69904;
    $quiz->reviewcorrectness = 4368;
    $quiz->reviewmarks = 4368;
    $quiz->reviewspecificfeedback = 4368;
    $quiz->reviewgeneralfeedback = 4368;
    $quiz->reviewrightanswer = 4368;
    $quiz->reviewoverallfeedback = 4368;
    $quiz->questionsperpage = 1;
    $quiz->navmethod = 'free';
    $quiz->shuffleanswers = 1;
    $quiz->sumgrades = count($quizdata['questions']);
    $quiz->grade = 100;
    $quiz->timecreated = time();
    $quiz->timemodified = time();
    $quiz->password = '';
    $quiz->subnet = '';
    $quiz->browsersecurity = '-';
    $quiz->delay1 = 0;
    $quiz->delay2 = 0;
    $quiz->showuserpicture = 0;
    $quiz->showblocks = 0;
    $quiz->completionattemptsexhausted = 0;
    $quiz->completionminattempts = 0;
    $quiz->allowofflineattempts = 0;

    $quizid = quiz_add_instance($quiz);

    if ($quizid) {
        echo "Created quiz: {$quiz->name} (ID: $quizid)\n";

        // Add course module
        $cm = new stdClass();
        $cm->course = $courseid;
        $cm->module = $DB->get_field('modules', 'id', ['name' => 'quiz']);
        $cm->instance = $quizid;
        $cm->section = $DB->get_field('course_sections', 'id', ['course' => $courseid, 'section' => $quizdata['section']]);
        $cm->visible = 1;
        $cm->visibleoncoursepage = 1;
        $cm->added = time();

        $cmid = $DB->insert_record('course_modules', $cm);
        echo "Created course module (ID: $cmid)\n";

        // Add to section sequence
        $section = $DB->get_record('course_sections', ['id' => $cm->section]);
        if ($section->sequence) {
            $section->sequence .= ',' . $cmid;
        } else {
            $section->sequence = $cmid;
        }
        $DB->update_record('course_sections', $section);

        // Add questions to quiz
        $slot = 1;
        foreach ($quizdata['questions'] as $question) {
            quiz_add_quiz_question($question->id, $quiz, $slot, 1);
            $slot++;
        }

        quiz_update_sumgrades($quiz);
        echo "Added " . count($quizdata['questions']) . " questions to quiz\n\n";
    }
}

echo "Done! All quizzes created successfully.\n";
