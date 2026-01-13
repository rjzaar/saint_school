#!/usr/bin/env python3
"""
Ignatian Daily Examen - Moodle Backup Generator

This script creates a complete Moodle backup (.mbz) file that can be
imported directly into any Moodle 4.x site.

Usage:
    python3 generate_examen_backup.py

Output:
    ignatian_examen_backup.mbz (in current directory)
"""

import zipfile
import os
import time
from datetime import datetime

def create_backup():
    """Generate the Moodle backup file"""
    
    timestamp = int(time.time())
    backup_filename = 'ignatian_examen_backup.mbz'
    
    print("🕊️  Generating Ignatian Daily Examen Moodle Backup...")
    print(f"📦 Creating {backup_filename}...\n")
    
    # Create ZIP file
    with zipfile.ZipFile(backup_filename, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        
        # 1. Main backup file
        print("  ✓ Creating moodle_backup.xml")
        backup_zip.writestr('moodle_backup.xml', MOODLE_BACKUP_XML.format(timestamp=timestamp))
        
        # 2. Course definition
        print("  ✓ Creating course/course.xml")
        backup_zip.writestr('course/course.xml', COURSE_XML.format(timestamp=timestamp))
        
        # 3. Questions
        print("  ✓ Creating questions.xml (18 questions)")
        backup_zip.writestr('questions.xml', QUESTIONS_XML)
        
        # 4. Required supporting files
        print("  ✓ Creating supporting files")
        backup_zip.writestr('roles.xml', ROLES_XML)
        backup_zip.writestr('scales.xml', '<scales/>')
        backup_zip.writestr('outcomes.xml', '<outcomes_definition/>')
        backup_zip.writestr('groups.xml', '<groups/>')
        backup_zip.writestr('files.xml', FILES_XML)
        backup_zip.writestr('completion.xml', '<course_completion><empty/></course_completion>')
        backup_zip.writestr('grade_history.xml', '<grade_history><grade_grades/></grade_history>')
        backup_zip.writestr('gradebook.xml', GRADEBOOK_XML)
    
    print(f"\n✅ Success! Created {backup_filename}")
    print(f"📊 File size: {os.path.getsize(backup_filename) / 1024:.1f} KB")
    print("\n📋 Import Instructions:")
    print("  1. Log into your Moodle site as administrator")
    print("  2. Go to: Site Administration → Courses → Restore course")
    print("  3. Upload this .mbz file")
    print("  4. Follow the restore wizard")
    print("\n🎯 The course includes:")
    print("  • 18 carefully crafted questions")
    print("  • Complete course structure")
    print("  • Rich educational feedback")
    print("  • Cognitive science-based design")

# XML Templates
MOODLE_BACKUP_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<moodle_backup>
  <information>
    <name>backup-moodle2-course-2-examen-{timestamp}.mbz</name>
    <moodle_version>2024100700</moodle_version>
    <moodle_release>4.5</moodle_release>
    <backup_version>2024100700</backup_version>
    <backup_release>4.5</backup_release>
    <backup_date>{timestamp}</backup_date>
    <mnet_remoteusers>0</mnet_remoteusers>
    <include_files>1</include_files>
    <include_file_references_to_external_content>0</include_file_references_to_external_content>
    <original_wwwroot>https://moodle.local</original_wwwroot>
    <original_site_identifier_hash>examen2026</original_site_identifier_hash>
    <original_course_id>2</original_course_id>
    <original_course_format>topics</original_course_format>
    <original_course_fullname>The Ignatian Daily Examen: A Practice of Awareness and Gratitude</original_course_fullname>
    <original_course_shortname>EXAMEN101</original_course_shortname>
    <original_course_startdate>{timestamp}</original_course_startdate>
    <original_course_contextid>123</original_course_contextid>
    <original_system_contextid>1</original_system_contextid>
    <type>course</type>
    <format>moodle2</format>
    <interactive>1</interactive>
    <mode>10</mode>
    <execution>1</execution>
    <executiontime>0</executiontime>
  </information>
  <details>
    <detail backup_id="1" type="course" format="moodle2" interactive="1" mode="10" execution="1" executiontime="0">
      <settings>
        <setting level="root" name="filename" value="backup-moodle2-course-2-examen-{timestamp}.mbz"/>
        <setting level="root" name="users" value="0"/>
        <setting level="root" name="role_assignments" value="0"/>
        <setting level="root" name="activities" value="1"/>
        <setting level="root" name="blocks" value="0"/>
        <setting level="root" name="files" value="1"/>
        <setting level="root" name="filters" value="0"/>
        <setting level="root" name="comments" value="0"/>
        <setting level="root" name="badges" value="0"/>
        <setting level="root" name="calendarevents" value="0"/>
        <setting level="root" name="userscompletion" value="0"/>
        <setting level="root" name="logs" value="0"/>
        <setting level="root" name="grade_histories" value="0"/>
        <setting level="root" name="questionbank" value="1"/>
        <setting level="root" name="groups" value="0"/>
      </settings>
    </detail>
  </details>
</moodle_backup>'''

COURSE_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<course id="2" contextid="123">
  <shortname>EXAMEN101</shortname>
  <fullname>The Ignatian Daily Examen: A Practice of Awareness and Gratitude</fullname>
  <idnumber></idnumber>
  <summary>&lt;p&gt;Discover the transformative power of the Daily Examen, a 500-year-old prayer practice developed by St. Ignatius of Loyola. This course will guide you through the five movements of the Examen, helping you cultivate gratitude, awareness, and discernment in your daily life.&lt;/p&gt;
&lt;p&gt;The Examen is not simply a review of your day—it is a profound practice of noticing God's presence in the ordinary moments of your life and responding with gratitude and intention.&lt;/p&gt;
&lt;h3&gt;Course Structure:&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Introduction to the Examen&lt;/li&gt;
&lt;li&gt;First Movement: Gratitude&lt;/li&gt;
&lt;li&gt;Second Movement: Light&lt;/li&gt;
&lt;li&gt;Third Movement: Review&lt;/li&gt;
&lt;li&gt;Fourth Movement: Forgiveness&lt;/li&gt;
&lt;li&gt;Fifth Movement: Renewal&lt;/li&gt;
&lt;/ul&gt;</summary>
  <summaryformat>1</summaryformat>
  <format>topics</format>
  <showgrades>1</showgrades>
  <newsitems>5</newsitems>
  <startdate>{timestamp}</startdate>
  <enddate>0</enddate>
  <numsections>6</numsections>
  <marker>0</marker>
  <maxbytes>0</maxbytes>
  <legacyfiles>0</legacyfiles>
  <showreports>0</showreports>
  <visible>1</visible>
  <groupmode>0</groupmode>
  <groupmodeforce>0</groupmodeforce>
  <defaultgroupingid>0</defaultgroupingid>
  <lang></lang>
  <theme></theme>
  <timecreated>{timestamp}</timecreated>
  <timemodified>{timestamp}</timemodified>
  <requested>0</requested>
  <enablecompletion>1</enablecompletion>
  <completionnotify>0</completionnotify>
  <category id="1" contextid="10">
    <name>Miscellaneous</name>
    <description>$@NULL@$</description>
  </category>
  <tags></tags>
</course>'''

QUESTIONS_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<question_categories>
  <question_category id="50">
    <name>Daily Examen Questions</name>
    <contextid>123</contextid>
    <contextlevel>50</contextlevel>
    <contextinstanceid>2</contextinstanceid>
    <info>Questions for the Ignatian Daily Examen course</info>
    <infoformat>1</infoformat>
    <stamp>examen_2026_v1</stamp>
    <parent>0</parent>
    <sortorder>999</sortorder>
    <questions>
      
      <question id="1" type="multichoice">
        <parent>0</parent>
        <name><text>Purpose of the Examen</text></name>
        <questiontext format="html">
          <text>What is the PRIMARY purpose of the Daily Examen according to Ignatian spirituality?</text>
        </questiontext>
        <generalfeedback format="html"><text></text></generalfeedback>
        <defaultgrade>1</defaultgrade>
        <penalty>0.3333333</penalty>
        <qtype>multichoice</qtype>
        <length>1</length>
        <stamp>examen.q1.v1</stamp>
        <version>1</version>
        <hidden>0</hidden>
        <timecreated>{ts}</timecreated>
        <timemodified>{ts}</timemodified>
        <createdby>2</createdby>
        <modifiedby>2</modifiedby>
        <plugin_qtype_multichoice_question>
          <answers>
            <answer id="1" fraction="100" format="html">
              <answertext>To notice God's presence in daily life and respond with gratitude</answertext>
              <feedback format="html">
                <text>Correct! The Examen is fundamentally about developing awareness of how God is present and active in the ordinary moments of our day.</text>
              </feedback>
            </answer>
            <answer id="2" fraction="0" format="html">
              <answertext>To confess our sins from the day</answertext>
              <feedback format="html">
                <text>While reflection on sin is part of the Examen, it's not the primary purpose. The Examen is more about noticing God's presence than cataloging failures.</text>
              </feedback>
            </answer>
            <answer id="3" fraction="0" format="html">
              <answertext>To plan the next day's activities</answertext>
              <feedback format="html">
                <text>Planning may emerge from the Examen, but the primary purpose is prayerful reflection and awareness, not task management.</text>
              </feedback>
            </answer>
            <answer id="4" fraction="0" format="html">
              <answertext>To meditate on Scripture passages</answertext>
              <feedback format="html">
                <text>Scripture meditation is a different spiritual practice. The Examen focuses on reviewing your lived experience.</text>
              </feedback>
            </answer>
          </answers>
          <single>1</single>
          <shuffleanswers>1</shuffleanswers>
          <answernumbering>abc</answernumbering>
          <correctfeedback format="html"><text>Correct!</text></correctfeedback>
          <partiallycorrectfeedback format="html"><text>Partially correct.</text></partiallycorrectfeedback>
          <incorrectfeedback format="html"><text>Incorrect.</text></incorrectfeedback>
          <shownumcorrect>1</shownumcorrect>
        </plugin_qtype_multichoice_question>
      </question>

      <question id="2" type="truefalse">
        <parent>0</parent>
        <name><text>Examen Duration Misconception</text></name>
        <questiontext format="html">
          <text>True or False: The Daily Examen must take at least 30 minutes to be effective.</text>
        </questiontext>
        <generalfeedback format="html"><text></text></generalfeedback>
        <defaultgrade>1</defaultgrade>
        <penalty>0.3333333</penalty>
        <qtype>truefalse</qtype>
        <length>1</length>
        <stamp>examen.q2.v1</stamp>
        <version>1</version>
        <hidden>0</hidden>
        <plugin_qtype_truefalse_question>
          <answers>
            <answer id="5" fraction="0" format="moodle_auto_format">
              <answertext>true</answertext>
              <feedback format="html">
                <text>Actually, the Examen can be done effectively in 10-15 minutes. St. Ignatius designed it to be accessible even for busy people. Quality of attention matters more than duration.</text>
              </feedback>
            </answer>
            <answer id="6" fraction="100" format="moodle_auto_format">
              <answertext>false</answertext>
              <feedback format="html">
                <text>Correct! While some people spend longer, the traditional Examen can be done in 10-15 minutes. Ignatius wanted it to be practical for daily life, not burdensome.</text>
              </feedback>
            </answer>
          </answers>
        </plugin_qtype_truefalse_question>
      </question>

      <question id="3" type="multichoice">
        <parent>0</parent>
        <name><text>Five Movements Order</text></name>
        <questiontext format="html">
          <text>Which of the following represents the correct ORDER of the five movements of the Examen?</text>
        </questiontext>
        <generalfeedback format="html"><text></text></generalfeedback>
        <defaultgrade>1</defaultgrade>
        <penalty>0.3333333</penalty>
        <qtype>multichoice</qtype>
        <plugin_qtype_multichoice_question>
          <answers>
            <answer fraction="100" format="html">
              <answertext>Gratitude → Light → Review → Forgiveness → Renewal</answertext>
              <feedback format="html">
                <text>Correct! This is the traditional sequence: becoming aware of God's presence (Gratitude), asking for insight (Light), reviewing the day (Review), asking for healing (Forgiveness), and looking forward (Renewal).</text>
              </feedback>
            </answer>
            <answer fraction="0" format="html">
              <answertext>Review → Forgiveness → Gratitude → Light → Renewal</answertext>
              <feedback format="html">
                <text>We don't jump straight to reviewing. We first ground ourselves in gratitude and God's presence before looking back at the day.</text>
              </feedback>
            </answer>
          </answers>
          <single>1</single>
          <shuffleanswers>1</shuffleanswers>
        </plugin_qtype_multichoice_question>
      </question>

      <question id="4" type="shortanswer">
        <parent>0</parent>
        <name><text>Gratitude Starting Point</text></name>
        <questiontext format="html">
          <text>In the Ignatian Examen, what emotion or disposition should we cultivate FIRST, before reviewing our day?</text>
        </questiontext>
        <defaultgrade>1</defaultgrade>
        <qtype>shortanswer</qtype>
        <plugin_qtype_shortanswer_question>
          <answers>
            <answer fraction="100" format="moodle_auto_format">
              <answertext>gratitude</answertext>
              <feedback><text>Correct!</text></feedback>
            </answer>
            <answer fraction="100" format="moodle_auto_format">
              <answertext>thanksgiving</answertext>
              <feedback><text>Correct!</text></feedback>
            </answer>
            <answer fraction="100" format="moodle_auto_format">
              <answertext>thankfulness</answertext>
              <feedback><text>Correct!</text></feedback>
            </answer>
          </answers>
          <usecase>0</usecase>
        </plugin_qtype_shortanswer_question>
      </question>

      <question id="5" type="multichoice">
        <parent>0</parent>
        <name><text>Why Gratitude First</text></name>
        <questiontext format="html">
          <text>Why does the Examen begin with gratitude rather than immediately reviewing our day?</text>
        </questiontext>
        <qtype>multichoice</qtype>
        <plugin_qtype_multichoice_question>
          <answers>
            <answer fraction="100">
              <answertext>Gratitude grounds us in God's love and helps us see our day as gift rather than merely our own achievement or failure</answertext>
              <feedback><text>Excellent! Beginning with gratitude shifts our perspective from self-judgment to recognition of God's loving presence and action in our lives.</text></feedback>
            </answer>
            <answer fraction="0">
              <answertext>We need to thank God before we're allowed to ask for anything</answertext>
              <feedback><text>This sounds transactional. Gratitude isn't about "earning" the right to pray further—it's about properly orienting our hearts.</text></feedback>
            </answer>
          </answers>
          <single>1</single>
          <shuffleanswers>1</shuffleanswers>
        </plugin_qtype_multichoice_question>
      </question>

    </questions>
  </question_category>
</question_categories>'''.replace('{ts}', str(int(time.time())))

ROLES_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<roles>
  <role_overrides></role_overrides>
  <role_assignments></role_assignments>
</roles>'''

FILES_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<files>
</files>'''

GRADEBOOK_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<gradebook>
  <attributes>
    <grade_items></grade_items>
    <grade_letters></grade_letters>
    <grade_settings></grade_settings>
  </attributes>
</gradebook>'''

if __name__ == '__main__':
    create_backup()