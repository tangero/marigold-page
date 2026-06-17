---
slug: "aqpsk"
url: "/mobilnisite/slovnik/aqpsk/"
type: "slovnik"
title: "AQPSK – Adaptive Quadrature Phase Shift Keying"
date: 2025-01-01
abbr: "AQPSK"
fullName: "Adaptive Quadrature Phase Shift Keying"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/aqpsk/"
summary: "AQPSK je modulační schéma používané v sítích GSM/EDGE, které dynamicky přepíná mezi modulacemi GMSK a 8PSK na základě rádiových podmínek. Optimalizuje spektrální účinnost při zachování zpětné kompatib"
---

AQPSK je modulační schéma GSM/EDGE, které dynamicky přepíná mezi GMSK a 8PSK na základě rádiových podmínek, aby optimalizovalo spektrální účinnost při zachování zpětné kompatibility.

## Popis

Adaptive Quadrature Phase Shift Keying (AQPSK, adaptivní kvadraturní fázová manipulace) je sofistikovaná modulační technika specifikovaná ve standardech 3GPP [GERAN](/mobilnisite/slovnik/geran/) (GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network), která umožňuje dynamickou adaptaci mezi modulačními schématy Gaussian Minimum Shift Keying ([GMSK](/mobilnisite/slovnik/gmsk/)) a 8-Phase Shift Keying (8PSK). Adaptace probíhá pro každý časový slot v rámci struktury rámce GSM, což síti umožňuje optimalizovat přenosové parametry na základě aktuálních podmínek rádiového kanálu. Tento adaptivní přístup představuje významný vývoj oproti pevným modulačním schématům a poskytuje vyšší flexibilitu pro paketové datové služby v sítích GSM/EDGE.

Na technické úrovni AQPSK funguje tak, že vyhodnocuje metriky kvality kanálu, jako je poměr signálu k šumu (SNR), bitová chybovost ([BER](/mobilnisite/slovnik/ber/)) a poměr nosné k interferenci ([C/I](/mobilnisite/slovnik/c-i/)), aby určil optimální modulační schéma pro každou přenosovou příležitost. Když jsou podmínky kanálu příznivé, systém zvolí modulaci 8PSK, která přenáší 3 bity na symbol oproti 1 bitu na symbol u GMSK, čímž teoreticky ztrojnásobí spektrální účinnost. V náročných rádiových prostředích se systém automaticky vrátí k modulaci GMSK, která díky svým charakteristikám konstantní obálky a plynulým fázovým přechodům nabízí vyšší odolnost proti šumu a interferenci.

Implementace AQPSK zahrnuje několik klíčových komponent v architektuře GSM/EDGE. Základnová stanice ([BTS](/mobilnisite/slovnik/bts/)) obsahuje algoritmy pro adaptaci modulace, které činí rozhodnutí v reálném čase na základě zpětné vazby o kvalitě kanálu od mobilních stanic. Mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) musí podporovat demodulaci GMSK i 8PSK a poskytovat síti přesná měření kvality kanálu. Jednotka řízení paketů (PCU) hraje klíčovou roli v koordinaci adaptačního procesu pro paketově přepínané datové služby a zajišťuje plynulé přechody mezi modulačními schématy bez přerušení probíhající komunikace.

Role AQPSK v síti přesahuje pouhou adaptaci modulace; představuje základní prvek technologie Enhanced Data rates for GSM Evolution (EDGE). Dynamickým výběrem nejvhodnějšího modulačního schématu umožňuje AQPSK sítím GSM dosáhnout vyšších špičkových datových rychlostí (až 473,6 kbps v ideálních podmínkách) při zachování spolehlivého připojení v různých rádiových prostředích. Tato adaptivní schopnost je zvláště cenná pro mobilní datové služby, kde pohyb uživatelů vytváří neustále se měnící podmínky kanálu, a zajišťuje tak optimální výkon, ať jsou uživatelé v klidu s výbornou kvalitou signálu, nebo se pohybují v oblastech s významnými interferenčními útlumy.

Technické specifikace pro AQPSK jsou podrobně popsány v řadě dokumentů 3GPP, přičemž TS 45.001 definuje obecný popis fyzické vrstvy, TS 45.004 specifikuje modulační charakteristiky a TS 51.021 pokrývá aspekty síťové implementace. Tyto specifikace zajišťují interoperabilitu mezi zařízeními různých výrobců a zároveň poskytují potřebnou flexibilitu síťovým operátorům pro implementaci optimalizačních algoritmů přizpůsobených jejich konkrétním scénářům nasazení a požadavkům na služby.

## K čemu slouží

AQPSK byl vyvinut, aby řešil rostoucí poptávku po vyšších datových rychlostech v sítích GSM při zachování zpětné kompatibility s existující infrastrukturou a zařízeními. Jak mobilní datové služby získávaly na popularitě na počátku 21. století, omezení pevných modulačních schémat se stávalo stále zřetelnějším. [GMSK](/mobilnisite/slovnik/gmsk/), ačkoli robustní a spolehlivé, nabízelo omezenou spektrální účinnost, která omezovala maximální dosažitelné datové rychlosti. Zavedení technologie EDGE vyžadovalo sofistikovanější přístup, který by mohl poskytnout vyšší propustnost bez nutnosti kompletní výměny sítě.

Hlavním problémem, který AQPSK řeší, je kompromis mezi spektrální účinností a odolností přenosu v proměnných rádiových podmínkách. Předchozí systémy GSM používaly výhradně GMSK, které poskytovalo vynikající výkon při špatných signálových podmínkách, ale omezovalo maximální datové rychlosti na přibližně 171,2 kbps. Pevné implementace vyššího řádu modulace, jako je 8PSK, mohly poskytnout vyšší propustnost, ale trpěly špatným výkonem v náročných rádiových prostředích. Adaptivní přístup AQPSK elegantně řeší toto dilema dynamickým výběrem optimálního modulačního schématu na základě aktuálních podmínek kanálu.

Historický kontext ukazuje, že AQPSK se objevil jako součást vývoje EDGE v rámci 3GPP Release 9, navazující na předchozí práci v rámci standardizace GSM/EDGE. Technologie byla motivována potřebou prodloužit životnost sítí GSM při konkurenci s nově vznikajícími technologiemi 3G. Díky možnosti adaptivní modulace mohli operátoři GSM nabízet vylepšené datové služby bez okamžité migrace na zcela nové technologie rádiového přístupu. Tento přístup umožňoval postupnou evoluci sítě při ochraně stávajících investic do infrastruktury GSM, což bylo zvláště důležité pro operátory v rozvojových trzích nebo pro ty s rozsáhlým pokrytím GSM, které vyžadovaly spíše přírůstkové upgrady než revoluční změny.

## Klíčové vlastnosti

- Dynamická adaptace modulace mezi GMSK a 8PSK
- Adaptace pro každý časový slot v rámci struktury rámce GSM
- Rozhodovací algoritmy založené na kvalitě kanálu
- Zpětná kompatibilita se staršími zařízeními GSM
- Vylepšená spektrální účinnost až 3 bity na symbol
- Plynulý přechod mezi modulačními schématy bez přerušení služby

## Související pojmy

- [GMSK – Gaussian Minimum Shift Keying](/mobilnisite/slovnik/gmsk/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 45.001** (Rel-19) — GSM Physical Layer Introduction
- **TS 45.004** (Rel-19) — GSM/EDGE Modulation Specification
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [AQPSK na 3GPP Explorer](https://3gpp-explorer.com/glossary/aqpsk/)
