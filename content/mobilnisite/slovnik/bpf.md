---
slug: "bpf"
url: "/mobilnisite/slovnik/bpf/"
type: "slovnik"
title: "BPF – Band Pass Filter"
date: 2025-01-01
abbr: "BPF"
fullName: "Band Pass Filter"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bpf/"
summary: "Pásmový filtr (Band Pass Filter – BPF) je elektronický obvod nebo komponenta, která selektivně propouští signály v určitém frekvenčním rozsahu a současně potlačuje frekvence mimo toto pásmo. V rámci 3"
---

BPF (pásmový filtr) je vysokofrekvenční (RF) komponenta používaná v mobilních sítích k propuštění signálů v určitém frekvenčním pásmu a blokování ostatních, čímž zajišťuje spektrální čistotu a snižuje interferenci.

## Popis

Pásmový filtr (Band Pass Filter – BPF) je lineární, časově invariantní filtr charakterizovaný svým propustným pásmem, nepropustným pásmem, střední frekvencí, šířkou pásma a profilu útlumu. V kontextu 3GPP rádiových systémů funguje v rámci [RF](/mobilnisite/slovnik/rf/) předkoncového stupně transceiverů. Architektonicky je umístěn za anténou a šumovým předzesilovačem ([LNA](/mobilnisite/slovnik/lna/)) v přijímacím řetězci a před výkonovým zesilovačem ([PA](/mobilnisite/slovnik/pa/)) v vysílacím řetězci. Jeho hlavní úlohou je propustit pouze frekvence určeného komunikačního kanálu a zároveň potlačit mimopásmové signály, včetně rušení z přilehlých kanálů, harmonických složek a šumu. Tato selektivní filtrace je nezbytná pro zachování integrity signálu a prevenci desenzibilizace přijímače.

Z technického hlediska je funkce BPF definována jeho přenosovou funkcí, která může být realizována pomocí různých technologií, jako jsou povrchové akustické vlny (SAW), objemové akustické vlny (BAW), keramické nebo [LC](/mobilnisite/slovnik/lc/) (cívka-kondenzátor) rezonátory. V 5G-Advanced (Rel-18/19) se požadavky na návrh zpřísnily kvůli větším šířkám pásma, agregaci nosných v roztříštěném spektru a využití vyšších frekvenčních pásem jako FR2 (mmWave). Filtr musí vykazovat nízký vložný útlum v propustném pásmu pro zachování výkonu signálu, vysoké potlačení v nepropustných pásmech pro blokování rušivých signálů a strmé přechodové charakteristiky, aby vyhověl úzkým ochranným pásmům. Jeho výkon přímo ovlivňuje klíčové RF parametry, jako je velikost chybového vektoru ([EVM](/mobilnisite/slovnik/evm/)), poměr úniku do přilehlého kanálu ([ACLR](/mobilnisite/slovnik/aclr/)) a citlivost přijímače.

Integrace a řízení BPF jsou rovněž řešeny ve specifikacích 3GPP. Například ve scénářích zahrnujících dynamické sdílení spektra (DSS) nebo adaptaci šířky pásma mohou být požadovány laditelné nebo přepínatelné charakteristiky filtru. Specifikace jako 38.774 (Radio Frequency (RF) requirement background for NR) a 38.869 (RF requirements for Multi-Radio Dual Connectivity ([MR-DC](/mobilnisite/slovnik/mr-dc/))) podrobně popisují testovací metodologie a požadavky na shodu pro tyto filtry ve spojení s dalšími RF komponentami. Filtr spolupracuje s duplexery, přepínači a zesilovači a tvoří kompletní RF předkoncový modul. Jeho role je zásadní; bez účinné pásmové filtrace by byly vysoce účinné modulační schémata (např. 1024QAM) a husté frekvenční opakování moderních celulárních sítí nemožné kvůli nadměrnému rušení.

