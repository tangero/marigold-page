---
slug: "v-chf"
url: "/mobilnisite/slovnik/v-chf/"
type: "slovnik"
title: "V-CHF – Visited Charging Function"
date: 2025-01-01
abbr: "V-CHF"
fullName: "Visited Charging Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/v-chf/"
summary: "Funkce účtování (CHF) umístěná ve navštívené veřejné pozemní mobilní síti (VPLMN). Umožňuje účtování v reálném čase pro roamující účastníky prostřednictvím rozhraní s CHF domovské sítě. Je klíčová pro"
---

V-CHF je funkce účtování (Charging Function) umístěná ve navštívené veřejné pozemní mobilní síti (Visited PLMN), která umožňuje účtování v reálném čase pro roamující účastníky prostřednictvím rozhraní s CHF domovské sítě.

## Popis

Funkce účtování v navštívené síti (V-CHF) je prvek jádra sítě specifikovaný v architektuře 5G systému (5GS) pro správu účtovacích operací pro uživatelská zařízení (UE), která roamují mimo svou domovskou síť. Nachází se ve navštívené veřejné pozemní mobilní síti ([VPLMN](/mobilnisite/slovnik/vplmn/)) a pracuje ve spolupráci s domovskou funkcí účtování (H-CHF) umístěnou v domovské veřejné pozemní mobilní síti ([HPLMN](/mobilnisite/slovnik/hplmn/)). Hlavní architektonickou rolí V-CHF je fungovat jako účtovací brána v navštívené síti, která sbírá data o využití a předává je H-CHF pro centralizované účtování a rozhodování o politikách.

Operačně V-CHF komunikuje s funkcí správy relací ([SMF](/mobilnisite/slovnik/smf/)) ve VPLMN přes referenční bod N40. Když je navázána roamující relace, SMF komunikuje s V-CHF, aby hlásila účtovací události na základě datového využití účastníka, spotřeby služeb nebo konkrétních síťových událostí. V-CHF aplikuje lokální účtovací politiky, které mohou být odvozeny od domovské sítě, aby generovala záznamy o účtovacích datech ([CDR](/mobilnisite/slovnik/cdr/)) nebo předávala účtovací události v reálném čase. Pro komunikaci s H-CHF využívá rozhraní Nchf (konkrétně Nchf_ConvergedCharging), čímž zajišťuje bezpečné předání všech účtovacích informací do fakturačního systému domovského operátora.

Klíčové součásti funkčnosti V-CHF zahrnují schopnost podporovat jak offline, tak online modely účtování. V online účtování může v reálném čase žádat o přidělení kvót od H-CHF a spravovat je za účelem kontroly využití služeb. Její role je klíčová pro umožnění plynulého roamování tím, že zajišťuje přesné účtování v souladu s mezispolečenskými dohodami a nezavádí latenci, která by zhoršovala uživatelský zážitek. V-CHF je základní součástí architektury účtování v 5G, která odděluje účtovací akce v navštívené síti od konečné fakturační autority domovské sítě.

## K čemu slouží

V-CHF byla zavedena, aby řešila složitost účtování v roamujících scénářích 5G, kde služby poskytuje navštívená síť, ale účtuje je síť domovská. Před její standardizací se roamující účtování často spoléhalo na jednodušší, méně real-time mechanismy, které mohly vést k nepřesnostem ve fakturaci, podvodům nebo omezené podpoře nových servisních modelů, jako je síťové dělení (network slicing) a edge computing. Oddělení účtovacích funkcí mezi navštívenou a domovskou sítí umožňuje podrobnější a okamžitou kontrolu využití zdrojů.

Její vznik motivovala potřeba standardizovaného, interoperabilního rozhraní pro konvergované účtování přes hranice sítí, jak je definováno ve 3GPP Release 16. To umožňuje operátorům implementovat pokročilé účtovací politiky pro roamující účastníky, včetně podpory servisně orientované architektury ([SBA](/mobilnisite/slovnik/sba/)) a bezproblémové integrace s řízením politik. V-CHF řeší problém, jak efektivně a bezpečně hlásit data o využití z navštívené sítě do fakturačních systémů domovské sítě, aniž by vyžadovala přímou integraci mezi každým síťovým prvkem, čímž zjednodušuje účtovací architekturu pro roaming.

## Klíčové vlastnosti

- Umístěna ve navštívené veřejné pozemní mobilní síti (VPLMN)
- Komunikuje s SMF ve VPLMN přes referenční bod N40
- Komunikuje s domovskou CHF (H-CHF) přes rozhraní Nchf_ConvergedCharging
- Podporuje jak online, tak offline modely účtování pro roamující uživatele
- Generuje a předává záznamy o účtovacích datech (CDR) nebo účtovací události
- Aplikuje účtovací politiky přijaté od domovské sítě

## Související pojmy

- [CHF – Charging Function](/mobilnisite/slovnik/chf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 32.256** (Rel-19) — 5G Connection & Mobility Charging Spec
- **TR 33.928** (Rel-19) — ADMF Logic for LI Provisioning

---

📖 **Anglický originál a plná specifikace:** [V-CHF na 3GPP Explorer](https://3gpp-explorer.com/glossary/v-chf/)
