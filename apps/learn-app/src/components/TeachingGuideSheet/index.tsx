/**
 * TeachingGuideSheet
 *
 * Surfaces pedagogical metadata from lesson YAML frontmatter
 * in a slide-in sheet. Organized into logical groups so teachers
 * can quickly scan the guide alongside lesson content.
 */

import React from "react";
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetDescription,
} from "@/components/ui/sheet";
import styles from "./styles.module.css";

/* ─── Frontmatter types ─── */

interface Skill {
  name: string;
  proficiency_level?: string;
  category?: string;
  bloom_level?: string;
  digcomp_area?: string;
  measurable_at_this_level?: string;
}

interface LearningObjective {
  objective: string;
  proficiency_level?: string;
  bloom_level?: string;
  assessment_method?: string;
}

interface CognitiveLoad {
  new_concepts?: number;
  assessment?: string;
}

interface Differentiation {
  extension_for_advanced?: string;
  remedial_for_struggling?: string;
}

interface TeachingGuide {
  lesson_type?: string;
  session_group?: number;
  session_title?: string;
  key_points?: string[];
  misconceptions?: string[];
  discussion_prompts?: string[];
  teaching_tips?: string[];
  assessment_quick_check?: string[];
}

export interface TeachingFrontmatter {
  title?: string;
  duration_minutes?: number;
  primary_layer?: string;
  layer_progression?: string;
  learning_objectives?: LearningObjective[];
  skills?: Skill[];
  cognitive_load?: CognitiveLoad;
  differentiation?: Differentiation;
  prerequisites?: string[];
  teaching_guide?: TeachingGuide;
}

interface TeachingGuideSheetProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  frontmatter: TeachingFrontmatter;
}

/* ─── Bloom badge color mapping ─── */

const bloomClass: Record<string, string> = {
  Remember: styles.bloomRemember,
  Understand: styles.bloomUnderstand,
  Apply: styles.bloomApply,
  Analyze: styles.bloomAnalyze,
  Evaluate: styles.bloomEvaluate,
  Create: styles.bloomCreate,
};

/* ─── Main component ─── */

