---
slug: "supl"
url: "/mobilnisite/slovnik/supl/"
type: "slovnik"
title: "SUPL – Secure User Plane for Location"
date: 2026-01-01
abbr: "SUPL"
fullName: "Secure User Plane for Location"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/supl/"
summary: "Secure User Plane for Location (SUPL) je standardizovaný protokol 3GPP, který umožňuje zabezpečený přenos polohových dat přes uživatelskou rovinu (založenou na IP) pro určení geografické polohy mobiln"
---

SUPL je standardizovaný protokol 3GPP, který umožňuje zabezpečený přenos polohových dat přes IP-based uživatelskou rovinu pro určení geografické polohy mobilního zařízení.

## Popis

Secure User Plane for Location (SUPL) je soubor protokolů standardizovaný organizacemi 3GPP a Open Mobile Alliance ([OMA](/mobilnisite/slovnik/oma/)), který poskytuje služby určování polohy ([LCS](/mobilnisite/slovnik/lcs/)) využitím uživatelské roviny (datových kanálů založených na IP) namísto signalizačních kanálů řídicí roviny. Zavedený ve 3GPP Release 7 umožňuje SUPL efektivní a škálovatelné určení polohy mobilního zařízení přenosem polohových zpráv mezi SUPL Enabled Terminal ([SET](/mobilnisite/slovnik/set/)), což je mobilní zařízení, a SUPL Location Platform ([SLP](/mobilnisite/slovnik/slp/)), což je síťový polohový server. SLP se skládá ze dvou hlavních komponent: SUPL Location Center ([SLC](/mobilnisite/slovnik/slc/)), které spravuje relace a soukromí, a SUPL Positioning Center ([SPC](/mobilnisite/slovnik/spc/)), které provádí výpočet polohy.

SUPL funguje tak, že mezi SET a SLP naváže zabezpečené IP spojení (pomocí [TLS](/mobilnisite/slovnik/tls/)/[DTLS](/mobilnisite/slovnik/dtls/)). Protokol podporuje více metod určování polohy, včetně Assisted Global Navigation Satellite System (A-GNSS), Observed Time Difference of Arrival (OTDOA), Enhanced Cell ID (E-CID) a dalších. V typické SUPL relaci iniciuje žádost o polohu buď SLP, nebo SET. Výměnou zpráv (pomocí protokolů definovaných OMA, jako jsou ULPS nebo LPP) se přenášejí pomocná data (např. efemeridy satelitů pro A-GNSS) ze SLP do SET a měřicí data (např. pseudovzdálenosti nebo časová měření) ze SET do SLP. SPC následně vypočte polohu, která může být vrácena SET nebo externímu LCS klientovi (např. navigační aplikaci nebo záchranné službě).

Mezi klíčové architektonické prvky patří SUPL agent v SET (aplikace vyžadující polohu), rozhraní SLP s prvky jádra sítě (jako je GMLC v LCS řídicí roviny) a podpora roamingových scénářů, kde mohou spolupracovat domácí SLP a navštívené SLP. SUPL je navržen ke snížení signalizační zátěže na řídicí rovině, nabízí rychlejší určování polohy a podporuje služby kontinuálního sledování. Je široce nasazován pro komerční služby založené na poloze (např. mapy, vyhledávače přátel) a v některých regionech je povinný pro záchranné služby jako E911. Specifikace pokrývají 3GPP (např. 23.271 pro architekturu) a OMA (např. OMA-AD-SUPL pro podrobnosti protokolu), což zajišťuje interoperabilitu napříč zařízeními a sítěmi.

## K čemu slouží

SUPL byl vyvinut pro řešení omezení řešení určování polohy v řídicí rovině v sítích 2G/3G, která byla závislá na signalizačním systému č. 7 (SS7) a okruhově přepínaných spojích. LCS v řídicí rovině bylo složité, pomalé a pro hromadné služby založené na poloze neškálovatelné kvůli vysoké signalizační režii a závislosti na implementacích síťových dodavatelů. S rostoucí poptávkou po polohových službách v důsledku nástupu smartphonů a aplikací bylo zapotřebí efektivnějšího přístupu založeného na IP.

Hlavní motivací pro SUPL bylo využít pro určování polohy uživatelskou rovinu (paketově přepínaná data), což umožnilo rychlejší navázání relace, snížení zahlcení sítě a snadnější integraci s internetovými aplikacemi. Použitím standardní IP zabezpečení (TLS) poskytoval SUPL také inherentní bezpečnostní a ochranné mechanismy soukromí, které byly v metodách řídicí roviny méně robustní. To umožnilo operátorům nabízet komerční LCS (jako navigaci nebo reklamu) bez dopadu na stabilitu jádra sítě.

SUPL navíc podporoval širší škálu polohových technologií (např. A-GNSS, určování polohy přes Wi-Fi) a umožňoval nepřetržité sledování polohy pro služby jako správa vozového parku nebo monitorování dětí. Jeho zavedení v Release 7 se časově shodovalo s rozvojem datových služeb 3G a poskytlo perspektivní rámec, který se dále rozvíjel přes LTE a 5G. SUPL také usnadnil splnění regulatorních požadavků pro záchranné služby (např. E112 v Evropě) tím, že nabídl standardizovanou a spolehlivou metodu určování polohy, která doplňuje řešení v řídicí rovině. SUPL tak vyřešil problémy škálovatelnosti, rychlosti a flexibility a umožnil vznik ekosystému služeb využívajících polohu, který známe dnes.

## Klíčové vlastnosti

- Určování polohy v uživatelské rovině s využitím IP-based přenosu (např. TCP/IP se zabezpečením TLS/DTLS)
- Podpora více metod určování polohy: A-GNSS, OTDOA, E-CID, Wi-Fi a metod založených na senzorech
- Podpora roamingu s interakcí domácího a navštíveného SLP
- Iniciace relace sítí (network-initiated) nebo zařízením (SET-initiated)
- Zabezpečený přenos pomocných dat a měřicích reportů
- Integrace s LCS v řídicí rovině pro hybridní určování polohy a záchranné služby

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [E-CID – Enhanced Cell-ID](/mobilnisite/slovnik/e-cid/)
- [SLP – Service Location Protocol](/mobilnisite/slovnik/slp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.814** (Rel-10) — Study on LCS support for non-3GPP accesses
- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.303** (Rel-19) — Proximity Services (ProSe) Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 23.868** (Rel-9) — Study on IMS Emergency Calls
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 24.572** (Rel-19) — 5G LCS User Plane Protocol Specification
- **TS 29.171** (Rel-19) — LCS Application Protocol (LCS-AP) Specification
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [SUPL na 3GPP Explorer](https://3gpp-explorer.com/glossary/supl/)
