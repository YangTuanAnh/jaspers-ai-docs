# GitHub Repository Setup Instructions

## Initial Setup (One Time)

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `jaspers-ai-docs` (or your preferred name)
3. Description: "Jaspers AI - Technical Documentation and Assessment"
4. Choose **Private** or **Public**
5. **Do NOT** initialize with README, .gitignore, or license
6. Click **Create repository**

### Step 2: Initialize Local Git Repository

Open terminal in this folder (`/Users/minhdoan/work/ai/jasper-cursor/`) and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Jaspers AI documentation and technical assessment"

# Rename branch to main (if needed)
git branch -M main

# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/jaspers-ai-docs.git

# Push to GitHub
git push -u origin main
```

---

## If Repository Already Exists

If you've already created the repository and need to push updates:

```bash
# Add all changes
git add .

# Commit changes
git commit -m "Update documentation"

# Push to GitHub
git push origin main
```

---

## File Structure Being Uploaded

```
jaspers-ai-docs/
├── PRD.md                              # Product Requirements Document
├── test.md                             # Technical Assessment for Engineers
├── apis.md                             # API Architecture Documentation
├── backend-implementation-plan.md      # Backend Development Plan
├── jaspers-ai-mvp.plan.md             # MVP Implementation Plan
├── jaspers.dbml                        # Database Schema
└── GITHUB_SETUP.md                     # This file
```

---

## Quick Commands Reference

### Check Status
```bash
git status
```

### See What Changed
```bash
git diff
```

### View Commit History
```bash
git log --oneline
```

### Add Specific File
```bash
git add PRD.md
git commit -m "Update PRD"
git push
```

### Update All Files
```bash
git add -A
git commit -m "Update all documentation"
git push
```

---

## Create .gitignore (Optional)

If you want to exclude certain files:

```bash
# Create .gitignore file
cat > .gitignore << 'EOF'
# OS Files
.DS_Store
Thumbs.db

# Editor Files
.vscode/
.idea/
*.swp
*.swo

# Temporary Files
*.tmp
*.log

# Environment Files (if you add any)
.env
.env.local

# Node modules (if you add code later)
node_modules/
EOF

git add .gitignore
git commit -m "Add .gitignore"
git push
```

---

## Sharing with Others

### Give Access to Repository

1. Go to your repository on GitHub
2. Click **Settings** tab
3. Click **Collaborators** in left sidebar
4. Click **Add people**
5. Enter their GitHub username or email
6. Choose permission level (Read, Write, or Admin)

### Share Repository Link

- **Public repo:** `https://github.com/YOUR_USERNAME/jaspers-ai-docs`
- **Private repo:** Invite collaborators first (they need GitHub account)

---

## Common Issues & Solutions

### Issue: "remote origin already exists"
```bash
# Remove existing remote
git remote remove origin

# Add correct remote
git remote add origin https://github.com/YOUR_USERNAME/jaspers-ai-docs.git
```

### Issue: "failed to push some refs"
```bash
# Pull remote changes first
git pull origin main --rebase

# Then push
git push origin main
```

### Issue: "Authentication failed"
```bash
# Use Personal Access Token instead of password
# Generate token at: https://github.com/settings/tokens
# Use token as password when prompted
```

---

## For Daywednes (Collaborator Instructions)

If you're sharing this repository with someone:

### Option 1: They Clone the Repository
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/jaspers-ai-docs.git

# Navigate into folder
cd jaspers-ai-docs

# View files
ls -la
```

### Option 2: Download as ZIP
1. Go to repository on GitHub
2. Click green **Code** button
3. Click **Download ZIP**
4. Extract and open files

---

## Next Steps

After pushing to GitHub:

1. ✅ Verify files appear on GitHub
2. ✅ Add repository description and topics
3. ✅ Add collaborators if needed
4. ✅ Share repository URL with team
5. ✅ Update README on GitHub (optional)

---

## Need Help?

- **GitHub Docs:** https://docs.github.com/en/get-started
- **Git Cheat Sheet:** https://education.github.com/git-cheat-sheet-education.pdf
- **Troubleshooting:** https://docs.github.com/en/get-started/using-git/troubleshooting-the-git-commit-command

