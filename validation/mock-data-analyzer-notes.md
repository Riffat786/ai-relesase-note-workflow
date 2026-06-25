This file is simply pretending to be the combined output of **Azure DevOps + ServiceNow**.

## Step 1: Create a JSON file

Created the file in data > release--2025.8.json

## Step 2: Add Realistic Mock Data

Use a mix of:

- Features
- Enhancements
- Bugs
- Technical Tasks (that should be filtered out)

This helps demonstrate the AI's ability to classify and filter.

## Step 3: Why This Data Works

**Analyzer Agent** should produce:

**Features**
- Multi-Factor Authentication
- Export Dashboard Reports

**Enhancements**
- Improved Search Performance
  
**Bug Fixes**
- Password Reset Email Failure
- Duplicate Notifications

**Filtered Out**
- Database Index Optimization
- Upgrade Logging Framework
- Production Deployment

This demonstrates:

✅ Classification

✅ Filtering

✅ Business value extraction

## Step 4: Test the expected outcome
I have document this in validation/mock-data-validation.md and output/anaylyzed-released.json.

# What I Just Built

Collector Agent
        ↓
Analyzer Agent

workflow.

The JSON file is acting as:

**Collector Agent Output**

and Claude's response is acting as:

**Analyzer Agent Output**

# The pipeline becomes:

release-2025.8.json
        ↓
Analyzer Agent
        ↓
analyzed-release.json