---
slug: "sacch-c8"
url: "/mobilnisite/slovnik/sacch-c8/"
type: "slovnik"
title: "SACCH/C8 – Slow Associated Control CHannel/SDCCH/8"
date: 2025-01-01
abbr: "SACCH/C8"
fullName: "Slow Associated Control CHannel/SDCCH/8"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sacch-c8/"
summary: "Specifická konfigurace SACCH přidružená ke kanálu SDCCH/8 (Standalone Dedicated Control Channel s 8 podkanály). Plní stejnou řídicí funkci jako SACCH/C4, ale pro konfiguraci SDCCH s vyšší kapacitou, p"
---

SACCH/C8 je konfigurace pomalého přidruženého řídicího kanálu (Slow Associated Control Channel) používaná s kanálem SDCCH/8, která poskytuje signalizační a řídicí funkce pro jeho vyšší uživatelskou kapacitu.

## Popis

[SACCH](/mobilnisite/slovnik/sacch/)/C8 označuje pomalý přidružený řídicí kanál (Slow Associated Control CHannel), který je přidružen ke konfiguraci [SDCCH](/mobilnisite/slovnik/sdcch/)/8 v sítích GSM. SDCCH/8 je multiplexní konfigurace, ve které je osm nezávislých podkanálů SDCCH mapováno na jeden fyzický kanál (jeden časový slot). Tato konfigurace umožňuje vyšší hustotu současných signalizačních uživatelů ve srovnání se SDCCH/4, což efektivněji využívá omezené rádiové zdroje v vytížených buňkách. SACCH/C8 je přidružený řídicí kanál spárovaný s touto konkrétní strukturou SDCCH/8.

Architektura sleduje stejný princip jako [SACCH/C4](/mobilnisite/slovnik/sacch-c4/), ale v rámci navrženém pro vyšší kapacitu. SDCCH/8 a jeho přidružený SACCH/C8 jsou mapovány na 51-rámcový multirámec. Multiplexní schéma přiděluje specifické rámce v tomto multirámci osmi podkanálům SDCCH a jejich odpovídajícím zdrojům SACCH. Každý z osmi logických podkanálů SDCCH má vyhrazený, periodický časový slot pro svůj přidružený SACCH/C8. Tím vzniká osm paralelních pomalých přidružených řídicích kanálů, jeden pro každého signalizačního uživatele, všechny odvozené ze stejného fyzického časového slotu.

Provozně, když je mobilní stanici přidělen jeden z osmi podkanálů SDCCH, získá také přístup k odpovídajícímu zdroji SACCH/C8. Mobil používá tento kanál k vysílání periodických měřicích hlášení ([RXLEV](/mobilnisite/slovnik/rxlev/), [RXQUAL](/mobilnisite/slovnik/rxqual/)) k podsystému základnové stanice ([BSS](/mobilnisite/slovnik/bss/)). Tato hlášení informují síť o síle a kvalitě signálu na downlinku z obsluhované a sousedních buněk. Současně síť používá SACCH/C8 k odesílání příkazů mobilu, jako jsou příkazy pro úpravu vysílacího výkonu (řízení výkonu) a aktualizaci hodnoty časového předstihu (Timing Advance). Tato kontinuální výměna probíhá na pozadí, zatímco hlavní signalizační dialog (např. nastavení hovoru prostřednictvím [CM](/mobilnisite/slovnik/cm/) SERVICE REQUEST) probíhá na hlavním podkanálu SDCCH. Tím je zajištěno, že dohled rádiového spoje je udržován pro všech osm uživatelů sdílejících fyzický kanál, což zabraňuje signalizačním selháním způsobeným nezjištěným zhoršením rádiových podmínek a připravuje každý mobil na potenciální následné přidělení na hovorový kanál.

## K čemu slouží

Účelem [SACCH](/mobilnisite/slovnik/sacch/)/C8 je poskytnout základní funkčnost přidruženého řídicího kanálu pro konfiguraci SDCCH/8 s vysokou kapacitou. Jak se sítě GSM vyvíjely a hustota účastníků rostla, vznikla potřeba podporovat více simultánních signalizačních transakcí (nastavení hovorů, SMS, aktualizace polohy) na jeden rádiový nosič. Konfigurace SDCCH/8 byla vyvinuta pro multiplexování osmi signalizačních kanálů do jednoho časového slotu, čímž zdvojnásobila kapacitu oproti SDCCH/4. SACCH/C8 byl nezbytný k doprovodu této konfigurace, aby byla zajištěna zachování kritických funkcí dohledu nad rádiovým spojem a řízení SACCH pro všech osm uživatelů.

Bez přidruženého SACCH pro SDCCH/8 by síť ztratila schopnost monitorovat kvalitu spoje a řídit rádiové parametry mobilu během těchto signalizačních fází s vysokou hustotou. To by učinilo signalizační procedury méně robustními a mohlo by vést k vyšší míře selhání v vytížených městských buňkách. SACCH/C8 to řeší rozšířením zavedeného paradigmatu SACCH na spektrálně efektivnější strukturu SDCCH/8. Umožňuje operátorům sítí zvýšit signalizační kapacitu bez obětování spolehlivosti řídicích mechanismů, které jsou zásadní pro provoz GSM, jako je příprava předávání hovoru na základě měření a řízení výkonu, a to i během počáteční fáze přístupu k síti.

## Klíčové vlastnosti

- Specificky přidružen ke konfiguraci signalizačního kanálu SDCCH/8 s vysokou kapacitou
- Podporuje osm paralelních přidružených řídicích kanálů na jednom fyzickém časovém slotu
- Funguje v rámci 51-rámcové multirámcové struktury pro řídicí kanály
- Poskytuje dohled nad rádiovým spojem pro každého uživatele na podkanálu SDCCH/8
- Přenáší měřicí hlášení a nese příkazy pro řízení výkonu a časového předstihu
- Umožňuje efektivní a spolehlivou signalizaci pro scénáře s vysokou hustotou uživatelů

## Související pojmy

- [SDCCH – Stand-Alone Dedicated Control Channel](/mobilnisite/slovnik/sdcch/)
- [SACCH – Standalone Associated Control CHannel](/mobilnisite/slovnik/sacch/)
- [SACCH/C4 – Slow Associated Control CHannel/SDCCH/4](/mobilnisite/slovnik/sacch-c4/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [SACCH/C8 na 3GPP Explorer](https://3gpp-explorer.com/glossary/sacch-c8/)
