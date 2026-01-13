# Rosary 101 Course - Working Backup

## File
`rosary101-working-backup.mbz`

## Description
This is a **fully working** Moodle course backup created on 2026-01-13. It contains the complete Rosary 101 course with all quizzes functioning correctly.

## Course Contents

### Course Information
- **Course Name**: Rosary 101
- **Course ID**: 8 (in source system)
- **Moodle Version**: 4.4.12+ (Build: 20251212)

### Course Structure
The course includes:
- Multiple page resources with instructional content
- **4 Working Quizzes** with 34 questions total

### Quizzes

1. **Quiz: The Prayers of the Rosary** (8 questions)
   - Questions 71-78
   - Focus: Memorizing the prayers used in the Rosary

2. **Quiz: Structure of the Rosary** (6 questions)
   - Questions 79-84
   - Focus: Understanding how the Rosary is structured and how to use rosary beads

3. **Quiz: The Mysteries of the Rosary** (10 questions)
   - Questions 85-94
   - Focus: The four sets of mysteries and their traditional days

4. **Final Quiz: Comprehensive Review** (10 questions)
   - Questions 95-104
   - Focus: Comprehensive review of all Rosary aspects
   - Passing score: 80%

### Question Types
- Multiple Choice (10 questions)
- True/False (18 questions)
- Short Answer (6 questions)

## How to Import

### Method 1: Via Moodle Web UI (Easiest)
1. Log into your Moodle site as an administrator
2. Navigate to: **Site Administration > Courses > Restore Course**
3. Upload `rosary101-working-backup.mbz`
4. Follow the restore wizard:
   - Select target category
   - Choose restore options (create new course recommended)
   - Complete the process

### Method 2: Via Command Line
```bash
# From your Moodle root directory
php admin/cli/restore_backup.php \
  --file=/path/to/rosary101-working-backup.mbz \
  --categoryid=1 \
  --shortname=ROSARY101

# Or if using DDEV:
ddev exec php admin/cli/restore_backup.php \
  --file=/path/to/rosary101-working-backup.mbz \
  --categoryid=1 \
  --shortname=ROSARY101
```

## Technical Notes

### What Makes This Backup "Working"

This backup was created **after** fixing all the quiz structure issues. The quizzes in this backup were built using:

1. **Moodle's Official APIs** - Used `quiz_add_quiz_question()` instead of manual database manipulation
2. **Proper Version Fields** - All `question_references` have `version=1` set correctly
3. **Question Set References** - All quizzes have proper `question_set_references` entries
4. **Complete Question Structure** - All questions include:
   - Question bank entries
   - Question versions
   - Question data
   - Answers
   - Type-specific options (truefalse, shortanswer, multichoice)

### Differences from Original Backups

The original backup files (`backup-moodle2-course-rosarywithquestions.mbz` and `backup-moodle2-course-rosary101-20251230-0944.mbz`) had structural issues that caused errors when attempting quizzes. This backup was created from the **working course** after all fixes were applied.

## Verification

After importing, verify the course works by:
1. Enrolling a test user in the course
2. Attempting each quiz
3. Verifying questions display correctly
4. Verifying answers are graded correctly

If you encounter any "Can't find data record in database" errors, refer to the troubleshooting guide in `MOODLE_COURSE_CREATION_GUIDE.md`.

## Backup Details

- **Created**: 2026-01-13 14:11 UTC
- **Backup Format**: Moodle 2.x course backup (.mbz)
- **Compression**: gzip
- **File Size**: 42KB
- **Original Size**: 812KB (uncompressed)

## Related Files

- `MOODLE_COURSE_CREATION_GUIDE.md` - Complete guide for creating Moodle courses with quizzes
- `rosary_questions.xml` - Extracted questions in Moodle XML format (if you need to import questions separately)

## License

Course content is provided as-is for educational purposes related to Catholic devotional practices.

## Support

If you encounter issues importing or using this course backup, refer to:
1. The troubleshooting section in `MOODLE_COURSE_CREATION_GUIDE.md`
2. Moodle documentation: https://docs.moodle.org/en/Course_restore
3. Verify your Moodle version is 4.4+ (this backup may not work with older versions)

---

**Last Updated**: 2026-01-13
**Tested With**: Moodle 4.4.12+ (Build: 20251212)