export function TeachingGuideSheet({
  open,
  onOpenChange,
  frontmatter: fm,
}: TeachingGuideSheetProps) {
  const guide = fm.teaching_guide;

  // Build session info line
  const sessionParts: string[] = [];
  if (guide?.session_group != null)
    sessionParts.push(`Session ${guide.session_group}`);
  if (guide?.session_title) sessionParts.push(guide.session_title);
  if (guide?.lesson_type) sessionParts.push(guide.lesson_type);

  const hasOverview =
    fm.duration_minutes != null || fm.primary_layer || sessionParts.length > 0;

  const hasObjectives =
    (fm.learning_objectives && fm.learning_objectives.length > 0) ||
    (fm.skills && fm.skills.length > 0);

  const hasStudentNeeds =
    fm.cognitive_load?.new_concepts != null ||
    fm.cognitive_load?.assessment ||
    fm.differentiation?.extension_for_advanced ||
    fm.differentiation?.remedial_for_struggling ||
    (fm.prerequisites && fm.prerequisites.length > 0);

  const hasTeachingGuide =
    guide &&
    ((guide.key_points && guide.key_points.length > 0) ||
      (guide.misconceptions && guide.misconceptions.length > 0) ||
      (guide.discussion_prompts && guide.discussion_prompts.length > 0) ||
      (guide.teaching_tips && guide.teaching_tips.length > 0) ||
      (guide.assessment_quick_check &&
        guide.assessment_quick_check.length > 0));

  return (
    <Sheet open={open} onOpenChange={onOpenChange}>
      <SheetContent
        side="right"
        className={`${styles.sheetContent} sm:max-w-lg`}
      >
        <SheetHeader className={styles.sheetHeader}>
          <SheetTitle className={styles.sheetTitle}>Teaching Aid</SheetTitle>
          <SheetDescription className={styles.sheetDescription}>
            Pedagogical guide for this lesson
          </SheetDescription>
        </SheetHeader>

        <div className={styles.scrollArea}>
          {/* ─── GROUP 1: Lesson Overview (banner) ─── */}
          {hasOverview && (
            <div className={`${styles.group} ${styles.overviewBanner}`}>
              {fm.duration_minutes != null && (
                <div className={styles.overviewItem}>
                  <span className={styles.overviewLabel}>Duration</span>
                  <span className={styles.overviewValue}>
                    {fm.duration_minutes} min
                  </span>
                </div>
              )}
              {fm.primary_layer && (
                <div className={styles.overviewItem}>
                  <span className={styles.overviewLabel}>Layer</span>
                  <span className={styles.overviewValue}>
                    <span className={styles.layerBadge}>
                      {fm.primary_layer}
                    </span>
                    {fm.layer_progression && (
                      <span className={styles.layerDetail}>
                        {fm.layer_progression}
                      </span>
                    )}
                  </span>
                </div>
              )}
              {sessionParts.length > 0 && (
                <div className={styles.overviewItem}>
                  <span className={styles.overviewLabel}>Session</span>
                  <span className={styles.overviewValue}>
                    {sessionParts.join(" \u2022 ")}
                  </span>
                </div>
              )}
            </div>
          )}

          {/* ─── GROUP 2: Learning Outcomes ─── */}
          {hasObjectives && (
            <div className={styles.group}>
              <h3 className={styles.groupTitle}>Learning Outcomes</h3>

              {fm.learning_objectives && fm.learning_objectives.length > 0 && (
                <div className={styles.subsection}>
                  <h4 className={styles.subsectionTitle}>Objectives</h4>
                  <table className={styles.objectivesTable}>
                    <thead>
                      <tr>
                        <th>Objective</th>
                        <th>Level</th>
                        <th>Bloom</th>
                      </tr>
                    </thead>
                    <tbody>
                      {fm.learning_objectives.map((obj, i) => (
                        <tr key={i}>
                          <td>
                            <span className={styles.objectiveText}>
                              {obj.objective}
                            </span>
                            {obj.assessment_method && (
                              <span className={styles.assessmentHint}>
                                {obj.assessment_method}
                              </span>
                            )}
                          </td>
                          <td>
                            {obj.proficiency_level && (
                              <span
                                className={`${styles.badge} ${styles.proficiency}`}
                              >
                                {obj.proficiency_level}
                              </span>
                            )}
                          </td>
                          <td>
                            {obj.bloom_level && (
                              <span
                                className={`${styles.badge} ${bloomClass[obj.bloom_level] ?? ""}`}
                              >
                                {obj.bloom_level}
                              </span>
                            )}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}

              {fm.skills && fm.skills.length > 0 && (
                <div className={styles.subsection}>
                  <h4 className={styles.subsectionTitle}>Skills Built</h4>
                  <div className={styles.skillCards}>
                    {fm.skills.map((skill, i) => (
                      <div key={i} className={styles.skillCard}>
                        <span className={styles.skillName}>{skill.name}</span>
                        <div className={styles.skillBadges}>
                          {skill.proficiency_level && (
                            <span
                              className={`${styles.badge} ${styles.proficiency}`}
                            >
                              {skill.proficiency_level}
                            </span>
                          )}
                          {skill.bloom_level && (
                            <span
                              className={`${styles.badge} ${bloomClass[skill.bloom_level] ?? ""}`}
                            >
                              {skill.bloom_level}
                            </span>
                          )}
                          {skill.category && (
                            <span className={styles.badge}>
                              {skill.category}
                            </span>
                          )}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}

          {/* ─── GROUP 3: Student Needs ─── */}
          {hasStudentNeeds && (
            <div className={styles.group}>
              <h3 className={styles.groupTitle}>Student Needs</h3>

              {fm.cognitive_load &&
                (fm.cognitive_load.new_concepts != null ||
                  fm.cognitive_load.assessment) && (
                  <div className={styles.subsection}>
                    <h4 className={styles.subsectionTitle}>Cognitive Load</h4>
                    <div className={styles.cognitiveCard}>
                      {fm.cognitive_load.new_concepts != null && (
                        <div className={styles.cognitiveCount}>
                          <span className={styles.cognitiveNumber}>
                            {fm.cognitive_load.new_concepts}
                          </span>
                          <span className={styles.cognitiveLabel}>
                            new concepts
                          </span>
                        </div>
                      )}
                      {fm.cognitive_load.assessment && (
                        <p className={styles.cognitiveNote}>
                          {fm.cognitive_load.assessment}
                        </p>
                      )}
                    </div>
                  </div>
                )}

              {(fm.differentiation?.extension_for_advanced ||
                fm.differentiation?.remedial_for_struggling) && (
                <div className={styles.subsection}>
                  <h4 className={styles.subsectionTitle}>Differentiation</h4>
                  <div className={styles.diffCards}>
                    {fm.differentiation?.extension_for_advanced && (
                      <div
                        className={`${styles.diffCard} ${styles.diffAdvanced}`}
                      >
                        <span className={styles.diffLabel}>
                          Advanced Students
                        </span>
                        <p>{fm.differentiation.extension_for_advanced}</p>
                      </div>
                    )}
                    {fm.differentiation?.remedial_for_struggling && (
                      <div
                        className={`${styles.diffCard} ${styles.diffStruggling}`}
                      >
                        <span className={styles.diffLabel}>
                          Struggling Students
                        </span>
                        <p>{fm.differentiation.remedial_for_struggling}</p>
                      </div>
                    )}
                  </div>
                </div>
              )}

              {fm.prerequisites && fm.prerequisites.length > 0 && (
                <div className={styles.subsection}>
                  <h4 className={styles.subsectionTitle}>Prerequisites</h4>
                  <ul className={styles.bulletList}>
                    {fm.prerequisites.map((p, i) => (
                      <li key={i}>{p}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}

          {/* ─── GROUP 4: Teaching Guide ─── */}
          {hasTeachingGuide && guide && (
            <div className={styles.group}>
              <h3 className={styles.groupTitle}>Teaching Guide</h3>

              {guide.key_points && guide.key_points.length > 0 && (
                <div className={styles.subsection}>
                  <h4 className={styles.subsectionTitle}>Key Points</h4>
                  <ul className={styles.numberedList}>
                    {guide.key_points.map((pt, i) => (
                      <li key={i}>{pt}</li>
                    ))}
                  </ul>
                </div>
              )}

              {guide.misconceptions && guide.misconceptions.length > 0 && (
                <div className={styles.subsection}>
                  <h4
                    className={`${styles.subsectionTitle} ${styles.warningTitle}`}
                  >
                    Common Misconceptions
                  </h4>
                  <ul className={styles.warningList}>
                    {guide.misconceptions.map((m, i) => (
                      <li key={i}>{m}</li>
                    ))}
                  </ul>
                </div>
              )}

              {guide.discussion_prompts &&
                guide.discussion_prompts.length > 0 && (
                  <div className={styles.subsection}>
                    <h4 className={styles.subsectionTitle}>
                      Discussion Prompts
                    </h4>
                    <ul className={styles.promptList}>
                      {guide.discussion_prompts.map((p, i) => (
                        <li key={i}>{p}</li>
                      ))}
                    </ul>
                  </div>
                )}

              {guide.teaching_tips && guide.teaching_tips.length > 0 && (
                <div className={styles.subsection}>
                  <h4 className={styles.subsectionTitle}>Teaching Tips</h4>
                  <ul className={styles.tipList}>
                    {guide.teaching_tips.map((t, i) => (
                      <li key={i}>{t}</li>
                    ))}
                  </ul>
                </div>
              )}

              {guide.assessment_quick_check &&
                guide.assessment_quick_check.length > 0 && (
                  <div className={styles.subsection}>
                    <h4 className={styles.subsectionTitle}>Quick Assessment</h4>
                    <ul className={styles.checkList}>
                      {guide.assessment_quick_check.map((c, i) => (
                        <li key={i}>{c}</li>
                      ))}
                    </ul>
                  </div>
                )}
            </div>
          )}
        </div>
      </SheetContent>
    </Sheet>
  );
}