Při nasazení sítě návrh BPF ovlivňuje složitost základnových stanic a uživatelských terminálů, spotřebu energie a náklady. Pro základnové stanice (gNB) se používají výkonné filtry s vysokou selektivitou pro správu vícenosných přenosů. V uživatelských terminálech množství podporovaných pásem (od sub-6 GHz po mmWave) pro globální roaming vyžaduje více BPF v rámci jednoho zařízení, často integrovaných do předkoncových modulů (FEM). Referované specifikace (26.253, 38.774, 38.869) poskytují rámec zajišťující, že tyto komponenty splňují přísné výkonnostní standardy nezbytné pro interoperabilní, vysoce výkonné sítě 5G-Advanced, které umožňují funkce jako vylepšené mobilní širokopásmové připojení (eMBB), ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a hromadná komunikace mezi stroji (mMTC).

## K čemu slouží

Pásmový filtr (BPF) existuje za účelem řešení základního problému frekvenční selektivity v bezdrátových komunikačních systémech. Rozhlasové spektrum je sdíleným a omezeným zdrojem, přičemž více operátorů a služeb vysílá současně na přilehlých frekvenčních kanálech. Bez filtrace by byl přijímač zaplaven směsicí signálů, což by znemožnilo dekódování požadovaného přenosu. BPF poskytuje nezbytnou izolaci, umožňující transceiveru se zaměřit výhradně na přidělené frekvenční pásmo. To je klíčové pro dosažení vysokého poměru signálu k šumu (SNR) a nízké chybovosti (BER), což jsou předpoklady spolehlivé komunikace s vysokou datovou rychlostí.

Historicky, jak se vyvíjely celulární standardy od 2G do 5G, problémy řešené BPF se prohloubily. Rané systémy jako GSM fungovaly v relativně úzkých, vyhrazených pásmech. Se zavedením 3G a 4G zavedení větších šířek pásma a agregace nosných zvýšilo nároky na linearitu filtru a mimopásmové potlačení. Přechod na 5G, zejména s 5G-Advanced v Rel-18, přinesl nové složitosti: využití milimetrových vln (mmWave), širší kanálové šířky pásma až do 400 MHz a agresivnější techniky sdílení spektra. Předchozí filtrační technologie často zápasily s kompromisy mezi šířkou pásma, vložným útlumem a velikostí. Omezení starších přístupů – jako nadměrný útlum na vysokých frekvencích nebo nedostatečné potlačení vedoucí k interferenci – motivovala pokroky v materiálech filtrů (např. BAW filtry s vysokým činitelem jakosti Q) a architekturách (např. laditelné filtry) pro splnění přísných požadavků 5G.

Vytváření a standardizace požadavků v 3GPP Rel-18 pro komponenty jako BPF byly hnací silou potřeby zajistit výkon sítě a interoperabilitu zařízení v tomto složitějším RF prostředí. Specifikace jako 38.774 a 38.869 definují RF požadavky, které implicitně řídí výkon BPF, a zajišťují, že síťová infrastruktura i uživatelská zařízení mohou pracovat efektivně, aniž by způsobovaly nebo podléhaly škodlivému rušení. To umožňuje plné využití nového spektra, podporuje hustá nasazení sítí a je základem kvality služeb pro pokročilé služby 5G, od gigabitového mobilního širokopásmového připojení až po kritické IoT aplikace.

## Klíčové vlastnosti

- Selektivní propustné pásmo pro izolaci požadovaných komunikačních kanálů
- Vysoké mimopásmové potlačení pro potlačení rušení z přilehlých kanálů a rušivých signálů
- Nízký vložný útlum v propustném pásmu pro zachování výkonu signálu a citlivosti přijímače
- Definované přechodové charakteristiky pro vyhovění úzkým ochranným pásmům v zaplněném spektru
- Splnění specifikovaných RF výkonnostních metrik 3GPP (např. ACLR, EVM, citlivost)
- Podpora širokých a ultraširokých šířek pásma definovaných pro nosné 5G NR

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 38.774** (Rel-19) — Rel-19 LP-WUS/WUR RF Requirements TR
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR

---

📖 **Anglický originál a plná specifikace:** [BPF na 3GPP Explorer](https://3gpp-explorer.com/glossary/bpf/)
