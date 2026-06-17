---
slug: "dsl"
url: "/mobilnisite/slovnik/dsl/"
type: "slovnik"
title: "DSL – Digital Subscriber Line"
date: 2025-01-01
abbr: "DSL"
fullName: "Digital Subscriber Line"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dsl/"
summary: "Digital Subscriber Line (DSL) je rodina technologií poskytujících vysokorychlostní přístup k internetu přes tradiční měděné telefonní linky. Používá pokročilé modulační techniky k přenosu digitálních"
---

DSL je rodina technologií, která poskytuje vysokorychlostní přístup k internetu přes měděné telefonní linky pomocí pokročilé modulace pro přenos dat, což umožňuje současné hlasové a datové služby.

## Popis

Technologie Digital Subscriber Line funguje tak, že rozděluje frekvenční spektrum dostupné na měděné kroucené dvoulince. Nižší frekvenční pásmo (0–4 kHz) je vyhrazeno pro klasickou telefonní službu (POTS), což umožňuje standardní hlasové hovory. Vyšší frekvenční pásma se používají pro přenos dat za využití sofistikovaných modulačních schémat, jako je Discrete Multi-Tone (DMT) pro [ADSL](/mobilnisite/slovnik/adsl/) nebo modulace Carrierless Amplitude Phase ([CAP](/mobilnisite/slovnik/cap/)). Klíčovými koncovými body jsou DSL modem na straně zákazníka a DSL Access Multiplexer (DSLAM) v telefonní ústředně nebo v uliční skříni.

Architektura se skládá z zařízení na straně zákazníka ([CPE](/mobilnisite/slovnik/cpe/)) s DSL modemem nebo bránou, místní smyčky (měděné linky) a DSLAM umístěného v centrální ústředně nebo vzdáleném uzlu. DSLAM agreguje provoz od více účastníků, demultiplexuje datové a hlasové signály a přeposílá datový provoz do jádra širokopásmové sítě. Na obou koncích se používají filtry (splittery) nebo mikrofiltry, aby se zabránilo interferenci mezi vysokofrekvenčními datovými signály a nízkofrekvenčními hlasovými signály.

Ve specifikacích 3GPP je DSL často zmiňována v kontextu integrace pevných sítí, síťové spolupráce a jako potenciální přístupová síť pro IP Multimedia Subsystem (IMS) nebo pro konvergenci pevných a mobilních sítí. Specifikace jako 29.214 (referenční bod Rx) nebo 33.937 (bezpečnost [FMC](/mobilnisite/slovnik/fmc/)) považují DSL za důvěryhodný přístup mimo 3GPP. Její role spočívá v tom, že jde o doplňkovou technologii pevného širokopásmového přístupu, kterou lze integrovat s mobilními jádrovými sítěmi pro konvergované služby.

## K čemu slouží

DSL byl vyvinut, aby využil stávající, všudypřítomnou infrastrukturu měděných telefonních linek pro poskytování širokopásmového přístupu k internetu a překonal tak závažná rychlostní omezení vytáčených modemů. Vyřešil problém poskytování trvalého vysokorychlostního datového připojení bez nutnosti masivních nových investic do kabeláže poslední míle, jaké byly potřeba pro optiku do domu.

Historickým motivem byl exploze internetu v 90. letech a rostoucí poptávka po rezidenčním a podnikovém širokopásmovém připojení. Technologie DSL, jako je [ADSL](/mobilnisite/slovnik/adsl/), umožnily telekomunikačním operátorům nabízet internetové služby ve vrstvách přes jejich stávající měděnou síť, čímž vytvořily nový zdroj příjmů a konkurovaly poskytovatelům kabelových modemů. Odstranila klíčové omezení hlasového pásma modemů, které bylo zásadně limitováno 3,4 kHz kanálem telefonní sítě, tím, že využila mnohem širší frekvenční spektrum dostupné na fyzickém měděném páru.

## Klíčové vlastnosti

- Současný přenos hlasu (POTS) a vysokorychlostních dat přes jediný měděný pár
- Frekvenční multiplex s dělením pro oddělení hlasového a datového pásma
- Využití pokročilé modulace (např. DMT) pro robustní přenos dat po mědi
- Rychlostně adaptivní technologie pro maximalizaci rychlosti na základě stavu linky
- Asymetrická šířka pásma (downstream >> upstream) u běžných variant jako ADSL
- Integrace s agregačními sítěmi prostřednictvím DSLAM

## Související pojmy

- [ADSL – Asymmetric Digital Subscriber Line](/mobilnisite/slovnik/adsl/)

## Definující specifikace

- **TR 21.866** (Rel-15) — Study on Energy Efficiency in 3GPP Standards
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TR 22.937** (Rel-13) — FMC requirements for 3GPP-WLAN service continuity
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 24.525** (Rel-19) — Business Trunking Architecture & Requirements
- **TS 24.819** (Rel-7) — IMS Services via Fixed Broadband Access
- **TR 24.930** (Rel-19) — IMS Session Setup Signalling Flows
- **TS 25.467** (Rel-19) — UTRAN Architecture for 3G Home Node B
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 32.833** (Rel-11) — Converged OSS End-to-End Management Study
- **TR 33.937** (Rel-19) — Protection against Unsolicited Communication in IMS
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [DSL na 3GPP Explorer](https://3gpp-explorer.com/glossary/dsl/)
