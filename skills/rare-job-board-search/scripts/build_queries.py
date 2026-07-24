#!/usr/bin/env python3
"""Build Google site queries for direct ATS job-board searches."""

from __future__ import annotations

import argparse


PLATFORMS = {
    "ashby": ["jobs.ashbyhq.com"],
    "lever": ["jobs.lever.co"],
    "greenhouse": ["boards.greenhouse.io"],
    "workday": [
        "wd1.myworkdayjobs.com",
        "wd3.myworkdayjobs.com",
        "wd5.myworkdayjobs.com",
        "wd12.myworkdayjobs.com",
    ],
    "smartrecruiters": ["jobs.smartrecruiters.com"],
    "jobvite": ["jobs.jobvite.com"],
    "bamboohr": ["jobs.bamboohr.com"],
    "jazzhr": ["apply.jazz.co"],
    "workable": ["careers.workable.com", "apply.workable.com"],
    "icims": ["careers.icims.com"],
}

PLATFORM_KEYWORDS = {
    "ashby": ["Ashby"],
    "lever": ["Lever"],
    "greenhouse": ["Greenhouse"],
    "workday": ["Workday"],
    "smartrecruiters": ["SmartRecruiters"],
    "jobvite": ["Jobvite"],
    "bamboohr": ["BambooHR"],
    "jazzhr": ["JazzHR"],
    "workable": ["Workable"],
    "icims": ["iCIMS"],
}

PRESETS = {
    "startup": ["ashby", "lever", "greenhouse", "workable", "jazzhr", "bamboohr"],
    "mixed": ["lever", "greenhouse", "smartrecruiters", "jobvite", "ashby"],
    "enterprise": ["workday", "icims", "smartrecruiters", "jobvite"],
    "max-volume": list(PLATFORMS),
}

TITLE_PACKS = {
    "core": [
        "software engineer",
        "backend engineer",
        "software development engineer",
        "SDE I",
        "associate software engineer",
    ],
    "hidden-junior": [
        "software engineer i",
        "software engineer 1",
        "SDE 1",
        "SDE-1",
        "junior software engineer",
        "graduate software engineer",
        "graduate engineer",
        "entry level software engineer",
    ],
    "backend-systems": [
        "backend engineer",
        "backend software engineer",
        "platform engineer",
        "infrastructure engineer",
        "production engineer",
        "integrations engineer",
    ],
    "early-career": [
        "new grad",
        "graduate",
        "entry level",
        "early career",
        "new college graduate",
        "campus",
    ],
}

DISCOVERY_KEYWORDS = ["careers", "jobs", "hiring"]
EXTRA_VENDOR_KEYWORDS = ["Teamtailor", "Recruitee"]

DEFAULT_TITLES = TITLE_PACKS["core"]

DEFAULT_LOCATIONS = [
    "India",
    "Remote",
    "Bengaluru",
    "Bangalore",
]

DEFAULT_EXPERIENCE = [
    "new grad",
    "graduate",
    "entry level",
    "0-1 years",
    "0-2 years",
    "internship",
]


def split_csv(values: list[str]) -> list[str]:
    items: list[str] = []
    for value in values:
        parts = [part.strip() for part in value.split(",")]
        items.extend(part for part in parts if part)
    return items


def unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))


def quote_phrase(value: str) -> str:
    escaped = value.replace('"', '\\"')
    return f'"{escaped}"'


def bool_group(items: list[str]) -> str:
    quoted = []
    for item in items:
        normalized = item.replace(" ", "")
        needs_quotes = " " in item or not normalized.isalnum()
        quoted.append(f'"{item}"' if needs_quotes else item)
    if len(quoted) == 1:
        return quoted[0]
    return "(" + " OR ".join(quoted) + ")"


def site_group(domains: list[str]) -> str:
    if len(domains) == 1:
        return f"site:{domains[0]}"
    return "(" + " OR ".join(f"site:{domain}" for domain in domains) + ")"


def render_query(domains: list[str], groups: list[str], exclude_terms: str) -> str:
    query = f"{site_group(domains)} " + " ".join(groups)
    if exclude_terms:
        query = f"{query} {exclude_terms}"
    return query


