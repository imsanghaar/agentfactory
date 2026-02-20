interface ExerciseConfig {
  repo: string;
  releaseTag: string;
  description?: string;
}

const EXERCISE_REGISTRY: Record<string, ExerciseConfig> = {
  "ch3-basics": {
    repo: "panaversity/claude-code-basic-exercises",
    releaseTag: "latest",
    description:
      "Claude Code Basic Exercises — prompting, file operations, debugging",
  },
  "ch3-skills": {
    repo: "panaversity/claude-code-skills-exercises",
    releaseTag: "latest",
    description: "Claude Code Skills Exercises — custom skills creation",
  },
  "ch3-plugins": {
    repo: "panaversity/claude-code-plugins-exercises",
    releaseTag: "latest",
    description: "Claude Code Plugins Exercises — MCP and tool integration",
  },
  "ch3-agent-teams": {
    repo: "panaversity/claude-code-agent-teams-exercises",
    releaseTag: "latest",
    description: "Claude Code Agent Teams Exercises — multi-agent workflows",
  },
  "ch4-context": {
    repo: "panaversity/claude-code-context-exercises",
    releaseTag: "latest",
    description:
      "Context Engineering Exercises — CLAUDE.md, memory, prompt design",
  },
  "ch5-sdd": {
    repo: "panaversity/claude-code-sdd-exercises",
    releaseTag: "latest",
    description:
      "Spec-Driven Development Exercises — specs, plans, tasks workflows",
  },
  "ch6-principles": {
    repo: "panaversity/claude-code-principles-exercises",
    releaseTag: "latest",
    description:
      "Seven Principles Exercises — bash, verification, decomposition",
  },
  "ch8-file-processing": {
    repo: "panaversity/claude-code-file-processing-exercises",
    releaseTag: "latest",
    description:
      "File Processing Exercises — markdown, CSV, JSON, batch workflows",
  },
  "ch9-computation": {
    repo: "panaversity/claude-code-computation-exercises",
    releaseTag: "latest",
    description:
      "Computation & Data Extraction Exercises — calculations, parsing, analysis",
  },
  "ch10-structured-data": {
    repo: "panaversity/claude-code-structured-data-exercises",
    releaseTag: "latest",
    description:
      "Structured Data Exercises — databases, schemas, persistent storage",
  },
  "ch11-linux": {
    repo: "panaversity/claude-code-linux-mastery-exercises",
    releaseTag: "latest",
    description:
      "Linux Mastery Exercises — commands, scripting, system operations",
  },
  "ch12-version-control": {
    repo: "panaversity/claude-code-version-control-exercises",
    releaseTag: "latest",
    description:
      "Version Control Exercises — git workflows, branching, collaboration",
  },
};

export function getExercise(exerciseId: string): ExerciseConfig | undefined {
  return EXERCISE_REGISTRY[exerciseId];
}

export function listExercises(): Record<string, ExerciseConfig> {
  return { ...EXERCISE_REGISTRY };
}
