---
slug: "pixit"
url: "/mobilnisite/slovnik/pixit/"
type: "slovnik"
title: "PIXIT – Protocol Implementation eXtra Information for Testing"
date: 2025-01-01
abbr: "PIXIT"
fullName: "Protocol Implementation eXtra Information for Testing"
category: "Management"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/pixit/"
summary: "PIXIT (Protocol Implementation eXtra Information for Testing) je dokument používaný při testování shody podle 3GPP, konkrétně pro rádiový přístupový síť (RAN). Poskytuje implementačně specifické param"
---

PIXIT je dokument, který poskytuje implementačně specifické parametry a konfigurace potřebné ke správnému provedení testů shody 3GPP pro konkrétní uživatelské zařízení (UE) nebo síťovou techniku.

## Popis

Protocol Implementation eXtra Information for Testing (PIXIT) je klíčovou součástí rámce pro testování shody podle 3GPP, zejména pro testování uživatelských zařízení (UE) a základnových stanic. Nejde o protokol samotný, ale o strukturovanou sadu dat – často ve formě tabulky nebo konfiguračního souboru – která doplňuje formální specifikace testovacích případů ([TC](/mobilnisite/slovnik/tc/)). PIXIT obsahuje implementačně závislé parametry, které nejsou definovány v základních standardech protokolů, ale jsou nezbytné pro to, aby testovací systém mohl správně stimulovat testovanou implementaci ([IUT](/mobilnisite/slovnik/iut/)) a vyhodnocovat její odpovědi.

V praxi, když testovací laboratoř provádí testovací případ shody ze specifikace jako je 38.523 (5G NR), abstraktní testovací procedura vyžaduje konkrétní hodnoty pro četné proměnné. Ty zahrnují schopnosti UE (např. podporované šířky pásma, počet antén), rádiové konfigurace (např. konkrétní kmitočtová pásma, rozestupy podnosných) a dokonce i časovací parametry. Soubor PIXIT, který dodává výrobce zařízení, poskytuje tyto konkrétní hodnoty pro jejich specifickou implementaci. Testovací systém tyto informace používá ke konfiguraci testovací techniky (např. emulátoru základnové stanice) a k přizpůsobení testovací sekvence deklarovaným schopnostem IUT.

Architektura PIXIT je založena na tabulkách a typicky mapuje identifikátory parametrů (PIXIT Proforma) z testovací specifikace na skutečné hodnoty. Jeho úlohou je překlenout propast mezi obecnými, standardem definovanými testovacími případy a nekonečnou rozmanitostí reálných implementací. Bez PIXIT by testování shody nebylo možné, protože testovacímu systému by chyběl potřebný kontext pro komunikaci s IUT. Je to základní prvek pro zajištění toho, že zařízení, které deklaruje shodu se standardy 3GPP, bylo ověřeno za podmínek přesně odpovídajících jeho zamýšlenému provozu.

## K čemu slouží

PIXIT existuje proto, aby řešil základní problém aplikace obecných, standardizovaných testovacích procedur na konkrétní, jedinečné implementace produktů. Testovací specifikace 3GPP definují 'co' testovat abstraktním způsobem, ale nemohou předepsat 'jak' pro každou možnou konfiguraci zařízení. Účelem PIXIT je poskytnout tuto chybějící implementačně specifickou informaci 'jak', což umožňuje reprodukovatelné a přesné testování shody napříč různými výrobci a variantami produktů.

Motivace pro jeho vytvoření spočívá ve složitosti a konfigurovatelnosti moderních rádiových zařízení. Jeden rádiový standard 3GPP, jako je 5G NR, podporuje obrovskou škálu možností: kmitočtová pásma, šířky pásma, kombinace agregace nosných a sady funkcí. Testovací případ musí být proveden s konkrétní kombinací těchto možností, aby byl vykonatelný. PIXIT formalizuje proces, kterým výrobce tyto možnosti deklaruje, a zajišťuje, že testovací laboratoř vyhodnocuje zařízení podle schopností, které skutečně implementuje. Tím se předchází selhání testů z důvodu chybné konfigurace spíše než z důvodu nedodržení protokolu.

Historicky, jak se rádiové standardy vyvíjely od jednodušších systémů 2G k vysoce komplexním systémům 4G a 5G, potřeba takového strukturovaného dokumentu s doplňujícími informacemi se stala prvořadou. Řeší omezení dřívějších, méně formalizovaných metod, kdy se testovací parametry mohly předávat ad-hoc, což vedlo k nekonzistentnostem a problémům s interoperabilitou. PIXIT zajišťuje, že proces testování shody je jak důsledný, tak spravedlivý, což je nezbytné pro globální přístup na trh a interoperabilitu sítí.

## Klíčové vlastnosti

- Poskytuje implementačně specifické parametry pro provádění abstraktních testovacích případů
- Strukturovaný formát (např. TSV, XML) mapující identifikátory parametrů na konkrétní hodnoty
- Nezbytný pro konfiguraci zařízení testovacího systému (např. emulátorů základnových stanic)
- Pokrývá schopnosti UE, konfigurace rádiových zdrojů a možnosti protokolů
- Umožňuje reprodukovatelné testování v různých laboratořích a pro různé varianty zařízení
- Formální součást balíčku pro předložení testu shody 3GPP

## Související pojmy

- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)

## Definující specifikace

- **TS 36.523** (Rel-19) — UE Conformance Test Spec for Idle Mode
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.522** (Rel-19) — UE Conformance Test Applicability Statement
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [PIXIT na 3GPP Explorer](https://3gpp-explorer.com/glossary/pixit/)
