# Automated Workflow #
## TRIGGER----> New TPT Ticket Detected ##

**STEP 1:** Monitor  and Alert MarCom (Automated via TPT MCP Server)

**STEP 2:** Download Attachment (Word/PDF)

**STEP 3:** Extract & Parse Content (Claude AI analyzes content-Using claude skill/command)

**STEP 4:** AI Clarity Check (Claude identifies gaps, ambiguities - Claude Skill)
 
**STEP 5:** If content clear, move to STEP 5. If not, ask for clarification from SME (Human intervention)

**STEP 6:** Create/Update publication in Tridion (Automated via Tridion MCP)

**STEP 7:** Generate DITA XML topics if new document or else update topic (Claude generates XML)

**STEP 8:** Generate Output (Automated)

**STEP 9:** Create Adobe shared review and add reviewers (Automated via Adobe MCP)

**STEP 10:** Monitor Review and track approvals. Follow steps 2 through 8 if further inputs received from SME.

**STEP 11:** Once all changes approved, initiate final TPT approval.(Human review to avoid any missing edits)

**STEP 12:** Release Draft in Tridion DOCs (Human final review and then automated release)

**STEP 13:** Post the released document to TPT (Automated via Sharepoint MCP)

**STEP 14:** Publish to AEM if confirmed by SME (Human plus Automated via AEM MCP)

### Time Savings Breakdown ###
| Task | Manual Time | Automated Time | Savings |
|------|------------|----------------|---------|
| **Download & Parse Attachments** | 15-30 min | 1-2 min | 93% |
| **Content Quality Analysis** | 20-45 min | 2-3 min | 95% |
| **Create/Open Publication** | 10-15 min | 1-2 min | 85% |
| **Generate DITA Changes** | 30-60 min | 5-10 min | 83% |
| **Create Adobe Review** | 15-20 min | 1 min | 98% |
| **Add Reviewers & Send Invites** | 10-15 min | <1 min | 99% |
| **Monitor Review Status** | 20-30 min (continuous) | <1 min (auto-polling) | 99% |
| **Publication Release** | 5-10 min | <1 min | 95% |
| **AEM Publishing** | 10-15 min | 1-2 min | 92% |
| **TPT Status Updates** | 5-10 min | <1 min | 99% |
| **TOTAL PER RELEASE** | **2.5-4 hours** | **15-25 minutes** | **~90% Reduction** |

## Where Humans Must Intervene ##

* When: Step 4 - If Claude's analysis detects ambiguities, missing information, or unclear technical details, human review is important. 
* What Writers Must Do:
  * Contact the SME with specific clarification questions.
  * Receive SME response and validate completeness
  * Confirm ready to proceed 

* When: During DITA generation if content involves:
  * Architecture changes requiring restructuring
  * Significant content reorganization
* What Writers Must Do:
  * Review AI-generated DITA structure
  * Validate against style guide & publishing standards
  * Make manual adjustments if needed
  * Approve final structure

## Automation Summary ##
### FULLY AUTOMATED (90% of workflow):###
* TPT ticket monitoring
* Attachment download & extraction
* Content parsing & clarity assessment
* Publication creation/versioning
* DITA XML generation & updates
* Document output generation
* Adobe review creation
* Reviewer notifications
* Status tracking & polling
* Final publication release
* AEM website publishing

### HUMAN-REQUIRED (10% of workflow): ###
* Content clarification with SMEs
* Review feedback assessment & implementation
* Technical decision validation
* Optional QA review
