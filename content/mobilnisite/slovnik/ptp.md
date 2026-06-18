---
slug: "ptp"
url: "/mobilnisite/slovnik/ptp/"
type: "slovnik"
title: "PTP – Physical Termination Point"
date: 2026-01-01
abbr: "PTP"
fullName: "Physical Termination Point"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ptp/"
summary: "Konceptuální bod představující fyzickou hranici sítě 3GPP, typicky uživatelské zařízení (UE) nebo síťové ukončení. Je to základní referenční bod pro definici síťových rozhraní, přístupových bodů služe"
---

PTP je konceptuální bod fyzické hranice sítě 3GPP, například na uživatelském zařízení, používaný jako základní referenční bod pro definici rozhraní a ukončení protokolu v architektonických modelech.

## Popis

Physical Termination Point (PTP) je základní architektonický koncept ve specifikacích 3GPP používaný k modelování fyzické hranice sítě. Nejde o fyzické zařízení, ale o logický referenční bod, který představuje místo, kde je fyzické spojení ukončeno. Tato abstrakce je zásadní pro definici přesných koncových bodů rozhraní a protokolů. Ve většině kontextů je PTP asociován s uživatelským zařízením (UE) a představuje bod, kde se zařízení uživatele připojuje k funkčním jednotkám rádiového přístupu nebo jádra sítě. Slouží jako kotva pro definici uživatelsko-síťového rozhraní ([UNI](/mobilnisite/slovnik/uni/)) a je klíčový pro oddělení odpovědností uživatelské domény od domény síťového operátora.

Architektonicky je PTP používán napříč více doménami 3GPP, včetně jádra sítě (CN) a rádiové přístupové sítě (RAN). V definicích protokolových zásobníků jsou vrstvy často popsány jako poskytující služby vyšším vrstvám na přístupovém bodu služeb ([SAP](/mobilnisite/slovnik/sap/)) a PTP může představovat nejnižší SAP fyzické vrstvy. Pro systémy správy a účtování je PTP klíčovým identifikovatelným bodem pro přiřazení politik, měření využití a aplikaci pravidel kvality služeb (QoS). Jeho definice zajišťuje konzistenci při specifikaci, jak jsou informační toky iniciovány, ukončovány a spravovány na fyzickém okraji standardizovaného systému.

Role PTP zasahuje do definic služeb a diagramů síťové architektury. Je to stabilní reference, která přetrvává i při vývoji podkladových technologií od GSM přes UMTS a LTE až po 5G NR. Tím, že poskytuje jasný demarkační bod, napomáhá specifikaci přenosových cest, scénářů alokace IP adres a bezpečnostních perimetrů. Například v IP Multimedia Subsystem (IMS) pomáhá PTP definovat spojovací bod pro [SIP](/mobilnisite/slovnik/sip/) uživatelské agenty. Jeho konzistentní použití v desítkách technických specifikací (TS) a technických zpráv (TR) 3GPP podtrhuje jeho význam jako základního stavebního kamene pro síťové modelování a testování interoperability.

## K čemu slouží

Physical Termination Point byl zaveden za účelem vytvoření jasného, jednoznačného a standardizovaného modelu pro fyzickou hranici telekomunikační sítě. Před takovým formálním modelováním mohlo být definování, kde síť 'končí' a uživatelské zařízení 'začíná', nepřesné, což vedlo k možným nejednoznačnostem ve specifikacích rozhraní, odpovědnostech protokolů a definicích služeb. PTP tento problém řeší tím, že poskytuje univerzální referenční bod, ke kterému se mohou všechny ostatní architektonické prvky konzistentně vztahovat.

Tento konceptuální model je zásadní pro rozdělení funkčních a provozních odpovědností. Jasně vymezuje doménu síťového operátora od domény uživatele, což je klíčové pro definici standardizovaných rozhraní, zajištění interoperability mezi zařízeními různých výrobců a stanovení jasných bodů pro účtování, zákonné odposlechy a vynucování bezpečnosti. PTP umožňuje specifikacím jednoznačně stanovit, které funkce jsou prováděny uvnitř sítě a které v uživatelském zařízení, čímž zjednodušuje návrh systému a testování.

Historicky, jak se systémy 3GPP vyvíjely pro podporu paketových služeb, IMS a různých přístupových technologií, potřeba stabilní architektonické kotvy ještě vzrostla. PTP tuto stabilitu poskytuje a umožňuje integraci nových služeb a protokolů do architektury definováním jejich vztahu k tomuto základnímu hraničnímu bodu. Řeší tak omezení ad-hoc nebo technologií specifických definic hranic a zajišťuje soudržný architektonický rámec od 2G přes 5G a dále.

## Klíčové vlastnosti

- Logický referenční bod pro fyzickou hranici sítě
- Základní kotva pro definici uživatelsko-síťového rozhraní (UNI)
- Referenční bod pro přístupový bod služeb (SAP) v protokolových zásobnících
- Demarkační bod pro odpovědnosti domény operátora versus uživatele
- Klíčová entita pro správu sítě, účtování a vynucování politik
- Technologií nezávislý koncept aplikovaný od GSM po 5G NR

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [MT – Mobile Terminated Short Message Service](/mobilnisite/slovnik/mt/)
- [TE – Terminal Equipment](/mobilnisite/slovnik/te/)
- [SAP – Service Access Point](/mobilnisite/slovnik/sap/)
- [UNI – User to Network Interface](/mobilnisite/slovnik/uni/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TR 22.867** (Rel-18) — Study on 5G Smart Energy and Infrastructure
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.247** (Rel-19) — 5G Multicast/Broadcast Service Architecture
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TS 24.065** (Rel-4) — GPRS Subnetwork Dependent Convergence Protocol
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.535** (Rel-19) — TS 24535: (g)PTP Message Delivery Protocol
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- … a dalších 27 specifikací

---

📖 **Anglický originál a plná specifikace:** [PTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ptp/)
