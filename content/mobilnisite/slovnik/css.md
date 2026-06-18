---
slug: "css"
url: "/mobilnisite/slovnik/css/"
type: "slovnik"
title: "CSS – Composite Source Signal"
date: 2025-01-01
abbr: "CSS"
fullName: "Composite Source Signal"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/css/"
summary: "Composite Source Signal (CSS) je standardizovaný testovací signál používaný v testování shody 3GPP pro zvukové a řečové kodeky. Poskytuje konzistentní, reprodukovatelnou referenci pro hodnocení výkonu"
---

CSS je standardizovaný testovací signál 3GPP, který poskytuje konzistentní referenci pro hodnocení výkonu, kvality a interoperability zvukových a řečových kodeků během testování shody.

## Popis

Composite Source Signal (CSS) je přesně definovaný umělý testovací signál specifikovaný 3GPP pro objektivní hodnocení výkonu řečových a zvukových kodeků. Není funkční součástí architektury živé sítě, ale klíčovým nástrojem ve fázích vývoje, ověřování a schvalování typu. CSS je navržen tak, aby simuloval komplexní, náročný akustický scénář, který zatěžuje algoritmy kodeků, což inženýrům umožňuje měřit klíčové ukazatele výkonu, jako je kvalita řeči, odolnost proti šumu a zpracovatelské zpoždění za kontrolovaných, opakovatelných laboratorních podmínek.

Samotný signál je složený průběh generovaný smícháním více zvukových zdrojů podle přesného receptu definovaného v příslušných testovacích specifikacích 3GPP (např. TS 26.132, TS 26.907). Typicky kombinuje prvky jako čisté řečové vzorky, šum pozadí různých typů (např. hladina hovorů, automobilový, uliční) a někdy i tónové rušiče nebo hudbu. Specifické úrovně, spektrální charakteristiky a časové zarovnání těchto složek jsou standardizovány, aby vytvořily testovací podmínku reprezentující 'nejhorší případ' nebo vysoce reprezentativní stav. Tato složená povaha je klíčová, protože přesahuje testování jednoduchými, čistými řečovými signály a hodnotí, jak si kodek poradí se složitým, hlučným zvukem, s nímž se setkáváme v reálném použití.

Během testování je CSS přiváděn jako vstup do testovaného kodeku nebo zařízení. Výstup z řetězce kódování a dekódování kodeku (nebo koncová přenosová cesta v systémovém testu) je následně analyzován. Tato analýza využívá objektivní algoritmy pro měření percepční kvality, jako je [POLQA](/mobilnisite/slovnik/polqa/) (Perceptual Objective Listening Quality Analysis) nebo [PESQ](/mobilnisite/slovnik/pesq/) (Perceptual Evaluation of Speech Quality), které porovnávají degradovaný výstupní signál s původní referenční CSS. Výsledné skóre, například střední hodnota známky kvality (Mean Opinion Score, [MOS](/mobilnisite/slovnik/mos/)), kvantifikuje výkon kodeku. Úlohou CSS je poskytovat neměnnou, kvalitní referenci, vůči níž jsou všechna tato měření prováděna, což zajišťuje srovnatelnost výsledků testů napříč různými laboratořemi, výrobci a testovacími kampaněmi.

Specifikace upravující CSS (např. TS 26.132 pro řeč, TS 26.907 pro zvuk) podrobně popisují jeho přesné složení, digitální formát a postupy použití. Dodržování těchto testovacích specifikací, včetně správné aplikace CSS, je povinné pro síťová zařízení a uživatelská zařízení usilující o certifikaci 3GPP. Proto je CSS, byť pro koncového uživatele neviditelný, základním prvkem v ekosystému zajištění kvality, který garantuje, že hlasové a zvukové služby v sítích 3GPP splňují minimální standardy výkonu a poskytují konzistentní uživatelský zážitek.

## K čemu slouží

Composite Source Signal byl vytvořen k řešení základního problému nekonzistentního a neopakovatelného testování kodeků. Před jeho standardizací mohli různí výrobci a zkušebny používat vlastní proprietární testovací signály nebo jednoduché tóny k hodnocení výkonu kodeků. To znemožňovalo přímé srovnání výsledků mezi zařízeními různých dodavatelů a nebylo možné si být jisti, že zařízení certifikované jednou laboratoří bude adekvátně fungovat v jiné síti. CSS poskytuje univerzální, náročný etalon, který zajišťuje, že všechny strany testují vůči stejnému přísnému standardu.

Jeho vývoj byl motivován potřebou robustních metodik objektivního testování s tím, jak se mobilní sítě vyvíjely a zaváděly pokročilejší a někdy složitější řečové a zvukové kodeky (jako [AMR](/mobilnisite/slovnik/amr/), [AMR-WB](/mobilnisite/slovnik/amr-wb/) a později [EVS](/mobilnisite/slovnik/evs/)). Tyto kodeky využívají sofistikované techniky, jako je potlačení šumu, nespojitý přenos ([DTX](/mobilnisite/slovnik/dtx/)) a maskování ztrát paketů. K řádnému posouzení těchto funkcí je jednoduchý čistý řečový signál nedostatečný. CSS se svou směsí řeči a šumu efektivně testuje schopnost kodeku zvládat reálné akustické prostředí, čímž zajišťuje, že kvalita je zachována nejen v tichých kancelářích, ale také v hlučných ulicích nebo jedoucích vozidlech.

Zavedením této společné referenční signálové základny umožnilo 3GPP efektivní procesy testování shody a schvalování typu. Umožňuje regulačním orgánům a síťovým operátorům definovat jasná, měřitelná kritéria úspěšnosti/neúspěšnosti pro zvukovou kvalitu. To následně pohání zlepšování kvality napříč odvětvím, protože výrobci kodeků a zařízení musí optimalizovat své implementace, aby dobře fungovaly při testování standardizovaným CSS. V konečném důsledku chrání zážitek koncového uživatele tím, že zajišťuje základní úroveň zvukového výkonu pro všechna certifikovaná zařízení v síti.

## Klíčové vlastnosti

- Standardizované složení průběhu pro opakovatelné testování
- Kombinuje více zvukových zdrojů (řeč, šum, rušiče) k simulaci komplexních akustických scén
- Slouží jako povinný referenční signál pro testy shody zvukových kodeků 3GPP
- Umožňuje objektivní měření kvality pomocí algoritmů jako POLQA a PESQ
- Poskytuje náročný etalon pro zatěžovací testování odolnosti a výkonu kodeků
- Zajišťuje srovnatelnost výsledků testů napříč různými laboratořemi a výrobci

## Související pojmy

- [POLQA – Perceptual Objective Listening Quality Assessment](/mobilnisite/slovnik/polqa/)
- [PESQ – Perceptual Evaluation of Speech Quality](/mobilnisite/slovnik/pesq/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.012** (Rel-19) — Circuit Switched Location Management Procedures
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.844** (Rel-12) — IMS P2P Content Distribution Services Study
- **TS 25.700** (Rel-12) — Further Enhanced Uplink (EUL) Study
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 26.307** (Rel-19) — 3GPP HTML5 Profile Specification
- **TR 26.907** (Rel-19) — HTML5 for 3GPP Services Study
- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download
- **TS 29.272** (Rel-19) — Diameter Interfaces for MME/SGSN
- **TS 32.373** (Rel-9) — IRP Security Services CORBA Solution
- **TS 32.376** (Rel-19) — Security services for IRP Solution Set
- **TS 33.701** (Rel-19) — Study on mitigations against bidding down attacks
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [CSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/css/)
