---
slug: "mbr"
url: "/mobilnisite/slovnik/mbr/"
type: "slovnik"
title: "MBR – Maritime Broadband Radio Links"
date: 2025-01-01
abbr: "MBR"
fullName: "Maritime Broadband Radio Links"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mbr/"
summary: "MBR označuje širokopásmové rádiové komunikační systémy navržené pro námořní prostředí, které umožňují vysokorychlostní datovou konektivitu pro lodě a offshore instalace. Řeší specifické výzvy námořní"
---

MBR je širokopásmový rádiový komunikační systém pro námořní prostředí, který umožňuje vysokorychlostní datovou konektivitu pro lodě a pobřežní či offshore instalace díky využití pozemních a satelitních komponent k řešení výzev jako velké vzdálenosti a drsné podmínky.

## Popis

Maritime Broadband Radio Links (MBR) jsou specializované systémy rádiového přístupu standardizované 3GPP pro poskytování spolehlivé širokopásmové konektivity v námořních scénářích. Tyto systémy jsou konstruovány tak, aby překonaly specifické výzvy šíření signálu a mobility na otevřeném moři, kde je tradiční pozemní buněčné pokrytí omezené nebo neexistuje. Architektury MBR často integrují pozemní základnové stanice rozmístěné podél pobřeží se satelitními komunikačními komponentami, aby zajistily nepřetržité pokrytí při plavbě plavidel mimo dosah přímé viditelnosti pobřežní infrastruktury. Technologie podporuje jak komerční, tak bezpečnostně kritické aplikace a vyžaduje robustní úrovně signálu (link budget) a pokročilé anténní systémy pro udržení konektivity navzdory náklonu, houpání plavidla a útlumu signálu na velké vzdálenosti.

Z technické perspektivy MBR pracuje ve vyhrazených námořních kmitočtových pásmech a využívá průběhy signálu (waveforms) a protokoly optimalizované pro šíření přes vodní hladinu. Klíčové síťové prvky zahrnují námořní základnové stanice (Maritime Base Stations, [MBS](/mobilnisite/slovnik/mbs/)), které mohou být umístěny na pobřeží nebo na offshore platformách, a uživatelská zařízení (User Equipment, UE) instalovaná na plavidlech. Tyto prvky komunikují pomocí adaptací 3GPP rádiových rozhraní, jako jsou LTE nebo 5G NR, avšak s vylepšeními pro námořní modely mobility a rozšířený dosah buněk. Systém musí zvládat vysoké Dopplerovy posuny způsobené rychlostí plavidla a dynamicky řídit přechody (handovers) mezi pozemními buňkami a satelitními spoji, aby zajistil kontinuitu služeb.

Úlohou MBR v síti je rozšířit dosah služeb mobilního širokopásmového připojení na námořní trasy, přístavy a offshore ekonomické zóny. Umožňuje širokou škálu aplikací, od internetového přístupu pro posádku a přenosu provozních dat pro přepravní společnosti až po sledování v reálném čase a podporu autonomní navigace. Pro bezpečnost může MBR integrovat s námořními tísňovými a bezpečnostními systémy a poskytovat tak doplňkovou komunikační cestu pro záchranné služby. Jeho standardizace zajišťuje interoperabilitu mezi zařízeními od různých výrobců a usnadňuje globální roaming pro námořní uživatele, podobně jako pozemní buněčné sítě pro pozemní účastníky.

## K čemu slouží

Technologie MBR byla vytvořena, aby vyřešila významnou mezeru v konektivitě v námořních oblastech, kde jsou tradiční mobilní sítě nepraktické kvůli rozlehlým, neobydleným plochám oceánu. Před její standardizací byly námořní komunikace závislé převážně na starších systémech, jako je VHF rádio pro hlasové služby a úzkopásmové satelitní služby pro omezený přenos dat, které byly často drahé, nízkokapacitní a nedostatečné pro moderní digitální aplikace. Růst globálního lodního průmyslu, rostoucí poptávka po provozní efektivitě a potřeba zvýšené bezpečnosti a pohody posádky vedly k požadavku na nákladově efektivní vysokorychlostní širokopásmové připojení na moři.

Omezení předchozích přístupů byla mnohostranná. Satelitní komunikace, ačkoli poskytují široké pokrytí, historicky trpěly vysokou latencí (zejména v geostacionárních systémech) a omezenou kapacitou přenosové šířky pásma, což je činilo nevhodnými pro aplikace v reálném čase nebo náročné na data. Pozemní systémy samy o sobě nemohly pokrýt více než několik kilometrů od pobřeží. MBR tato omezení řeší vytvořením hybridní sítě, která optimálně kombinuje pozemní a satelitní spoje, nabízejíc vyšší přenosovou šířku pásma a nižší latenci poblíž pobřeží prostřednictvím pozemních spojů a zajišťujíc základní konektivitu na otevřeném moři prostřednictvím satelitů. Tento hybridní přístup vyvažuje výkon a pokrytí a umožňuje nové námořní služby, jako je sledování videí v reálném čase, vzdálená diagnostika a aktualizace digitálních navigačních map.

Historicky počáteční práce ve 3GPP Release 5 položily základy pro rozšíření mobilního širokopásmového připojení do námořního prostředí a uznaly námořní sektor jako specifický případ použití s jedinečnými požadavky. Následující specifikace (releases) dále vyvíjely standardy tak, aby začlenily pokroky v rádiové technologii, jako jsou LTE a 5G NR, a aby lépe integrovaly s globálními námořními regulačními rámci. Účelem MBR je tedy přinést výhody pozemního mobilního širokopásmového připojení – dostupnost, vysokou rychlost a nízkou latenci – do námořní domény, čímž podporuje ekonomické aktivity a bezpečnost na moři.

## Klíčové vlastnosti

- Hybridní architektura kombinující pozemní a satelitní spoje pro rozšířené pokrytí
- Optimalizace pro námořní modely mobility a šíření signálu na dlouhé vzdálenosti
- Podpora vysokorychlostních širokopásmových datových služeb pro plavidla
- Integrace s námořními bezpečnostními a tísňovými komunikačními systémy
- Vylepšené anténní systémy pro kompenzaci pohybu plavidla
- Schopnosti interoperability a globálního roamingu pro námořní uživatele

## Související pojmy

- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TS 23.202** (Rel-19) — CS Bearer Services Architecture in UMTS
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.924** (Rel-19) — MTSI QoS Improvement Study
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 37.890** (Rel-19) — Feasibility Study on 6 GHz for LTE/NR
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [MBR na 3GPP Explorer](https://3gpp-explorer.com/glossary/mbr/)
