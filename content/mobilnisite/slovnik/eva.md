---
slug: "eva"
url: "/mobilnisite/slovnik/eva/"
type: "slovnik"
title: "EVA – Enhanced Vulnerability Analysis"
date: 2025-01-01
abbr: "EVA"
fullName: "Enhanced Vulnerability Analysis"
category: "Security"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/eva/"
summary: "Systematická metodika bezpečnostního hodnocení v rámci 3GPP pro identifikaci, analýzu a zmírňování zranitelností v síťových funkcích a protokolech. Je klíčová pro proaktivní posilování bezpečnostní od"
---

EVA je systematická metodika bezpečnostního hodnocení podle 3GPP pro identifikaci, analýzu a zmírňování zranitelností v síťových funkcích a protokolech s cílem proaktivně posílit bezpečnost mobilních sítí.

## Popis

Enhanced Vulnerability Analysis (EVA) je formalizovaný proces definovaný 3GPP pro hodnocení bezpečnostní odolnosti síťových prvků a komunikačních protokolů. Funguje jako strukturovaná metodika, která provádí bezpečnostní analytiky procesem identifikace potenciálních slabin, posouzení jejich zneužitelnosti a dopadu a doporučení vhodných protiopatření. Proces je integrován do životního cyklu standardizace a je často aplikován během fáze specifikace nových funkcí nebo při významných změnách stávajících systémů.

Analýza typicky zahrnuje modelování hrozeb, kdy je hodnocený systém rozložen na části za účelem pochopení jeho aktiv, hranic důvěry a toků dat. Analytici poté systematicky zkoumají tyto komponenty na přítomnost zranitelností, které by mohly být zneužity k narušení důvěrnosti, integrity nebo dostupnosti. To zahrnuje revizi specifikací protokolů kvůli logickým chybám, implementačním předpokladům, které by mohly být porušeny, a potenciálním chybným konfiguracím. Výstupem je podrobná zpráva, která kategorizuje zranitelnosti a navrhuje zmírňující opatření, jež mohou být zpětně zapracovány do specifikace za účelem posílení návrhu před implementací.

Role EVA je zásadní pro zakotvení principů zabezpečení již v návrhu (security-by-design) do standardů 3GPP. Poskytuje společný rámec pro výrobce, operátory a bezpečnostní výzkumníky, aby mohli konzistentně hodnotit a komunikovat bezpečnostní rizika. Tím, že 3GPP vyžaduje nebo doporučuje provedení EVA pro kritické funkce, usiluje o snížení počtu zranitelností zavedených na architektonické úrovni, což vede k odolnějším sítím schopným lépe čelit útokům zaměřeným na jádrovou infrastrukturu mobilních sítí.

## K čemu slouží

EVA byla vytvořena jako odpověď na rostoucí složitost a spektrum hrozeb, kterým mobilní sítě čelí, zejména s přechodem na plně IP architektury v 3G a 4G. Dřívější bezpečnostní přístupy byly často reaktivní, spoléhaly se na penetrační testy až po implementaci nebo na reakci na veřejně odhalené zneužitelné chyby. To ponechávalo sítě zranitelné vůči chybám na úrovni návrhu, které jsou po nasazení nákladné a obtížně opravitelné. EVA zavádí proaktivní, systematickou analýzu během fáze standardizace, aby posunula bezpečnostní opatření dříve do životního cyklu vývoje.

Primárním problémem, který EVA řeší, je nekonzistentní a nahodilá povaha bezpečnostních analýz v telekomunikacích. Bez standardizované metodiky by různé skupiny mohly rizika hodnotit rozdílně, což by mohlo vést k přehlédnutí kritických zranitelností. EVA poskytuje opakovatelný, dokumentovaný proces, který zajišťuje základní úroveň prověření síťových funkcí, zejména těch, které zpracovávají citlivá data jako je autentizace, správa klíčů a uživatelský provoz. Motivací byla potřeba vybudovat důvěru v mobilní sítě, které se staly klíčovou infrastrukturou, podporující nejen hlas a [SMS](/mobilnisite/slovnik/sms/), ale také kritické datové služby, finanční transakce a IoT aplikace.

Institucionalizací analýzy zranitelností si 3GPP klade za cíl zlepšit celkovou bezpečnostní záruku svých specifikací. To pomáhá výrobcům síťového vybavení a mobilním operátorům nasazovat systémy s méně inherentními slabinami, čímž se snižuje prostor pro útoky a potenciál pro rozsáhlé kompromitování. Představuje posun od bezpečnosti jako dodatečně přidané funkce k jejímu začlenění jako nedílné součásti procesu architektonického návrhu.

## Klíčové vlastnosti

- Strukturovaná metodika pro systematické bezpečnostní hodnocení
- Integrace do životního cyklu vývoje specifikací 3GPP
- Zaměření na identifikaci zranitelností na úrovni návrhu a protokolu
- Modelování hrozeb pro definici hranic systému a jeho aktiv
- Vytváří akční zprávy s posouzením rizik a doporučeními pro zmírnění
- Usiluje o prosazení principů zabezpečení již v návrhu (security-by-design) v síťové architektuře

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 33.805** (Rel-12) — 3GPP Network Product Security Assurance Methodology
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.855** (Rel-13) — E-UTRA Positioning Enhancements Study
- **TS 36.878** (Rel-13) — LTE Performance Enhancements for High Speed Scenarios
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance

---

📖 **Anglický originál a plná specifikace:** [EVA na 3GPP Explorer](https://3gpp-explorer.com/glossary/eva/)
