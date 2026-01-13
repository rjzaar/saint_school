<?php
// Extract questions from the backup XML and convert to Moodle XML format
$xml = simplexml_load_file('/home/rob/saint_school/rosary_extracted/questions.xml');

$output = '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
$output .= '<quiz>' . "\n";

$question_map = [];

foreach ($xml->question_category as $category) {
    $categoryName = (string)$category->name;

    foreach ($category->questions->question as $question) {
        $qid = (string)$question['id'];
        $question_map[$qid] = [
            'name' => (string)$question->name,
            'text' => (string)$question->questiontext,
            'type' => (string)$question->qtype,
            'answers' => []
        ];

        // Add to Moodle XML format
        $output .= "  <question type=\"" . htmlspecialchars((string)$question->qtype) . "\">\n";
        $output .= "    <name>\n";
        $output .= "      <text>" . htmlspecialchars((string)$question->name) . "</text>\n";
        $output .= "    </name>\n";
        $output .= "    <questiontext format=\"html\">\n";
        $output .= "      <text><![CDATA[" . (string)$question->questiontext . "]]></text>\n";
        $output .= "    </questiontext>\n";
        $output .= "    <generalfeedback format=\"html\">\n";
        $output .= "      <text></text>\n";
        $output .= "    </generalfeedback>\n";
        $output .= "    <defaultgrade>1.0000000</defaultgrade>\n";
        $output .= "    <penalty>0.3333333</penalty>\n";
        $output .= "    <hidden>0</hidden>\n";

        if ((string)$question->qtype == 'multichoice') {
            $output .= "    <single>true</single>\n";
            $output .= "    <shuffleanswers>true</shuffleanswers>\n";
            $output .= "    <answernumbering>abc</answernumbering>\n";

            foreach ($question->answers->answer as $answer) {
                $fraction = (float)$answer->fraction;
                $fraction_percent = $fraction * 100;

                $question_map[$qid]['answers'][] = [
                    'text' => (string)$answer->answertext,
                    'fraction' => $fraction
                ];

                $output .= "    <answer fraction=\"$fraction_percent\" format=\"html\">\n";
                $output .= "      <text><![CDATA[" . (string)$answer->answertext . "]]></text>\n";
                $output .= "      <feedback format=\"html\">\n";
                $output .= "        <text><![CDATA[" . (string)$answer->feedback . "]]></text>\n";
                $output .= "      </feedback>\n";
                $output .= "    </answer>\n";
            }
        }

        $output .= "  </question>\n\n";
    }
}

$output .= '</quiz>';

file_put_contents('/home/rob/saint_school/rosary_questions.xml', $output);
file_put_contents('/home/rob/saint_school/question_map.json', json_encode($question_map, JSON_PRETTY_PRINT));

echo "Extracted " . count($question_map) . " questions\n";
echo "Saved to: rosary_questions.xml\n";
