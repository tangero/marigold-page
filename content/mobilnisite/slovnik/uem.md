---
slug: "uem"
url: "/mobilnisite/slovnik/uem/"
type: "slovnik"
title: "UEM – Unwanted Emissions Mask"
date: 2025-01-01
abbr: "UEM"
fullName: "Unwanted Emissions Mask"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/uem/"
summary: "Maska nežádoucích emisí (Unwanted Emissions Mask – UEM) je regulační a technická specifikace definující přípustné limity rádiových emisí mimo přidělenou šířku přenosového pásma vysílače. Zajišťuje, ab"
---

UEM je regulační specifikace definující přípustné limity rádiových emisí vysílače mimo jeho přidělenou šířku přenosového pásma, aby se zabránilo škodlivému rušení jiných systémů.

## Popis

Maska nežádoucích emisí (Unwanted Emissions Mask – UEM) je soubor limitů specifikovaných v technických dokumentech 3GPP, které omezují mimopásmové a parazitní emise rádiových vysílačů. Nežádoucí emise se skládají z několika složek: Mimopásmové emise (Out-of-Band Emissions – [OOBE](/mobilnisite/slovnik/oobe/)), což jsou emise bezprostředně mimo přidělenou šířku kanálu způsobené modulací a nelinearitami výkonového zesilovače; a Parazitní emise (Spurious Emissions), což jsou emise na kmitočtech vzdálených od nosné, často způsobené harmonickými složkami, intermodulací nebo šumem hodin. UEM definuje profil výkonového limitu v rozsahu kmitočtů odstupujících od středu nosné.

Z architektonického hlediska je UEM požadavek kladený na návrh rádiového vysílače, který ovlivňuje vysokofrekvenční koncový stupeň, výkonový zesilovač, filtraci a digitální zpracování signálu. Měří se během testů shody zařízení. Maska je typicky definována jako maximální přípustná úroveň výkonu (v dBm) v rámci specifikované měřicí šířky pásma při daném kmitočtovém odstupu od okraje šířky pásma kanálu. Pro základnové stanice ([BS](/mobilnisite/slovnik/bs/)) a uživatelská zařízení (UE) mohou platit různé masky a mohou se lišit v závislosti na provozním pásmu a technologii (např. LTE vs. NR).

Její role je zásadní pro správu spektra a zamezení rušení. Dodržováním UEM zajišťuje zařízení vyhovující 3GPP, že neznečišťuje rádiové spektrum, a chrání tak služby v sousedních pásmech (což mohou být jiné buněčné systémy, Wi-Fi, radary nebo satelitní spoje). Dodržování UEM je povinné pro regulační schválení (např. [FCC](/mobilnisite/slovnik/fcc/) nebo [ETSI](/mobilnisite/slovnik/etsi/)). Specifikace (37.809, 37.810, 38.104 atd.) poskytují podrobné číselné limity a testovací metodiky pro ověřování těchto emisí.

## K čemu slouží

UEM existuje, aby umožnila pokojnou koexistenci více rádiových systémů v přeplněném rádiovém spektru. Bez přísných limitů pro nežádoucí emise by mohla výkonná 5G základnová stanice desenzibilizovat přijímače blízkého 4G systému nebo i necelaulární služby. Historicky, jak se buněčná technologie vyvíjela s širšími šířkami pásma a složitější modulací (např. od GSM k 5G NR), rostl i potenciál pro nežádoucí emise, což si vyžádalo propracovanější a přísnější masky.

Řeší technickou výzvu navrhování účinných vysokoenergetických vysílačů, které jsou zároveň 'čisté'. Motivací pro její kontinuální vývoj napříč verzemi jsou nové alokace spektra (např. nová pásma NR), zavedení technologií jako je agregace nosných (která kombinuje více nosných a ovlivňuje profil emisí) a potřeba globální harmonizace standardů zařízení. Každá verze aktualizuje limity UEM, aby vyvážila technickou proveditelnost s požadavky na ochranu spektra.

## Klíčové vlastnosti

- Definuje limity pro mimopásmové emise (Out-of-Band Emissions – OOBE)
- Definuje limity pro parazitní emise (Spurious Emissions)
- Konkrétní limity se liší podle typu zařízení (BS/UE) a kmitočtového pásma
- Kritické pro regulační shodu a typové schválení
- Zajišťuje koexistenci s jinými rádiovými službami
- Podrobně popsány v RF specifikacích pro testy shody

## Související pojmy

- [OOBE – Out-Of-Band Emission](/mobilnisite/slovnik/oobe/)

## Definující specifikace

- **TS 37.809** (Rel-11) — E-UTRA & MSR BS Class Requirements
- **TS 37.810** (Rel-12) — Study on Base Station Specification Structure
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.194** (Rel-19) — Ambient IoT Base Station RF Spec
- **TS 38.817** — 3GPP TR 38.817

---

📖 **Anglický originál a plná specifikace:** [UEM na 3GPP Explorer](https://3gpp-explorer.com/glossary/uem/)
