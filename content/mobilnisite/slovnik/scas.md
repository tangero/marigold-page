---
slug: "scas"
url: "/mobilnisite/slovnik/scas/"
type: "slovnik"
title: "SCAS – 3GPP Security Assurance Specification"
date: 2026-01-01
abbr: "SCAS"
fullName: "3GPP Security Assurance Specification"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/scas/"
summary: "Soubor specifikací 3GPP, které definují metodiky bezpečnostního hodnocení a testování pro síťové produkty a komponenty. Poskytují společný rámec pro bezpečnostní záruky, což umožňuje dodavatelům, oper"
---

SCAS je soubor specifikací 3GPP, které definují metodiky bezpečnostního hodnocení a testování, aby poskytly společný rámec pro ověřování, že síťové produkty splňují bezpečnostní požadavky.

## Popis

Specifikace bezpečnostních záruk 3GPP (SCAS) je komplexní a klíčový rámec v rámci bezpečnostní architektury 3GPP. Nejde o jediný dokument, ale o rodinu technických specifikací (TS), které definují metodiku pro hodnocení bezpečnosti konkrétních síťových produktů 3GPP. Rámec SCAS stanovuje standardizovanou sadu bezpečnostních požadavků, účelů testů a testovacích případů šitých na míru jednotlivým typům síťových prvků, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)), Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)), Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) a mnoho dalších, včetně 5G prvků jako [AMF](/mobilnisite/slovnik/amf/) a [SMF](/mobilnisite/slovnik/smf/). Jeho hlavním cílem je poskytnout záruku, že implementace produktu je v souladu s bezpečnostními ustanoveními popsanými ve specifikacích systémové architektury 3GPP (např. řada TS 33).

SCAS funguje tak, že rozkládá vysoké bezpečnostní cíle ze specifikací architektury na konkrétní, testovatelná tvrzení. Pro každý definovaný síťový prvek je vytvořen samostatný dokument SCAS (např. TS 33.117 pro HSS, TS 33.516 pro AMF). Tento dokument obvykle obsahuje několik klíčových částí: definici bezpečnostního problému, který uvádí hrozby, proti nimž se musí produkt bránit; sadu Bezpečnostních funkčních požadavků ([SFR](/mobilnisite/slovnik/sfr/)) odvozených ze specifikací bezpečnosti 3GPP; a podrobnou sadu testovacích případů navržených k ověření každého SFR. Testovací případy specifikují konfiguraci testu, postupy, očekávané výsledky a často i úroveň závažnosti testu. Tato metodika je úzce provázána s koncepty mezinárodních společných kritérií a poskytuje strukturovaný životní cyklus záruk.

Z architektonického hlediska stojí rámec SCAS mezi specifikacemi návrhu systému 3GPP a procesy certifikace reálných produktů prováděnými laboratořemi a průmyslovými skupinami, jako je schéma [NESAS](/mobilnisite/slovnik/nesas/) (Network Equipment Security Assurance Scheme) od GSMA. Dodavatelé používají dokumenty SCAS během svých vývojových fází a fází interního bezpečnostního testování. Nezávislé bezpečnostní zkušební laboratoře je používají jako základ pro formální testování shody. Mobilní síťoví operátoři se na shodu se SCAS odvolávají při pořizování zařízení, protože poskytuje standardizované měřítko bezpečnostní odolnosti. Rámec pokrývá širokou škálu bezpečnostních aspektů, včetně implementace kryptografických algoritmů, zabezpečených protokolů (např. NAS, Diameter, HTTP/2), řízení přístupu, auditování logů, odolnosti proti útokům typu denial-of-service a bezpečnosti rozhraní pro provoz a údržbu. Poskytnutím této společné testovací základny SCAS snižuje nejednoznačnost, brání uzamčení u dodavatele kvůli proprietárním bezpečnostním tvrzením a zvyšuje celkovou bezpečnostní úroveň globálních mobilních sítí.

## K čemu slouží

Rámec SCAS byl vytvořen, aby zaplnil kritickou mezeru v raném nasazení sítí 3G a 4G: nedostatek standardizovaného, objektivního prostředku pro ověření bezpečnostní implementace síťového zařízení. Zatímco specifikace 3GPP pečlivě definovaly, *jaké* bezpečnostní funkce by systém měl mít (např. vzájemné ověřování, šifrování), původně nespecifikovaly, *jak* testovat, zda produkt dodavatele tyto funkce implementoval správně a robustně. To vedlo k potenciálním zranitelnostem způsobeným implementačními chybami, chybami konfigurace nebo neúplnou podporou funkcí, které mohly být zneužity k narušení integrity sítě a soukromí účastníků.

Motivace pro SCAS vycházela z rostoucích obav operátorů a regulátorů ohledně bezpečnosti dodavatelského řetězce a potřeby vzájemného uznávání bezpečnostních hodnocení na různých trzích. Před SCAS museli operátoři provádět vlastní, často duplicitní a nekonzistentní bezpečnostní posouzení zařízení dodavatelů. To bylo nákladné, časově náročné a nezaručovalo konzistentní bezpečnostní laťku. SCAS tento problém řeší tím, že poskytuje jednotnou metodiku záruk definovanou 3GPP. Umožňuje dodavatelům navrhovat podle známé sady testovatelných požadavků, umožňuje laboratořím provádět hodnocení konzistentně a dává operátorům jistotu, že certifikované zařízení prošlo důkladným, standardizovaným testováním. Jeho vývoj byl historicky provázán a podporuje širší průmyslové iniciativy, jako je NESAS, které používá SCAS jako svou technickou základnu. SCAS řeší omezení předchozího ad-hoc přístupu zavedením předvídatelnosti, opakovatelnosti a transparentnosti do bezpečnostního hodnocení síťových produktů, což je zásadní pro budování důvěry v stále více softwarově definované a virtualizované sítě 5G.

## Klíčové vlastnosti

- Standardizovaná metodika bezpečnostního testování pro síťové prvky 3GPP
- Definuje produktově specifické Bezpečnostní funkční požadavky (SFR)
- Poskytuje podrobné testovací případy pro ověření implementace dodavatele
- Slučuje se s koncepty společných kritérií pro bezpečnostní hodnocení
- Tvoří technický základ pro průmyslová schémata jako GSMA NESAS
- Pokrývá širokou škálu prvků od EPC po 5GC (např. HSS, AMF, UPF)

## Související pojmy

- [NESAS – Network Equipment Security Assurance Scheme](/mobilnisite/slovnik/nesas/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TS 33.515** (Rel-20) — 5G SMF Security Assurance Specification
- **TS 33.805** (Rel-12) — 3GPP Network Product Security Assurance Methodology
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)
- **TR 33.926** (Rel-20) — Security Assurance Specification (SCAS)
- **TR 33.927** (Rel-19) — Security Assurance for Virtualized Network Products

---

📖 **Anglický originál a plná specifikace:** [SCAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/scas/)