def render_terms(terms: list[str], exclude_terms: str) -> str:
    query = " ".join(term for term in terms if term)
    if exclude_terms:
        query = f"{query} {exclude_terms}"
    return query


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate board-specific Google site queries for job search sweeps."
    )
    parser.add_argument(
        "--preset",
        action="append",
        default=[],
        help="Preset platform family or comma-separated list: startup, mixed, enterprise, max-volume.",
    )
    parser.add_argument(
        "--platform",
        action="append",
        default=[],
        help="Platform key or comma-separated keys. May be combined with --preset.",
    )
    parser.add_argument(
        "--site",
        action="append",
        default=[],
        help="Custom site domain or comma-separated domains. Use for employer-specific career domains.",
    )
    parser.add_argument(
        "--company",
        action="append",
        default=[],
        help="Company name or comma-separated list to generate company-seeded discovery queries.",
    )
    parser.add_argument(
        "--title-pack",
        action="append",
        default=[],
        help="Title pack or comma-separated list: core, hidden-junior, backend-systems, early-career.",
    )
    parser.add_argument(
        "--title",
        action="append",
        default=[],
        help="Role title or comma-separated list. Defaults to fresher SWE titles.",
    )
    parser.add_argument(
        "--location",
        action="append",
        default=[],
        help="Location or comma-separated list. Defaults to India plus Bengaluru and remote.",
    )
    parser.add_argument(
        "--experience",
        action="append",
        default=[],
        help="Experience term or comma-separated list. Defaults to fresher-friendly terms.",
    )
    parser.add_argument(
        "--skill",
        action="append",
        default=[],
        help="Skill keyword or comma-separated list to append as a boolean group.",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=["senior", "staff", "principal", "lead"],
        help="Terms to exclude. May be passed multiple times or comma-separated.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    requested_presets = split_csv(args.preset)
    explicit_platforms = split_csv(args.platform)
    custom_sites = unique(split_csv(args.site))
    companies = unique(split_csv(args.company))
    requested_title_packs = split_csv(args.title_pack)
    explicit_titles = split_csv(args.title)
    locations = split_csv(args.location) or DEFAULT_LOCATIONS
    experience = split_csv(args.experience) or DEFAULT_EXPERIENCE
    skills = split_csv(args.skill)
    excludes = split_csv(args.exclude)

    unknown_presets = [preset for preset in requested_presets if preset not in PRESETS]
    if unknown_presets:
        valid = ", ".join(sorted(PRESETS))
        raise SystemExit(
            f"Unknown preset(s): {', '.join(unknown_presets)}. Valid values: {valid}"
        )

    unknown_title_packs = [
        title_pack for title_pack in requested_title_packs if title_pack not in TITLE_PACKS
    ]
    if unknown_title_packs:
        valid = ", ".join(sorted(TITLE_PACKS))
        raise SystemExit(
            f"Unknown title pack(s): {', '.join(unknown_title_packs)}. Valid values: {valid}"
        )

    requested_platforms: list[str] = []
    for preset in requested_presets:
        requested_platforms.extend(PRESETS[preset])
    requested_platforms.extend(explicit_platforms)
    requested_platforms = unique(requested_platforms)

    if not requested_platforms and not custom_sites:
        requested_platforms = list(PLATFORMS)

    unknown = [platform for platform in requested_platforms if platform not in PLATFORMS]
    if unknown:
        valid = ", ".join(sorted(PLATFORMS))
        raise SystemExit(f"Unknown platform(s): {', '.join(unknown)}. Valid values: {valid}")

    titles: list[str] = []
    for title_pack in requested_title_packs:
        titles.extend(TITLE_PACKS[title_pack])
    titles.extend(explicit_titles)
    titles = unique(titles) or DEFAULT_TITLES

    groups = [
        bool_group(titles),
        bool_group(locations),
        bool_group(experience),
    ]
    if skills:
        groups.append(bool_group(skills))

    exclude_terms = " ".join(f"-{term}" for term in excludes if term)

    for platform in requested_platforms:
        print(f"[{platform}]")
        print(render_query(PLATFORMS[platform], groups, exclude_terms))
        print()

    for site in custom_sites:
        print(f"[site:{site}]")
        print(render_query([site], groups, exclude_terms))
        print()

    vendor_keywords = []
    vendor_platforms = requested_platforms or list(PLATFORMS)
    for platform in vendor_platforms:
        vendor_keywords.extend(PLATFORM_KEYWORDS[platform])
    vendor_keywords.extend(EXTRA_VENDOR_KEYWORDS)
    vendor_keywords = unique(vendor_keywords)

    for company in companies:
        company_term = quote_phrase(company)

        print(f"[company:{company}:careers]")
        print(
            render_terms(
                [company_term, bool_group(DISCOVERY_KEYWORDS), *groups],
                exclude_terms,
            )
        )
        print()

        print(f"[company:{company}:ats]")
        print(
            render_terms(
                [company_term, bool_group(vendor_keywords), *groups],
                exclude_terms,
            )
        )
        print()


if __name__ == "__main__":
    main()
