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

PRESETS = {
    "startup": ["ashby", "lever", "greenhouse", "workable", "jazzhr", "bamboohr"],
    "mixed": ["lever", "greenhouse", "smartrecruiters", "jobvite", "ashby"],
    "enterprise": ["workday", "icims", "smartrecruiters", "jobvite"],
    "max-volume": list(PLATFORMS),
}

DEFAULT_TITLES = [
    "software engineer",
    "backend engineer",
    "software development engineer",
    "SDE I",
    "associate software engineer",
]

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


def bool_group(items: list[str]) -> str:
    quoted = [f'"{item}"' if " " in item else item for item in items]
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
    titles = split_csv(args.title) or DEFAULT_TITLES
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


if __name__ == "__main__":
    main()
