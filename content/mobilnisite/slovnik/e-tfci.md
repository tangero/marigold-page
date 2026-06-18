---
slug: "e-tfci"
url: "/mobilnisite/slovnik/e-tfci/"
type: "slovnik"
title: "E-TFCI – E-DCH Transport Format Combination Indicator"
date: 2025-01-01
abbr: "E-TFCI"
fullName: "E-DCH Transport Format Combination Indicator"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-tfci/"
summary: "Řídicí pole v uplinku E-DCH, které informuje Node B o kombinaci transportních formátů (TFC) používané pro přenos dat na vylepšeném vyhrazeném kanálu (E-DCH). Je nezbytné, aby Node B mohl správně demod"
---

E-TFCI je řídicí pole v uplinku E-DCH, které informuje Node B o používané kombinaci transportních formátů, což umožňuje správnou demodulaci, dekódování, plánování a správu HARQ.

## Popis

Indikátor kombinace transportních formátů pro [E-DCH](/mobilnisite/slovnik/e-dch/) (E-TFCI) je klíčový řídicí prvek v rámci funkce High-Speed Uplink Packet Access ([HSUPA](/mobilnisite/slovnik/hsupa/)) v UMTS, zavedený ve 3GPP Release 6. Je přenášen jako součást vyhrazeného fyzického řídicího kanálu E-DCH ([E-DPCCH](/mobilnisite/slovnik/e-dpcch/)) v uplinku ze zařízení uživatele (UE) do Node B. Hodnota E-TFCI explicitně signalizuje přesnou kombinaci transportních formátů používanou pro vyhrazený fyzický datový kanál E-DCH ([E-DPDCH](/mobilnisite/slovnik/e-dpdch/)) v aktuálním přenosovém časovém intervalu ([TTI](/mobilnisite/slovnik/tti/)). Tato kombinace definuje parametry jako velikost transportního bloku, počet transportních bloků a schéma kódování kanálu. Příjemce v Node B používá dekódované E-TFCI k určení, jak demodulovat, odstředit a dekódovat přidružená data z E-DPDCH. Bez tohoto explicitního indikátoru by Node B musel transportní formát detekovat naslepo, což je výpočetně složité a náchylné k chybám, zejména vzhledem k širokému rozsahu podporovaných datových rychlostí v HSUPA. E-TFCI umožňuje spolehlivý a efektivní přenos dat v uplinku tím, že síťová strana má přesnou znalost přenosových parametrů zvolených UE na základě přiděleného plánovacího grantu a dostupných dat. Jeho návrh je nedílnou součástí rychlých procesů plánování řízených Node B a hybridního [ARQ](/mobilnisite/slovnik/arq/) ([HARQ](/mobilnisite/slovnik/harq/)), které definují výkonnostní vylepšení HSUPA oproti předchozím uplinkům [DCH](/mobilnisite/slovnik/dch/) z Release 99.

## K čemu slouží

E-TFCI bylo vytvořeno k vyřešení problému slepé detekce transportního formátu (BTFD) v uplinku pro vysokorychlostní paketová data. Ve vyhrazeném kanálu (DCH) z Release 99 před HSUPA byl transportní formát v uplinku buď pevný, nebo signalizovaný přes vyšší vrstvy (RRC), což zavádělo latenci. Pro dynamické, rychle plánované přenosy v HSUPA byla vyžadována metoda signalizace s nízkou latencí v pásmu. E-TFCI poskytuje Node B explicitní, okamžitou indikaci kombinace transportních formátů ve stejném TTI jako data. To řeší několik klíčových problémů: odstraňuje potřebu složité a nespolehlivé slepé detekce v Node B, která by omezovala praktický počet podporovaných transportních formátů a datových rychlostí. Umožňuje UE rychle přizpůsobovat datovou rychlost v uplinku v reakci na rychlé plánovací granty z Node B. Dále je nezbytné pro proces HARQ, protože Node B musí znát přesnou velikost transportního bloku, aby mohl provádět měkké kombinování retransmisí. E-TFCI je základním prvkem, který umožnil technickou realizaci vysoké propustnosti, nízké latence a lepší kapacity HSUPA.

## Klíčové vlastnosti

- Explicitně signalizuje aktivní kombinaci transportních formátů (TFC) pro E-DPDCH.
- Přenášen v pásmu na řídicím kanálu E-DPCCH společně s daty.
- Umožňuje spolehlivou demodulaci a dekódování proměnné rychlosti uplinkových dat v Node B.
- Základní pro fungování rychlého plánování řízeného Node B (E-AGCH, E-RGCH).
- Nezbytné pro měkké kombinování v hybridním ARQ (HARQ), protože musí být známa velikost TB.
- Podporuje více délek TTI (2 ms, 10 ms) jako součást rámce E-DCH.

## Související pojmy

- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [E-DPCCH – E-DCH Dedicated Physical Control Channel](/mobilnisite/slovnik/e-dpcch/)
- [E-DPDCH – E-DCH Dedicated Physical Data Channel](/mobilnisite/slovnik/e-dpdch/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)

## Definující specifikace

- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol

---

📖 **Anglický originál a plná specifikace:** [E-TFCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-tfci/)
