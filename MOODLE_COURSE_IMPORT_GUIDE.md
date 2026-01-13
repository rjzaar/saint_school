# Moodle Course Import Guide

This guide covers importing a Moodle course backup (.mbz file) into your Moodle site using the web interface.

---

## Prerequisites

Before importing a course, ensure you have:

1. **Administrator or Manager role** on the Moodle site
2. **A valid .mbz backup file** (Moodle backup format)
3. **Sufficient server storage** for the backup file and restored course
4. **PHP upload limits** configured appropriately (check with your admin if uploads fail)

---

## Understanding .mbz Files

The `.mbz` extension stands for "Moodle Backup Zip". These files contain:

- Course structure (sections, activities, resources)
- Question bank and quizzes
- User data (optional, depending on backup settings)
- Files and media
- Grades and completion data (optional)

---

## Method 1: Restore as a New Course

Use this method to create a completely new course from a backup file.

### Step 1: Navigate to Restore

1. Log into Moodle as an administrator
2. Go to **Site administration** (gear icon or left menu)
3. Navigate to **Courses** → **Restore course**

   *Alternative path*: Site administration → Courses → Manage courses and categories → Select a category → Click "Restore"

### Step 2: Upload the Backup File

1. In the **Import a backup file** section, either:
   - **Drag and drop** your .mbz file into the upload area, OR
   - Click **Choose a file** → Upload the .mbz file from your computer

2. Click **Restore**

   **Note**: If you see a file size error, contact your administrator to increase `upload_max_filesize` and `post_max_size` in PHP settings.

### Step 3: Confirm Backup Details

1. Review the backup file details displayed:
   - Backup date
   - Moodle version used to create backup
   - Course information
   - What's included (activities, blocks, files, etc.)

2. Click **Continue**

### Step 4: Choose Destination

1. Select **Restore as a new course**
2. Choose a **course category** where the new course will be placed
3. Click **Continue**

### Step 5: Configure Restore Settings

Review and configure the following settings:

| Setting | Description | Recommendation |
|---------|-------------|----------------|
| **Include activities and resources** | Restore all course content | Yes |
| **Include blocks** | Restore sidebar blocks | Yes |
| **Include filters** | Restore text filters | Yes |
| **Include comments** | Restore user comments | Optional |
| **Include badges** | Restore course badges | Yes if used |
| **Include calendar events** | Restore calendar items | Yes |
| **Include question bank** | Restore questions | Yes |
| **Include groups and groupings** | Restore group structures | Yes if used |
| **Include competencies** | Restore learning competencies | Yes if used |
| **Include content bank content** | Restore H5P and other content | Yes |
| **Include legacy files** | Restore old-style files | Usually not needed |

Click **Next**

### Step 6: Course Settings

Configure the restored course settings:

1. **Course name**: Enter the full name for the course
2. **Short name**: Enter a unique short identifier (e.g., COURSE101)
3. **Course start date**: Set when the course begins
4. **Course ID number**: Optional identifier for external systems

Click **Next**

### Step 7: Review and Execute

1. Review the complete restore summary showing:
   - Course settings
   - Sections to be restored
   - Activities and resources
   - Estimated file sizes

2. Click **Perform restore**

3. Wait for the restore process to complete (may take several minutes for large courses)

4. When you see "The course was restored successfully", click **Continue** to view your new course

---

## Method 2: Import into an Existing Course

Use this method to add content from a backup into a course that already exists.

### Step 1: Navigate to the Target Course

1. Go to the course where you want to import content
2. Click the **gear icon** (settings) in the top right
3. Select **Restore** from the dropdown menu

   *Alternative*: Course administration → Restore

### Step 2: Upload and Restore

1. Upload your .mbz file
2. Click **Restore**
3. When asked about destination, select:
   - **Merge the backup course into this course** (adds content alongside existing)
   - OR **Delete the contents of this course and then restore** (replaces everything)

4. Follow the remaining steps as in Method 1

### Important Considerations for Merging

When merging courses:
- Activities will be added to matching sections where possible
- Duplicate activity names may occur
- Question bank categories will be preserved (may create duplicates)
- Grades and user data require careful handling

---

## Method 3: Command Line Restore (Advanced)

For automated or scripted restores, use the CLI:

```bash
# Basic restore to new course
php admin/cli/restore_backup.php \
  --file=/path/to/backup.mbz \
  --categoryid=1

# With specific short name
php admin/cli/restore_backup.php \
  --file=/path/to/backup.mbz \
  --categoryid=1 \
  --shortname=MYCOURSE

# In a DDEV environment
ddev exec php admin/cli/restore_backup.php \
  --file=/var/www/html/backup.mbz \
  --categoryid=1
```

---

## Troubleshooting Import Issues

### Error: "File exceeds maximum upload size"

**Solution**: Increase PHP limits in `php.ini`:
```ini
upload_max_filesize = 256M
post_max_size = 256M
max_execution_time = 600
memory_limit = 512M
```

For DDEV, add to `.ddev/php/my-php.ini`:
```ini
upload_max_filesize = 256M
post_max_size = 256M
```

### Error: "Invalid backup file"

**Possible causes and solutions**:

1. **Corrupted download**: Re-download the backup file
2. **Wrong format**: Ensure it's a genuine .mbz file, not renamed
3. **Version mismatch**: Backup from much newer Moodle version

Check the file type:
```bash
file backup.mbz
# Should show: "Zip archive data" or similar
```

### Error: "Missing XML files" during restore

Some backups may be missing required XML files. Fix with:

```bash
# Extract the backup
mkdir extracted
cd extracted
unzip ../backup.mbz

# Create missing files
echo '<?xml version="1.0" encoding="UTF-8"?>
<roles><role_overrides></role_overrides><role_assignments></role_assignments></roles>' > roles.xml

echo '<?xml version="1.0" encoding="UTF-8"?>
<groups></groups>' > groups.xml

echo '<?xml version="1.0" encoding="UTF-8"?>
<scales></scales>' > scales.xml

echo '<?xml version="1.0" encoding="UTF-8"?>
<outcomes></outcomes>' > outcomes.xml

echo '<?xml version="1.0" encoding="UTF-8"?>
<grade_histories></grade_histories>' > grade_histories.xml

# Repackage
zip -r ../backup_fixed.mbz *
```

### Error: "Course short name already exists"

**Solution**: Choose a different short name in Step 6, or delete/rename the existing course first.

### Restore takes too long or times out

**Solutions**:
1. Increase PHP `max_execution_time` to 600 or higher
2. Use CLI restore instead (no timeout issues)
3. Restore without user data to reduce size
4. Split large courses into smaller backups

---

## Post-Import Checklist

After successfully importing a course:

- [ ] Verify all sections appear correctly
- [ ] Check that activities and resources are accessible
- [ ] Test quiz questions work properly
- [ ] Confirm files and images display correctly
- [ ] Review course settings (dates, visibility, enrollment)
- [ ] Check question bank imported correctly
- [ ] Test one quiz attempt to verify functionality
- [ ] Review and update any date-based restrictions
- [ ] Enroll test users to verify student experience

---

## Best Practices for Course Imports

1. **Always test imports on a staging site first** before production
2. **Document the original Moodle version** of the backup
3. **Keep backup files archived** for future reference
4. **Check storage space** before large imports
5. **Notify users** before importing into active courses
6. **Schedule imports during low-traffic periods**
7. **Verify backup integrity** before important imports

---

## Related Documentation

- [Moodle Course Creation Guide](MOODLE_COURSE_CREATION_GUIDE.md) - Technical guide for programmatic course creation
