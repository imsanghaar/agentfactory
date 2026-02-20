export default function useDocusaurusContext() {
  return {
    siteConfig: {
      customFields: {
        practiceEnabled: true,
      },
    },
    i18n: { currentLocale: "en" },
  };
}
