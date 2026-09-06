from typing import NotRequired, TypedDict, final

"""
To get the types of all of the
```
% cat courts_db/data/courts.json | jq 'map(map_values(type)) | reduce (.[] | to_entries[]) as $entry ({}; .[$entry.key][$entry.value] += 1)'
{
    "case_types": {"array":2538,"null":1,"string":10}
    "citation_string": {"string":2809}
    "dates": {"array":2809}
    "examples": {"array":2809}
    "id": {"string":2809}
    "jurisdiction": {"string":1332,"null":6}
    "level": {"string":2517,"null":292}
    "location": {"string":2809}
    "locations": {"number":153}
    "name": {"string":2809}
    "name_abbreviation": {"null":163,"string":262}
    "regex": {"array":2809}
    "sub_names": {"array":20}
    "system": {"string":2809}
    "type": {"string":2775,"null":34}
    "court_url": {"string":1952,"null":1}
    "appeal_to": {"string":37,"null":56,"array":1}
    "divisions": {"array":16}
    "federal_circuit": {"number":40}
    "active": {"boolean":196}
    "bankruptcy": {"null":1}
    "notes": {"string":1196,"null":7}
    "parent": {"string":2143,"null":7}
    "lower_courts": {"array":70}
    "division_type": {"string":23}
    "url": {"string":1}
    "reorganization_dates": {"array":2}
    "division": {"array":1,"string":1}
    "cites": {"array":4}
}

% cat courts_db/data/courts.json | jq 'map(.dates[] | map_values(type)) | reduce (.[] | to_entries[]) as $entry ({}; .[$entry.key][$entry.value] += 1)'
{
    "end": {"null":2350,"string":495}
    "start": {"null":1791,"string":1054}
    "reorganization": {"array":6,"string":2}
    "reason": {"string":3}
    "notes": {"string":34}
    "reorg": {"array":1}
    "reorganization_dates": {"array":1}
    "name": {"string":8}
}
```
"""


@final
class DateRange(TypedDict):
    start: str | None  # YYYY-MM-DD
    end: str | None  # YYYY-MM-DD
    reorganization: NotRequired[list[str]]
    notes: NotRequired[str]
    name: NotRequired[str]
    reason: NotRequired[str]


@final
class CourtDict(TypedDict):
    active: NotRequired[bool]
    case_types: NotRequired[list[str]]
    citation_string: str
    court_url: NotRequired[str | None]
    dates: list[DateRange]
    examples: list[str]
    id: str
    level: NotRequired[str | None]
    location: str
    name: str
    regex: list[str]
    system: str
    type: str | None
    notes: NotRequired[str | None]
    name_abbreviation: NotRequired[str | None]
    jurisdiction: NotRequired[str | None]
    parent: NotRequired[str | None]
    locations: NotRequired[int]
    cites: NotRequired[list[str]]
    sub_names: NotRequired[list[str]]
    divisions: NotRequired[list[str]]
    division_type: NotRequired[str]
    federal_circuit: NotRequired[int]
    lower_courts: NotRequired[list[str]]
    appeal_to: NotRequired[str | None]
