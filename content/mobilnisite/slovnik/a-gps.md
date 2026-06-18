---
slug: "a-gps"
url: "/mobilnisite/slovnik/a-gps/"
type: "slovnik"
title: "A-GPS – Assisted Global Positioning System"
date: 2025-01-01
abbr: "A-GPS"
fullName: "Assisted Global Positioning System"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/a-gps/"
summary: "A-GPS je síťově asistovaná lokalizační technologie, která zlepšuje výkon GPS v mobilních zařízeních tím, že poskytuje pomocná data ze sítě. Výrazně snižuje dobu do prvního určení polohy (TTFF), zlepšu"
---

A-GPS je síťově asistovaná lokalizační technologie, která zlepšuje výkon GPS v mobilních zařízeních tím, že poskytuje pomocná data pro zkrácení počáteční doby určení polohy, zvýšení přesnosti a šetření životnosti baterie.

## Popis

Assisted [GPS](/mobilnisite/slovnik/gps/) (A-GPS) je lokalizační metoda standardizovaná 3GPP, která využívá mobilní síť ke zlepšení výkonu samostatného GPS přijímače v uživatelském zařízení (UE). Základní princip spočívá v tom, že síť poskytuje UE pomocná data, která zahrnují efemeridy, almanach, referenční čas a přibližnou počáteční polohu. Tato data umožňují GPS přijímači v UE přesně vědět, které satelity jsou v dosahu a jaké mají očekávané parametry signálu, čímž odpadá potřeba zdlouhavého a energeticky náročného procesu hledání a demodulace satelitních signálů. UE pak může provést rychlejší a citlivější korelaci pro zachycení satelitních signálů, výpočet pseudovzdáleností a určení své polohy.

Z architektonického hlediska se A-GPS účastní několik klíčových síťových prvků definovaných ve specifikacích 3GPP. Serving Mobile Location Centre ([SMLC](/mobilnisite/slovnik/smlc/)) nebo jeho evolvovaná verze ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v LTE/5G je centrální uzel zodpovědný za generování a poskytování pomocných dat. Komunikuje s UE prostřednictvím rádiové přístupové sítě (RAN) a core sítě za použití řídicích protokolů, jako je Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) nebo jeho předchůdci. SMLC/E-SMLC se může připojit k síti GPS referenčních přijímačů pro získávání aktuálních satelitních dat. UE odesílá svá měření (např. pseudovzdálenosti, sílu signálu) zpět do sítě, která může volitelně provést konečný výpočet polohy v síťovém režimu, nebo si může UE svou polohu vypočítat sama v režimu založeném na UE za použití pomocných dat.

Provoz probíhá ve dvou hlavních režimech: UE-assisted (asistovaný UE) a UE-based (založený na UE). V režimu UE-assisted síť poskytuje pomocná data, UE měří satelitní signály a odesílá tato surová měření (jako je fáze kódu) zpět do SMLC. SMLC následně provede výpočet polohy. Tento režim je efektivní pro jednoduchá klientská zařízení. V režimu UE-based síť poskytuje komplexnější pomocná data (včetně efemerid a korekcí hodin), což umožňuje UE vypočítat svou polohu lokálně. To nabízí rychlejší dobu odezvy a funguje i tehdy, když UE po přijetí dat ztratí síťové připojení. Běžné jsou také hybridní přístupy.

Role A-GPS je klíčová pro splnění regulatorních (např. E911, eCall) a komerčních požadavků služeb založených na poloze ([LBS](/mobilnisite/slovnik/lbs/)). Poskytuje vyšší přesnost (často v rozmezí 5–50 metrů) ve srovnání se síťovými metodami, jako je Cell-ID nebo [OTDOA](/mobilnisite/slovnik/otdoa/), zejména v podmínkách s volným výhledem na oblohu. Její integrace s jinými lokalizačními metodami (hybridní lokalizace) v pozdějších vydáních 3GPP zajišťuje robustní výkon v různorodých prostředích, což z ní činí základní technologii pro moderní mobilní lokalizační služby.

## K čemu slouží

A-GPS byl vyvinut k řešení základních omezení samostatného [GPS](/mobilnisite/slovnik/gps/) v masově vyráběných mobilních telefonech. Klasické GPS přijímače trpí dlouhou dobou do prvního určení polohy (TTFF), která při studeném startu často činí 30 sekund až několik minut, protože si musí stáhnout orbitální data (efemeridy) velmi nízkou přenosovou rychlostí (50 bps) přímo ze satelitů. Tento proces spotřebovává značný výkon baterie a často selhává v prostředích se slabým signálem, jako jsou městské zástavby, vnitřní prostory nebo pod korunami stromů. Tyto nedostatky činily samostatné GPS nepraktickými pro nouzové služby (jako je povinné určení polohy pro E911) a pro spotřebitelské aplikace vyžadující rychlé a spolehlivé určení.

Vytvoření A-GPS bylo motivováno potřebou splnit přísné požadavky na přesnost a dobu odezvy pro lokalizaci volajících v nouzových situacích, jak to nařídily regulační orgány v Severní Americe (FCC E911) a později celosvětově. Využitím vysoké přenosové kapacity a neustálého připojení mobilních sítí doručuje A-GPS potřebná satelitní data do přístroje téměř okamžitě. Tato síťová asistence snižuje TTFF na několik sekund, zlepšuje citlivost (umožňuje provoz i při slabším signálu) a snižuje výpočetní a energetickou zátěž UE. Vyřešila tak ekonomickou a technickou výzvu integrace plnohodnotných vysoce výkonných GPS přijímačů do malých přístrojů s omezenou kapacitou baterie.

Historicky A-GPS ve verzi Rel-5 poskytlo architektonický základ, který umožnil široké přijetí lokalizačních služeb v sítích 2G a 3G. Vyřešilo kritický problém, jak učinit GPS technologii životaschopnou pro mobilní prostředí, a překlenulo tak propast mezi vysokou přesností satelitních systémů a praktickými omezeními spotřebitelských přístrojů. To otevřelo cestu rozsáhlému ekosystému navigačních aplikací, sociálních sítí a sledování majetku, které definují moderní mobilní zážitky.

## Klíčové vlastnosti

- Síťově poskytovaná pomocná data (efemeridy, almanach, čas, přibližná poloha)
- Výrazně zkrácená doba do prvního určení polohy (TTFF)
- Zlepšená citlivost přijímače pro provoz v prostředích se slabým signálem (např. uvnitř budov)
- Podpora režimů lokalizace UE-assisted a UE-based
- Snížená spotřeba energie v uživatelském zařízení (UE)
- Integrace s jinými lokalizačními metodami pro hybridní řešení určování polohy

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)

## Definující specifikace

- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.452** (Rel-19) — Iupc Interface Signalling Transport for PCAP
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 34.171** (Rel-9) — A-GPS FDD UE Conformance Testing Procedures
- **TS 34.172** (Rel-10) — A-GNSS Conformance Testing for UTRA FDD UE
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.171** (Rel-19) — 5G A-GNSS UE Positioning Requirements
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification
- **TS 45.005** (Rel-19) — GSM RF Requirements for MS and BSS
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [A-GPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/a-gps/)
