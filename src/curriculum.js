/** Append newly released bundled lessons without replacing authored lessons or progress. */
export function syncBundledCourse(state, bundled) {
  const existing = state.courses.find(course => course.id === bundled.id);
  if (!existing) {
    state.courses.unshift(structuredClone(bundled));
    return { added: 0, installed: true };
  }

  const previousRevision = existing.contentRevision ?? 1;
  const latestRevision = bundled.contentRevision ?? 1;
  if (previousRevision >= latestRevision) return { added: 0 };

  const knownIds = new Set(existing.lessons.map(lesson => lesson.id));
  const additions = bundled.lessons.filter(lesson =>
    (lesson.introducedInRevision ?? 1) > previousRevision && !knownIds.has(lesson.id)
  );

  // A heavily customized course must remain importable under the schema's size limit.
  if (existing.lessons.length + additions.length > 365) {
    return { added: 0, deferred: true };
  }

  existing.lessons.push(...structuredClone(additions));
  existing.contentRevision = latestRevision;
  if (existing.description === 'Big ideas. Tiny lessons. Build your intuition, one day at a time.') {
    existing.description = bundled.description;
  }
  // Drafts are intentionally independent: never overwrite work being authored.
  // Progress, XP, activity dates, and matching lesson IDs are left intact.
  return { added: additions.length };
}
