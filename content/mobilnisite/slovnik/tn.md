---
slug: "tn"
url: "/mobilnisite/slovnik/tn/"
type: "slovnik"
title: "TN – Terrestrial Network"
date: 2026-01-01
abbr: "TN"
fullName: "Terrestrial Network"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tn/"
summary: "Konvenční pozemní infrastruktura mobilní sítě zahrnující všechny komponenty rádiového přístupového i jádrového sítě. V 3GPP se často používá v protikladu k neterestrickým sítím (NTN) k vymezení tradič"
---

TN (Terrestrial Network) je konvenční pozemní infrastruktura mobilní sítě zahrnující všechny komponenty rádiového přístupového i jádrového sítě, používaná v protikladu k neterestrickým sítím (NTN).

## Popis

V terminologii 3GPP označuje Terrestrial Network (TN) celý ekosystém standardizovaných systémů buněčné komunikace, jejichž síťové uzly (základnové stanice, funkce jádra) a koncová zařízení se nacházejí na zemském povrchu nebo v atmosféře. Zahrnuje všechny generace mobilní technologie standardizované 3GPP, včetně GSM (2G), UMTS (3G), LTE (4G) a NR (5G). Architektura TN je zásadně hierarchická a geograficky distribuovaná a skládá se z rádiové přístupové sítě (RAN) a jádrové sítě (CN). RAN tvoří základnové stanice (např. NodeB, eNodeB, gNB), které vytvářejí buňky pro bezdrátovou komunikaci s koncovým zařízením (UE). Jádrová síť zajišťuje komutaci, směrování, správu účastníků, autentizaci a připojení k externím paketovým datovým sítím, jako je internet.

Z technického hlediska fungování TN závisí na hustém rozmístění pozemních základnových stanic propojených přenosovou sítí backhaul (mikrovlnné, vláknové nebo kabelové spoje). Rádiová komunikace využívá licencovaná pásma pod 6 GHz (Frekvenční rozsah 1) a v pozdějších generacích také milimetrová pásma nad 24 GHz (Frekvenční rozsah 2). Klíčové protokoly a rozhraní definované ve specifikacích 3GPP – například rozhraní S1 mezi LTE RAN a jádrem nebo rozhraní [NG](/mobilnisite/slovnik/ng/) v 5G – řídí komunikaci mezi těmito pozemními prvky. Správa mobility v TN je primárně navržena pro předávání hovorů mezi pozemními buňkami, řízení interference v husté, plánované síťové topologii a poskytování přístupu s nízkou latencí díky krátkým vzdálenostem mezi UE a základnovými stanicemi.

Role konceptu TN se vyvinula se zavedením neterestrických sítí ([NTN](/mobilnisite/slovnik/ntn/)). V tomto kontextu slouží „TN“ jako referenční základní model. Při diskusích o integrovaném přístupovém backhaulu ([IAB](/mobilnisite/slovnik/iab/)), síťových řezech nebo multi-konektivitě jsou předpoklady a výkonnostní charakteristiky často zakotveny v terestrickém paradigmatu. TN například typicky předpokládá zpoždění šíření menší než několik milisekund, vysokou spolehlivost díky kontrolovanému interferenčnímu prostředí a možnost nasazení síťových funkcí na fyzicky zabezpečených a napájených místech. Porozumění TN je tedy předpokladem pro pochopení vylepšení a výzev, které přináší rozšíření pokrytí pomocí satelitů (NTN), protože mnohá řešení NTN usilují o emulaci nebo bezproblémovou spolupráci se stávající infrastrukturou a protokoly pozemní sítě.

## K čemu slouží

Pojem „Terrestrial Network“ je základním konceptem od počátku standardů mobilních sítí, ale jeho explicitní definice a kontrastní použití získaly klíčový význam se standardizací neterestrických sítí ([NTN](/mobilnisite/slovnik/ntn/)) v 3GPP Release 15 a novějších. Historicky byly všechny mobilní sítě nutně terestrické, takže pojem byl implicitní. Když však průmysl začal zkoumat integraci satelitů ([GEO](/mobilnisite/slovnik/geo/), [MEO](/mobilnisite/slovnik/meo/), [LEO](/mobilnisite/slovnik/leo/)) a stanic na vysokých nadmořských výškách ([HAPS](/mobilnisite/slovnik/haps/)) za účelem poskytnutí globálního pokrytí, doplnění služeb 5G a obsluhy aplikací internetu věcí (IoT) v odlehlých oblastech, vznikla potřeba jasného rozlišení.

Toto formální vymezení řeší problém nejednoznačnosti v technických specifikacích. Stanovuje jasnou referenční architekturu, kanálový model, chování protokolů a výkonnostní očekávání, vůči nimž lze definovat rozšíření a úpravy pro NTN. Například scénáře NTN musí řešit výzvy jako velmi dlouhá zpoždění šíření (stovky milisekund), vysoké Dopplerovy posuvy a přerušovanou viditelnost, které se v typické TN nevyskytují. Definováním „TN“ vytváří 3GPP referenční bod, což umožňuje standardům specifikovat, které postupy TN zůstávají platné pro NTN, které je potřeba upravit (např. timing advance, předávání hovorů, náhodný přístup) a které nové postupy jsou vyžadovány. To umožňuje vývoj hybridních sítí, kde se může UE bezproblémově připojit k terestrickému gNB nebo satelitnímu gNB, přičemž jádrová síť tuto integraci spravuje. Motivací je vytvořit jednotný globální standard podporující všudypřítomnou konektivitu, který využívá vysokou kapacitu a nízkou latenci hustých TN tam, kde je to ekonomicky proveditelné, a rozsáhlé pokrytí NTN tam, kde je pozemní nasazení nepraktické.

## Klíčové vlastnosti

- Zahrnuje veškerou pozemní infrastrukturu RAN a jádrové sítě
- Využívá licencovaná frekvenční pásma (pod 6 GHz a mmWave)
- Charakterizována nízkou latencí a vysokou spolehlivostí díky krátkým spojům
- Podporuje husté, plánované nasazení buněk pro kapacitu a pokrytí
- Základ pro všechny generace mobilních sítí 3GPP (2G až 5G)
- Slouží jako výkonnostní a architektonický referenční základ pro integraci NTN

## Související pojmy

- [NTN – Non-Terrestrial Networks](/mobilnisite/slovnik/ntn/)
- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [IAB – Integrated Access and Backhaul](/mobilnisite/slovnik/iab/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.196** (Rel-19) — Enhanced Calling Name (eCNAM) Stage 3 Protocol
- **TS 28.530** (Rel-19) — Network Slicing Concepts & Requirements
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 28.733** (Rel-19) — TN NRM IRP Solution Set Definitions
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.585** (Rel-19) — TSN Interworking Protocol for 5G System
- **TS 32.715** (Rel-9) — TN interface NRM IRP XML file format definition
- **TS 32.716** (Rel-11) — TN NRM IRP Solution Set Definitions
- **TR 33.926** (Rel-20) — Security Assurance Specification (SCAS)
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [TN na 3GPP Explorer](https://3gpp-explorer.com/glossary/tn/)
